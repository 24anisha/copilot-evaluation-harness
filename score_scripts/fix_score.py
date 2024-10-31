import json
from pathlib import Path
from typing import Dict, Any, List, Tuple
import difflib
from static_analysis_tools import (
    ToolResult,
    get_supported_tools,
    get_tool_run_fn,
)

def evaluate_fix_with_tool(
        tool: str,
        repo_folder: Path,
        before_file_path: Path,
        after_file_contents: str,
    ) -> Tuple[float, str, List[ToolResult], List[ToolResult]]:
        """Evaluate the quality of a fix generated by Copilot.

        Args:
            tool (str): The tool to use for evaluation, e.g. pylint, pyright, tsc

        Returns:
            Tuple[float, str, list, list]: A tuple containing the score, reason, and the before and after errors.
        """
        before_fix_evaluation = {}
        before_file_contents = before_file_path.read_text()
        after_results = []
        before_results = []
        tool_raw_output = []

        tool_fn = get_tool_run_fn(tool)

        cache_key = (str(repo_folder), tool)
        if cache_key in before_fix_evaluation:
            before_results = before_fix_evaluation[cache_key]
            print("USED CACHE KEY")
        else:
            before_results, _ = tool_fn(repo_folder)
            before_fix_evaluation[cache_key] = before_results

        try:
            before_file_path.write_text(after_file_contents)
            after_results, tool_raw_output = tool_fn(repo_folder)

            # There should never be a case of missing before results, so if it is None or an empty list, then there was a tool failure.
            # We can't tell the difference between a tool failure and all problems fixed for after_results. But since that check comes
            # after the check for before_results, it shouldn't cause an issue in practice even though in theory, it could.
            if not before_results:
                score = 0
                reason = f"{tool} failed to run on before fix file"
            elif after_results is None:
                score = 0
                reason = f"{tool} failed to run on after fix file"
            elif len(before_results) > len(after_results):
                score = 1
                reason = f"({tool}) After fix has fewer errors"
            elif len(before_results) == len(after_results):
                score = 0
                reason = f"({tool}) After fix has the same # of errors"
            else:
                score = 0
                reason = f"({tool}) After fix has more errors"
        except:
            score = 0
            reason = f"({tool}) After fix failed to run"
        finally:
            before_file_path.write_text(before_file_contents)

        return score, reason, before_results or [], after_results or [tool_raw_output]

def score_fix(base_path: Path, relative_path: Path, model_response: str, task: str, language: str) -> Dict[str, Any]:
    working_dir = base_path

    input_source_file_path = working_dir / relative_path
    input_source_file_contents = input_source_file_path.read_text()

    if task not in get_supported_tools():
        return {
            "metric": "fix",
            "success": False,
            "score": 0,
            "language": language,
            "reason": "tool is not supported",
            "original_file_syntax_pass": "",
            "post_file_syntax_pass": "",
            "extra_data_json": ""
        }

    score, reason, before_errors, after_errors = evaluate_fix_with_tool(
        tool=task,
        repo_folder=working_dir,
        before_file_path=input_source_file_path,
        after_file_contents=model_response
    )

    unidiff = "\n".join(
        list(
            difflib.unified_diff(
                input_source_file_contents.splitlines(),
                model_response.splitlines(),
                fromfile="before",
                tofile="after",
            )
        )
    )

    return {
        "metric": "fix",
        "success": score > 0,
        "score": score,
        "language": language,
        "reason": reason,
        "original_file_syntax_pass": before_errors,
        "post_file_syntax_pass": after_errors,
        "extra_data_json": json.dumps(
            {
                "unidiff": unidiff,
            }
        )
    }

if __name__ == "__main__":
    # Example usage
    base_path = Path("/mnt/c/users/rahul/nasty_python")
    relative_path = Path("main.py")
    task = "pylint"
    language = "python"
    model_response = ""
    
    result = score_fix(base_path, relative_path, model_response, task, language)
    print(result)

