import unittest
from pathlib import Path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from score_scripts import fix_score
from end_to_end_script import create_model_input
from absl import flags

class TestFixScoring(unittest.TestCase):
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
            commit_sha=test_case["commit"],
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
            commit_sha=test_case["commit"],
            test=True
        )
        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is incorrect
        self.assertEqual(result["score"], 0)
    
    def test_fix_js_pass(self):
        # Test case for fix scoring in javascript on a passing case
        #case-455
        test_case = {
            "case_id": "case-455",
            "repo_name": "javve/list.js",
            "commit": "0c947162b5fc7af515ba2b9340b7e5e45a63fee5",
            "file_path": "src/fuzzy-search.js",
            "code_snippet": "      if (values.hasOwnProperty(value)) {\n",
            "line_range": [
                46,
                46
            ],
            "command_specific_fields": {
                "static_analyzer": "eslint",
                "rule": "eslint-no-prototype-builtins",
                "analyzer_error": "Do not access Object.prototype method 'hasOwnProperty' from target object."
            },
            "language": "javascript",
            "prompt": ""
        }

        model_response = ""
        
        result = fix_score.score_fix(
            base_path=f"{self.base_path}",
            repo_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            task=test_case["command_specific_fields"]["static_analyzer"],
            language=test_case["language"],
            model_response=model_response,
            case_id=test_case["case_id"],
            commit_sha=test_case["commit"],
            test=True
        )
        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 1)

    def test_fix_js_fail(self):
        # Test case for fix scoring in javascript on a failing case
        #case-454
        test_case = {
            "case_id": "case-454",
            "repo_name": "purifycss/purifycss",
            "commit": "be52c1c6b1b6e287b6989428c57f05a79aa135dc",
            "file_path": "lib/purifycss.es.js",
            "code_snippet": "                throw _iteratorError;\n",
            "line_range": [
                803,
                803
            ],
            "command_specific_fields": {
                "static_analyzer": "eslint",
                "rule": "eslint-no-unsafe-finally",
                "analyzer_error": "Unsafe usage of ThrowStatement."
            },
            "language": "javascript",
            "prompt": ""
        }
        model_response = ""
        
        result = fix_score.score_fix(
            base_path=f"{self.base_path}",
            repo_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            task=test_case["command_specific_fields"]["static_analyzer"],
            language=test_case["language"],
            model_response=model_response,
            case_id=test_case["case_id"],
            commit_sha=test_case["commit"],
            test=True
        )
        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 0)
    
    def test_fix_ts_pass(self):
        # Test case for fix scoring in typescript on a passing case
        #case-567
        test_case = {
            "case_id": "case-567",
            "repo_name": "grid-js/gridjs",
            "commit": "9a6a53eacdc019c01decfdfa8e77cb800922de3d",
            "file_path": "src/pipeline/pipeline.ts",
            "code_snippet": "  ): PipelineProcessor<T, P> | undefined {\n",
            "line_range": [
                106,
                106
            ],
            "command_specific_fields": {
                "static_analyzer": "tsc",
                "rule": "tsc-Error TS2344: Type '{0}' does not satisfy the constraint '{1}'.",
                "analyzer_error": "Type 'P' does not satisfy the constraint 'Partial<PipelineProcessorProps>'."
            },
            "language": "typescript",
            "prompt": ""
        }

        model_response = "To fix this error, we need to ensure that the generic type `P` extends `Partial<PipelineProcessorProps>`. Here's the correction:\n\n---FIND\n```typescript\n): PipelineProcessor<T, P> | undefined {\n```\n\n---REPLACE\n```typescript\n): PipelineProcessor<T, P extends Partial<PipelineProcessorProps>> | undefined {\n```\n\n---COMPLETE\n\nThe fix adds a type constraint to the generic parameter `P` using the `extends` keyword, ensuring that `P` must be a type that extends `Partial<PipelineProcessorProps>`. This satisfies the TypeScript constraint error."
        
        result = fix_score.score_fix(
            base_path=f"{self.base_path}",
            repo_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            task=test_case["command_specific_fields"]["static_analyzer"],
            language=test_case["language"],
            model_response=model_response,
            case_id=test_case["case_id"],
            commit_sha=test_case["commit"],
            test=True
        )
        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 1)

    def test_fix_ts_fail(self):
        # Test case for fix scoring in typescript on a failing case
        #case-551
        test_case = {
            "case_id": "case-551",
            "repo_name": "nexe/nexe",
            "commit": "5219a2ac74f97e644127ea37f000daa4b39da538",
            "file_path": "src/compiler.ts",
            "code_snippet": "  @bound\n",
            "line_range": [
                175,
                175
            ],
            "command_specific_fields": {
                "static_analyzer": "tsc",
                "rule": "tsc-Error TS1241: Unable to resolve signature of method decorator when called as an expression.",
                "analyzer_error": "Unable to resolve signature of method decorator when called as an expression."
            },
            "language": "typescript",
            "prompt": ""
        }

        model_response = "Here's how to fix the decorator error:\n\n---FIND\n```typescript\n@bound\n\n```\n---REPLACE\n```typescript\n@bound()\n\n```\n---COMPLETE\n\nThe fix adds parentheses after the decorator name since decorators can be called as functions. This is a common syntax error with decorators - they need to be either:\n1. Called as a function with parentheses `@decorator()`\n2. Or referenced directly without parentheses but must be a valid decorator function `@decorator`\n\nIn this case, `bound` appears to be a decorator factory that needs to be called, so parentheses are required."
        
        result = fix_score.score_fix(
            base_path=f"{self.base_path}",
            repo_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            task=test_case["command_specific_fields"]["static_analyzer"],
            language=test_case["language"],
            model_response=model_response,
            case_id=test_case["case_id"],
            commit_sha=test_case["commit"],
            test=True
        )
        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 0)

if __name__ == '__main__':
    unittest.main() 
    # Usage for running a single test:
    # python -m unittest tests.fix_tests.TestFixScoring.(test name e.g. test_fix_python_pass)