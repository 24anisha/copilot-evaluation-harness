import re
import json
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional
import difflib
from static_analysis_tools import (
    ToolResult,
    get_supported_tools,
    get_tool_run_fn,
)

def get_code_from_outcome(outcome: str, language: str) -> Optional[str]:
    start_marker = f"```{language}"
    end_marker = "```"
    
    start_index = outcome.find(start_marker)
    if start_index == -1:
        start_marker = "```"
        start_index = outcome.find(start_marker)
    
    if start_index == -1:
        return None
    
    end_index = outcome.find(end_marker, start_index + len(start_marker))
    if end_index == -1:
        return None
    
    extracted_text = outcome[start_index + len(start_marker):end_index].strip()
    return extracted_text

def replace_lines_in_file(file_path: Path, code_snippet: str, line_range: List[int]) -> Optional[str]:
    """Replace specified lines in a file with a given code snippet.

    Args:
        file_path (Path): The path to the file to modify.
        code_snippet (str): The code snippet to insert.
        line_range (List[int]): A list containing the start and end line numbers to replace.

    Returns:
        Optional[str]: The modified file contents as a string, or None if the file cannot be read.
    """
    try:
        # Read the original file contents
        file_contents = file_path.read_text().splitlines()
        
        # Replace the specified lines with the code snippet
        start_line, end_line = line_range
        modified_contents = (
            file_contents[:start_line] +  # Lines before the range
            [code_snippet.strip()] +      # The new code snippet
            file_contents[end_line:]      # Lines after the range
        )
        
        return "\n".join(modified_contents)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def evaluate_fix_with_tool(
        self,
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

        before_file_contents = before_file_path.read_text()
        after_results = []
        before_results = []
        tool_raw_output = []

        tool_fn = get_tool_run_fn(tool)

        cache_key = (str(repo_folder), tool)
        if cache_key in self.before_fix_evaluation:
            before_results = self.before_fix_evaluation[cache_key]
            print("USED CACHE KEY")
        else:
            before_results, _ = tool_fn(repo_folder)
            self.before_fix_evaluation[cache_key] = before_results

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

def score_fix(base_path: Path, relative_path: Path, language: str, model_response: str, task: str, line_range: List[int]) -> Dict[str, Any]:
    working_dir = base_path

    input_source_file_path = working_dir / relative_path
    input_source_file_contents = input_source_file_path.read_text()

    generated_fix = get_code_from_outcome(model_response, language)
    if generated_fix is None:
        return {
            "success": False,
            "error": "No fix code found in the model response",
            "score": 0,
            "reason": "No fix generated",
        }
    if task not in get_supported_tools:
        return {
            "success": False,
            "error": "Unsupported task",
            "score": 0,
            "reason": "Task is not supported",
        }
    
    after_file_content = replace_lines_in_file(input_source_file_path, generated_fix, line_range)

    score, reason, before_errors, after_errors = evaluate_fix_with_tool(
        task,
        working_dir,
        input_source_file_path,
        after_file_content
    )

    unidiff = "\n".join(
        list(
            difflib.unified_diff(
                input_source_file_contents.splitlines(),
                generated_fix.splitlines(),
                fromfile="before",
                tofile="after",
            )
        )
    )

    return {
        "success": score > 0,
        "score": score,
        "reason": reason,
        "errors_before": before_errors,
        "errors_after": after_errors,
        "unidiff": unidiff,
    }

if __name__ == "__main__":
    # Example usage
    base_path = Path("/path/to/repository")
    relative_path = Path("src/main.py")
    language = "typescript"
    task = "typescript_eslint"
    model_response = "// eslint-disable-next-line typescript_eslint-@typescript-eslint/no-unsafe-assignment\n"
    line_range = [4, 4]
    
    result = score_fix(base_path, relative_path, language, model_response, task, line_range)
    print(result)

