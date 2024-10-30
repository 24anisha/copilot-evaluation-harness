# Copyright (c) Microsoft. All rights reserved.
"""Base class for evaluators. Evaluators score Copilot/LLM responses for specific metrics."""
import sys
import dataclasses
import re
import traceback
import tempfile
import mlflow
import matplotlib.pyplot as plt
import pandas as pd
import json
import os
import shutil
import numpy as np
from pathlib import Path
from abc import ABC
from typing import List, Tuple
from multiprocessing import Pool, cpu_count, Lock
from collections import Counter
from dataclasses import asdict
from scipy.stats import bootstrap

from evaluation_helper import EvaluationResult
from abs_conversation import get_state_file
from abs_state import get_workspace_folder, get_document_file_path
from syntax_parser import SyntaxParser
from test_case_parser import get_language_id_from_test_case
from os_helper import sanitize_print, set_print_lock
from timeout import EvalTimeoutError

def _print_reason_summary(failure_reasons: List[str]) -> None:
    """Prints a summary of the failure reasons"""
    # strip a case number from the reason
    failure_reasons2 = []
    # TODO: when we remove the case_number from the reason, we can remove this
    # *-4026.sim-requests-*.txt not found
    rex1 = re.compile(r"[*]-(\d+).sim-requests-[*].txt not found.*")
    # <class 'FileNotFoundError'> raised while running test suite [Errno 2] No such file or directory: '/tmp/eval_method_gen/test_case_879_0/.report.json'
    rex2 = re.compile(r"(.*/)test_case_(\d+_\d+)(/.*)")
    # Exception raised while evaluating test case case-1960 [panel] - case-1960: No test projects found for test generation of type nunit in the
    # conversation from candidate test projects [CsProj(name=LiteDB.Tests, path=LiteDB.Tests/LiteDB.Tests.csproj,
    # project_id=74E32E43-2A57-4A38-BD8C-9108B0DCAEAA)] ['xunit'] from question /tests Generate a nunit unit test for the method `FindOne`..: 1
    rex3 = re.compile(r"(.*)case[-_](\d+)(.*)case[-_](\d+)(.*type )(nunit|xunit)(.*)")
    # Exception raised while evaluating test case case-2215 [panel] - case-2215: [Errno 2] No such file or
    # directory: '/tmp/eval_test_gen/test_case_2215_0/YarnSpinner/YarnSpinner.csproj'
    rex5 = rex5 = re.compile(r"(.*)case[-_](\d+)(.*)case[-_](\d+)(: \[Errno 2\] No such file or directory:).*")
    # Exception raised while evaluating test case case-2246 [panel] - case-2246: No test projects found for test generation.
    rex4 = re.compile(r"(.*)case[-_](\d+)(.*)case[-_](\d+)(.*)")

    def sanitize_reason(reason):
        match1 = rex1.match(reason)
        match2 = rex2.match(reason)
        match3 = rex3.match(reason)
        match4 = rex4.match(reason)
        match5 = rex5.match(reason)
        if match1:
            reason = "*" + reason[2 + len(str(match1.group(1))) :]
        elif match5:
            reason = match5.group(1) + "case-***" + match5.group(3) + "case-***" + match5.group(5)
        elif match2:
            reason = match2.group(1) + "test_case_***" + match2.group(3)
        elif match3:
            reason = match3.group(1) + "case-***" + match3.group(3) + "case-***" + match3.group(5) + "***"
        elif match4:
            reason = match4.group(1) + "case-***" + match4.group(3) + "case-***" + match4.group(5)
        return reason

    for reason in failure_reasons:
        if not reason:
            reason = "Test succeeded"
        failure_reasons2.append(sanitize_reason(reason))
    agg_text = "Aggregate summary of test case failure reasons:\n"
    for reason, count in Counter(failure_reasons2).items():
        agg_text += f"\t{reason}: {count}\n"
    sanitize_print(agg_text)

