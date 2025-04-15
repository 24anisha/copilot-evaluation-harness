import unittest
from pathlib import Path
from score_scripts import test_score, fix_score, doc_score, model_handler
from end_to_end_script import create_model_input
import os
from absl import flags
import sys
import anthropic

class TestMetricsScoring(unittest.TestCase):
    def setUp(self):
        # Common test data setup
        self.base_path = "out/repos/test_repo"  # Adjust path as needed
        
    def test_fix_python_pass(self):
        # Test case for fix scoring in python
        #case-68
        test_case = {
            "case_id": "case-68",
            "repo_name": "cool-RR/PySnooper",
            "commit": "f2c60de87f318a9c6b6c8b6887fe31bd07f91fb9",
            "file_path": "tests/mini_toolbox/pathlib.py",
            "code_snippet": "                or self._flavour is not other._flavour):\n",
            "line_range": [
                966,
                966
            ],
            "command_specific_fields": {
                "static_analyzer": "pylint",
                "rule": "pylint-no-member",
                "analyzer_error": "Instance of 'PurePath' has no '_flavour' member"
            },
            "language": "python",
            "prompt": ""
        }
        
        model_response = "For this error, we need to access the proper path flavor attribute. Here's the fix:\n\n---FIND\n```python\nor self._flavour is not other._flavour):\n```\n---REPLACE\n```python\nor self.drive != other.drive):\n```\n---COMPLETE\n\nThe error occurs because `_flavour` is not a proper attribute to access in modern Python path handling. Instead, comparing drives is the recommended way to check path compatibility. The `drive` attribute is a public API that's available in both `PurePath` and `Path` objects.\n\nNote: If you specifically need to compare path flavors, you could alternatively use `isinstance()` to check if the paths are of the same type."
        
        result = fix_score.score_fix(
            base_path=f"{self.base_path}",
            repo_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            task=test_case["command_specific_fields"]["static_analyzer"],
            language=test_case["language"],
            model_response=model_response,
            case_id=test_case["case_id"],
            test=True
        )
        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 1)
    
    def test_fix_python_fail(self):
        # Test case for fix scoring in python
        #case-199
        test_case = {
            "case_id": "case-199",
            "repo_name": "httpie/cli",
            "commit": "f4cf43ecdd6c5c52b5c4ba91086d5c6ccfebcd6d",
            "file_path": "httpie/ssl_.py",
            "code_snippet": "        ciphers: str = None,\n",
            "line_range": [
                73,
                73
            ],
            "command_specific_fields": {
                "static_analyzer": "pyright",
                "rule": "pyright-reportArgumentType",
                "analyzer_error": "Expression of type \"None\" cannot be assigned to parameter of type \"str\"\n\u00a0\u00a0\"None\" is not assignable to \"str\""
            },
            "language": "python",
            "prompt": ""
        }
        
        model_response = "---FIND\n```python\nciphers: str = None,\n```\n---REPLACE\n```python\nfrom typing import Optional\n\nciphers: Optional[str] = None,\n```\n---COMPLETE"
        
        result = fix_score.score_fix(
            base_path=f"{self.base_path}",
            repo_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            task=test_case["command_specific_fields"]["static_analyzer"],
            language=test_case["language"],
            model_response=model_response,
            case_id=test_case["case_id"],
            test=True
        )
        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is incorrect
        self.assertEqual(result["score"], 0)
    
if __name__ == '__main__':
    unittest.main() 
    # Usage for running a single test:
    # python -m unittest test_metrics.TestMetricsScoring.(test name e.g. test_fix_python)