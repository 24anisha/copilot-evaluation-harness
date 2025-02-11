"""Evaluating Copilot for /generate retrieval"""

import json
import traceback
from typing import List, Optional
from pathlib import Path
from plum.utils.test_report_parsers import (
    get_js_test_failures,
    get_pytest_test_failures,
)

from abs_conversation import get_method_original_string
from abs_state import get_document_file_path, get_original_repo_name
from plum_exec_tools import run_test_suite
from base_evaluator import EvaluationResult, Evaluator


def get_test_failures(
        self,
        before_change_results: List[dict],
        after_change_results: List[dict],
        language: str,
        test_library: Optional[str],
    ):
        """Compare test suite results before and after applying Copilot method generation and return any additional tests failed."""

        if language in ("javascript", "typescript"):
            return get_js_test_failures(before_change_results, after_change_results, test_library=test_library)

        if language == "python":
            return get_pytest_test_failures(before_change_results, after_change_results)

        if language in ("java", "csharp"):
            # HACK: After change results will be ["BUILD ERROR"], thus not empty and failing the test, if the build failed
            return after_change_results

        if language == "cpp":
            return after_change_results

        raise NotImplementedError

# pylint: disable=too-many-arguments
def evaluate_test_case(
    self,
    working_dir: Path,
    _: Path,
    case_number: str,
    test_case_id: str,
    n_id: str,
    state: dict,
    conversation: dict,
    language: str,
    document_abs_path: Path,
    __: dict,
    post_files: List[Path],
) -> List[EvaluationResult]:
    """Scores each bug based on whether Copilot generated a valid method."""

    if len(post_files) == 0:
        return [self.get_missing_post_file_eval_result(case_number, n_id, language, test_case_id)]
    if len(post_files) > 1:
        print("TOO MANY POST FILES DETECTED: Expected 1 but got", len(post_files))

    post_file_path = post_files[0]
    print(f"post_file_path: {post_file_path}")

    before_change_results, after_change_results = None, None
    original_method_string = get_method_original_string(conversation)
    file_path = working_dir / get_document_file_path(state)
    original_file_contents = file_path.read_text()
    post_file_contents = post_file_path.read_text()
    original_repo_name = get_original_repo_name(state)
    failure_reasons = []

    try:
        # Replace comment line with original method body, run test suite, get before change test results
        before_change_results, _ = run_test_suite(working_dir, language, original_repo_name=original_repo_name)

        # Replace the file with the post file contents, run test suite, get after change results
        file_path.write_text(post_file_contents.replace(original_method_string, ""))
        after_change_results, test_library_tool = run_test_suite(working_dir, language, original_repo_name=original_repo_name)

        failed_tests = self.get_test_failures(
            before_change_results,
            after_change_results,
            language,
            test_library_tool,
        )

        if len(failed_tests) == 0:
            score = 1
        else:
            score = 0
            failure_reasons.append("Generated method caused additional test failures")
    except Exception as e:
        traceback.print_exc()
        score = Evaluator.no_score
        failure_reasons.append(
            f"{type(e)} raised while running test suite {e}",
        )
        print(f"{type(e)} raised while running test case number {case_number}: {e.args}")
        traceback.print_exception(e)
    finally:
        file_path.write_text(original_file_contents)

    syntax_is_correct = self.syntax_parser.file_contents_syntax_check(post_file_contents, language)
    if not syntax_is_correct:
        score = 0
        failure_reasons.append("Syntax error in post file")

    return [
        EvaluationResult(
            self.score_name,
            case_number,
            test_case_id,
            n_id,
            language,
            score,
            ",".join(failure_reasons),
            self.syntax_parser.check_syntax_by_file([document_abs_path], language),
            self.syntax_parser.check_syntax_by_file(post_files, language),
            json.dumps(
                {
                    "post_file_path": str(post_file_path.resolve()),
                    "original_method_string": original_method_string,
                    # "post_file_contents": post_file_contents,  # TODO this is for debugging
                    # "new_file_contents": new_file_contents  # TODO this is for debugging
                    # "failed_tests": failed_tests,
                }
            ),
        )
    ]