class Evaluator(ABC):
    """Base class for evaluators. Evaluators score Copilot/LLM responses for specific metrics."""

    no_score = -1  # indicates filtered or exception rather than failure

    # pylint: disable=unused-argument
    def __init__(self, score_name: str, **kwargs):
        mlflow.autolog()
        self.score_name = score_name
        self.syntax_parser = SyntaxParser()
        self.publish_files = {}
        self.output_path = Path(".")  # path for evaluator output files
        self.evaluator_output_path = kwargs.pop("evaluator_output_path", None)

    def evaluate(self, simulator_input_folder: str, simulator_output_folder, **kwargs) -> Tuple[pd.DataFrame, List[dict]]:
        """
        ENTRY POINT INTO EACH EVALUATION.

        Evaluate the predictions on the dataset.

        Args:
            simulator_input_folder (str): the folder given from the simulator component containing simulator input
            simulator_output_folder (str): the folder given from the simulator component containing simulator output

        Returns:
            Tuple[pd.DataFrame, List[dict]]: the evaluation results data frame and score summary
        """
        sim_input_path = Path(simulator_input_folder) / "simulator_input"
        sim_output_path = Path(simulator_output_folder) / "simulator_output"
        eval_results = self.batch_score(sim_input_path, sim_output_path)
        eval_df = pd.DataFrame(map(dataclasses.asdict, eval_results))
        return eval_df, self.compute_score_summary(eval_df)

    def get_filtered_eval_result(self, case_number: int, n_id: str, language: str, test_case_id: str) -> EvaluationResult:
        """Creates an evaluation result for a filtered test case run"""
        return EvaluationResult(
            self.score_name,
            case_number,
            test_case_id,
            n_id,
            language,
            Evaluator.no_score,
            "Filtered",
            None,
            None,
            json.dumps({}),
        )

    def get_missing_post_file_eval_result(self, case_number: int, n_id: str, language: str, test_case_id: str) -> EvaluationResult:
        """Creates an evaluation result for a test case run with missing post files"""

        return EvaluationResult(
            self.score_name,
            case_number,
            test_case_id,
            n_id,
            language,
            Evaluator.no_score,
            "Missing post file",
            None,
            None,
            json.dumps({}),
        )

    def print_eval_result_report(self, results: List[EvaluationResult], n_test_cases: int):
        """Prints a report of the evaluation results, including filtration and language by language results"""

        result_info: dict = {}
        result_info_by_language: List[dict] = []

        if len(results) == 0:
            sanitize_print("No test case results found")
            return result_info, result_info_by_language

        n_filtered = len([r for r in results if r.reason == "Filtered"])
        result_info["n_filtered"] = n_filtered

        # print the raw failure reasons for each test case result
        sanitize_print("Reasons (from non-filtered cases):")
        reasons = Counter([m.reason for m in results])
        result_info["not_scored_reasons"] = reasons
        for reason, count in reasons.items():
            sanitize_print(f"\t{reason}: {count}")
        sorted_results = sorted(results, key=lambda x: (x.case_number, x.n_id))
        for result in sorted_results:
            if int(result.score) < 1:
                sanitize_print(f"Test {result.case_number} ({result.language}) (run n={result.n_id}) failed (score={int(result.score)}):")
                sanitize_print(f"\t{result.reason[:120]}")
                sanitize_print(f"\t{str(result.extra_data_json)[:12288]}")

        # summarize the result reasons
        _print_reason_summary([m.reason for m in results])

        # print the scoring summaries
        evaluation_df = pd.DataFrame(map(dataclasses.asdict, results))
        languages = evaluation_df.language.unique()
        for language in languages:
            test_cases_by_language = evaluation_df[evaluation_df.language == language]
            mean_score = test_cases_by_language["score"].apply(lambda x: 0 if x == Evaluator.no_score else x).mean()
            scored_tests = test_cases_by_language[test_cases_by_language.score != Evaluator.no_score]
            unscored_tests = test_cases_by_language[test_cases_by_language.score == Evaluator.no_score]
            syntax_pass_rate = self.syntax_parser.calculate_syntax_pass_rate(test_cases_by_language.post_file_syntax_pass)

            result_info_by_language.append(
                {
                    "Language": language,
                    "nTestCases": len(test_cases_by_language),
                    "nScored": len(scored_tests),
                    "nUnscored": len(unscored_tests),
                    "MeanScore": mean_score,
                }
            )
            sanitize_print(f"{language}:")
            sanitize_print(f"\t{len(test_cases_by_language)} tests run")
            sanitize_print(f"\t{len(scored_tests)} tests scored")
            sanitize_print(f"\t{len(unscored_tests)} unscored due to exceptions or filtering")
            sanitize_print(f"\tsuccess rate of tests scored: {mean_score}")
            sanitize_print(f"\tsyntax pass rate: {syntax_pass_rate}")
            mlflow.log_metric(f"{self.score_name}_{language}_mean", mean_score)

        result_info["n_test_cases"] = n_test_cases
        result_info["n_filtered"] = n_filtered
        result_info["filtration_rate"] = n_filtered / n_test_cases
        result_info["syntax_pass_rate_original_files"] = self.syntax_parser.calculate_syntax_pass_rate(evaluation_df.original_file_syntax_pass)
        result_info["syntax_pass_rate_post_files"] = self.syntax_parser.calculate_syntax_pass_rate(evaluation_df.post_file_syntax_pass)
        sanitize_print(f"{n_test_cases} tests requested in total")
        sanitize_print("Filtration rate:", n_filtered / n_test_cases)
        sanitize_print(
            "Syntax pass rate for original files:",
            result_info["syntax_pass_rate_original_files"],
        )
        sanitize_print(
            "Syntax pass rate for post files:",
            result_info["syntax_pass_rate_post_files"],
        )
        return result_info, result_info_by_language

    def score_test_cases_sequentially(
        self,
        simulator_input_folder: Path,
        simulator_output_folder: Path,
        working_dir,
        test_case_reports,
    ) -> List[EvaluationResult]:
        """Score a list of TestCaseReport sequentially."""
        results: List[EvaluationResult] = []
        for test_case_report in test_case_reports:
            results.extend(
                self.run_test_case_eval(
                    test_case_report,
                    simulator_input_folder,
                    working_dir,
                    simulator_output_folder,
                )
            )
        return results

    # pylint: disable=too-many-statements
    def batch_score(
        self,
        simulator_input_folder: Path,
        simulator_output_folder: Path,
    ) -> List[EvaluationResult]:
        """Override-able method to score a batch of Copilot predictions."""

        # Move input files to temporary directory so that evaluations such as /fix can modify them
        # If the eval folder exists, remove it.
        tempdir = tempfile.gettempdir()
        working_dir = Path(tempdir) / f"eval_{self.score_name}"
        if working_dir.exists():
            shutil.rmtree(str(working_dir), ignore_errors=True)

        # Only uncomment this when debugging
        # sanitize_print(f"Copying {simulator_input_folder} to {working_dir}")
        # shutil.copytree(simulator_input_folder, working_dir)

        test_case_reports = json.loads((Path(simulator_output_folder) / "test_case_reports.json").read_text())
        sanitize_print(f"Found {len(test_case_reports)} test cases in {working_dir}")
        flat = lambda ls: [x for y in ls for x in y]
        ces_execute_tests = os.environ.get("CES_EVALUATE_ONLY_TEST_NUMBERS")
        if ces_execute_tests:
            execute_only_case_numbers = [int(x) for x in ces_execute_tests.split(',')]
            if execute_only_case_numbers:
                test_case_reports = [c for c in test_case_reports if c.get("case_number", -1) in execute_only_case_numbers]

        # Test whether parallelism should be used
        # If the environment variable is not set, use the default setting in this code.
        # The environment variable value must be a string convertable to int and then to bool
        #   0 means execute sequential,
        #   non-zero integral value means execute in parallel
        #   alphabetic characters result in default behavior ("False" and "True" result in using the default in this code)
        # If the reports don't have a repo, it isn't clear that parallelism can be used safely, so use sequential processing.
        use_parallelism = False
        ces_use_eval_parallelism = None
        try:
            ces_use_eval_parallelism = bool(int(os.environ.get("CES_USE_EVAL_PARALLELISM")))
        except:
            ces_use_eval_parallelism = None
        if ces_use_eval_parallelism:
            use_parallelism = True
        else:
            if test_case_reports:
                with open(simulator_input_folder / test_case_reports[0]["conversation_file_path"], 'rt') as tcr_file:
                    conversation = json.load(tcr_file)
                repo_folder = conversation[0].get('repo_folder')
                use_parallelism = bool(repo_folder)

        if use_parallelism:
            parallel_test_case_reports = {}
            for tcr in test_case_reports:
                with open(simulator_input_folder / tcr["conversation_file_path"], 'rt') as tcr_file:
                    conversation = json.load(tcr_file)
                repo_folder = conversation[0].get('repo_folder')
                if not parallel_test_case_reports.get(repo_folder):
                    parallel_test_case_reports[repo_folder] = []
                parallel_test_case_reports[repo_folder].append(tcr)

            set_print_lock(Lock())

            # TODO: delete this tracing
            print(f"ces_use_eval_parallelism={ces_use_eval_parallelism}, use_parallelism={use_parallelism}, len(parallel_test_case_reports)={len(parallel_test_case_reports)}")
            for repo_folder, tcr_list in parallel_test_case_reports.items():
                print(repo_folder)
                for tcr in tcr_list:
                    # print('   ', dataclasses.asdict(tcr))
                    print('   ', tcr)

        # use_parallelism = False
        if use_parallelism:
            with Pool(cpu_count()) as pool:
                results = flat(
                    list(
                        pool.starmap(
                            # self.run_test_case_eval,
                            # [
                            #     (
                            #         test_case_report,
                            #         simulator_input_folder,
                            #         working_dir,
                            #         simulator_output_folder,
                            #     )
                            #     for test_case_report in test_case_reports
                            # ],
                            self.score_test_cases_sequentially,
                            [
                                (
                                    simulator_input_folder,
                                    simulator_output_folder,
                                    working_dir,
                                    test_case_report_list,
                                )
                                for _repo_folder, test_case_report_list in parallel_test_case_reports.items()
                            ],
                        )
                    )
                )
        else:
            results = self.score_test_cases_sequentially(simulator_input_folder, simulator_output_folder, working_dir, test_case_reports)

        if len(results) == 0:
            raise ValueError("No test results found from simulator.")

        # Save the results to a file
        self.publish_files["cpcResults"] = f"{self.output_path}/results.json"
        with open(self.publish_files["cpcResults"], "wt") as results_file:
            json.dump(list(map(asdict, results)), results_file, indent=4)

        # Save the scored results to files: .json and .md
        scored_results = [asdict(result) for result in results if result.score != Evaluator.no_score]
        self.publish_files["cpcScoredResults"] = f"{self.output_path}/scored_results.json"
        with open(self.publish_files["cpcScoredResults"], "wt") as results_file:
            json.dump(scored_results, results_file, indent=4)

        # print the results
        result_info, result_info_by_language = self.print_eval_result_report(results, len(test_case_reports))

        # Save the result summaries to files
        self.publish_files["cpcMetricScorecard"] = f"{self.output_path}/metric_scorecard.json"
        with open(self.publish_files["cpcMetricScorecard"], "wt") as result_info_file:
            json.dump(result_info, result_info_file, indent=4)
        with open(f"{self.output_path}/metric_scorecard_by_language.json", "wt") as result_info_file:
            json.dump(result_info_by_language, result_info_file, indent=4)

        try:
            if working_dir.exists():
                shutil.rmtree(str(working_dir), ignore_errors=True)
        except:
            print("Unable to delete the working dir")

        return results

    # pylint: disable=too-many-statements
    def run_test_case_eval(
        self,
        test_case_report: dict,
        simulator_input_folder: Path,
        working_dir: Path,
        simulator_output_folder: Path,
    ):
        """Parallelizable run method for conversation files"""

        results: List[EvaluationResult] = []
        case_number = test_case_report["case_number"]
        try:
            conversation_path = simulator_input_folder / test_case_report["conversation_file_path"]
            outcomes = test_case_report["outcomes"]
            conversation = json.loads(conversation_path.read_text())
            state_path = get_state_file(conversation)
            state = json.loads((conversation_path.parent / state_path).read_text())
            language = get_language_id_from_test_case(conversation, state)

            workspace_folder = get_workspace_folder(state)
            document_file_path = get_document_file_path(state, "unknown")
            document_abs_path = (
                conversation_path.parent / document_file_path
                if workspace_folder is None or document_file_path == "unknown"
                else simulator_input_folder / conversation_path.parent / workspace_folder / document_file_path
            )
        except Exception as e:
            traceback.print_exc()
            results.append(
                EvaluationResult(
                    self.score_name,
                    case_number,
                    test_case_report["test"],
                    "0",
                    "",
                    Evaluator.no_score,
                    "Exception raised while loading test case: " + str(e),
                    None,
                    None,
                    json.dumps({}),
                )
            )
            return results

        # 3. Iterate through each of n runs through this test case
        for n_id, outcome in enumerate(outcomes):
            if outcome["hit_content_filter"]:
                results.append(self.get_filtered_eval_result(case_number, n_id, language, test_case_report["test"]))
                continue

            # Retrieve post files for this n_id
            post_files = [simulator_output_folder / Path(p) for p in outcome.get("post_files", [])]

            # Prepare isolated working directory
            cwd = os.getcwd()
            isolated_working_dir = working_dir / f"test_case_{case_number}_{n_id}"

            # Copy files to isolated working directory
            try:
                if workspace_folder:
                    # If there is a workspace folder then we should copy
                    # the contents of the workspace folder to the isolated working dir
                    shutil.copytree(
                        conversation_path.parent / workspace_folder,
                        isolated_working_dir,
                    )
                else:
                    if "repos/" in str(document_file_path):
                        # HACK: remove this case once workspace folders are given
                        part_index = document_file_path.parts.index("repos")
                        relative_parts = document_file_path.parts[: part_index + 2]
                        repo_name = relative_parts[-1]
                        (isolated_working_dir / "repos").mkdir(parents=True, exist_ok=True)
                        shutil.copytree(
                            simulator_input_folder / Path().joinpath(*relative_parts),
                            isolated_working_dir / "repos" / repo_name,
                        )
                    else:
                        # If there is no workspace folder then we should copy
                        # the document file itself to the isolated working dir
                        # QUESTION: is the document file path relative to the data asset folder root or the conversation path?
                        isolated_working_dir.mkdir(parents=True, exist_ok=True)
                        shutil.copy(
                            conversation_path.parent / document_file_path,
                            isolated_working_dir,
                        )

                evaluation_results = self.evaluate_test_case(
                    isolated_working_dir,
                    simulator_output_folder,
                    case_number,
                    test_case_report["test"],
                    n_id,
                    state,
                    conversation,
                    language,
                    document_abs_path,
                    outcome,
                    post_files,
                )
                results.extend(evaluation_results)
            except KeyboardInterrupt:
                sys.exit(1)
            except EvalTimeoutError as e:
                print(f'EvalTimeoutError exception raised while evaluating test case {test_case_report.get("test", "Unknown test")}: ')
                _exc_type, _exc, exc_tb = sys.exc_info()
                formatted_exception = traceback.format_exception(e, e, exc_tb)
                results.append(
                    EvaluationResult(
                        self.score_name,
                        case_number,
                        test_case_report["test"],
                        n_id,
                        language,
                        Evaluator.no_score,
                        f'Exception raised while evaluating test case {test_case_report.get("test", "Unknown test")}: ' + str(e),
                        self.syntax_parser.check_syntax_by_file([document_abs_path], language),
                        self.syntax_parser.check_syntax_by_file(post_files, language),
                        json.dumps(formatted_exception),
                    )
                )
            except Exception as e:
                print(f'Exception raised while evaluating test case {test_case_report.get("test", "Unknown test")}: ')
                # traceback.print_exc()
                _exc_type, _exc, exc_tb = sys.exc_info()
                formatted_exception = traceback.format_exception(e, e, exc_tb)
                results.append(
                    EvaluationResult(
                        self.score_name,
                        case_number,
                        test_case_report["test"],
                        n_id,
                        language,
                        Evaluator.no_score,
                        f'Exception raised while evaluating test case {test_case_report["test"]}: ' + str(e),
                        self.syntax_parser.check_syntax_by_file([document_abs_path], language),
                        self.syntax_parser.check_syntax_by_file(post_files, language),
                        json.dumps(formatted_exception),
                    )
                )
            finally:
                try:
                    os.chdir(cwd)
                    shutil.rmtree(str(isolated_working_dir), ignore_errors=True)
                except:
                    print("Unable to remove isolated working dir")

        if not results:
            sanitize_print(f"No results for {case_number}")

        return results

    # pylint: disable=too-many-arguments
    def evaluate_test_case(
        self,
        working_dir: Path,
        simulator_output_folder: Path,
        case_number: str,
        test_case_id: str,
        n_id: str,
        state: dict,
        conversation: dict,
        language: str,
        document_abs_path: Path,
        outcome: dict,
        post_files: List[Path],
    ) -> List[EvaluationResult]:
        """Override-able method to score a single Copilot test case result.

        Args:
            working_dir (Path): The working directory containing the simulator input (copied to the tmp directory so that edits are possible)
            simulator_output_folder (Path): The simulator output folder.
            case_number (str): The identifier number in the path in the associated conversation json file.
            n_id (str): The identifier number for the ith run corresponding to the simulator's --n parameter.
            state (dict): The state file object
            conversation (dict): The conversation file object
            language (str): The language of the test case.
            sim_requests (List[dict]): The list of requests and responses made as part of the simulation
            sim_log (str): The simulation log file contents
            post_files (List[Path]): File paths to associated post files produced by the simulator
            original_file_syntax_pass (Dict[str, bool]): Pass this along to the EvaluationResults returned.
            post_file_syntax_pass (Dict[str, bool]): Pass this along to the EvaluationResults returned.

        Returns:
            List[EvaluationResult] of the evaluation outcomes for this test case.

        """
        raise NotImplementedError

    def compute_score_summary(self, evaluation_df: pd.DataFrame) -> List[dict]:
        """
        Compute the summary of the scores assuming all scores are floats.

        Args:
            scores (pd.Series): The scores.
        """
        scores = evaluation_df["score"][evaluation_df["score"] != Evaluator.no_score]
        rng = np.random.default_rng()
        try:
            bootstrap_std = bootstrap([scores], np.mean, confidence_level=0.9, random_state=rng)
            conf_int = f"({bootstrap_std.confidence_interval[0]:.3f}, {bootstrap_std.confidence_interval[1]:.3f})"
            std_err = bootstrap_std.standard_error
        except ValueError:
            conf_int = np.nan
            std_err = np.nan
        mean, median, count = scores.mean(), scores.median(), scores.count()
        mlflow.log_metrics(
            {
                f"{self.score_name}_mean": mean,
                f"{self.score_name}_median": median,
                f"{self.score_name}_std_err": std_err,
                f"{self.score_name}_count": count,
            }
        )

        # Plot lexicographically sorted test run id against score for a visually comparable plot between runs
        evaluation_df["test_run_id"] = evaluation_df.apply(lambda x: f"{x['case_number']}_{x['n_id']}", axis=1)
        sorted_scores = evaluation_df.sort_values(["test_run_id"])
        plot_file_name = "scores.png"
        plt.figure(figsize=(10, 6))
        plt.plot(sorted_scores["test_run_id"], sorted_scores["score"])
        plt.title("Test Run Scores")
        plt.xlabel("test_run_id")
        plt.ylabel("score")
        plt.savefig(plot_file_name)
        mlflow.log_artifact(plot_file_name, "test_run_results")

        return [
            {
                "metric": self.score_name,
                "mean": mean,
                "median": median,
                "std_err": std_err,
                "confidence_interval": conf_int,
                "count": count,
            }
        ]
