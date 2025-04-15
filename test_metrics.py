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
    
    #TODO: find fix python pass case

    def test_fix_js_fail(self):
        # Test case for fix scoring in python
        #case-434
        test_case = {
            "case_id": "case-434",
            "repo_name": "dthree/cash",
            "commit": "3e28dae8bdb71215d5034df9003f3ef2804c2754",
            "file_path": "dist/commands/unalias.js",
            "code_snippet": "    args = args;\n",
            "line_range": [
                9,
                9
            ],
            "command_specific_fields": {
                "static_analyzer": "eslint",
                "rule": "eslint-no-self-assign",
                "analyzer_error": "'args' is assigned to itself."
            },
            "language": "javascript",
            "prompt": ""
        }
        model_response = "---FIND\n```javascript\nargs = args;\n```\n---REPLACE\n```javascript\nthis.args = args;\n```\n---COMPLETE"
        
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

    def test_test_gen_js_pass(self):
        # Test case for test gen scoring in python
        #case-
        test_case = #TODO: find test_gen js pass case
        
        model_response = #TODO: find test_gen js pass case
        
        result = test_score.score_test(
            base_path=f"{self.base_path}",
            repo_folder_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
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

    def test_test_gen_js_fail(self):
        # Test case for test gen scoring in python
        #case-13
        test_case = {
            "case_id": "case-13",
            "repo_name": "tj/commander.js",
            "file_path": "lib/suggestSimilar.js",
            "code_snippet": "\n\nfunction suggestSimilar(word, candidates) {\n\n  if (!candidates || candidates.length === 0) return '';\n\n  // remove possible duplicates\n\n  candidates = Array.from(new Set(candidates));\n\n\n\n  const searchingOptions = word.startsWith('--');\n\n  if (searchingOptions) {\n\n    word = word.slice(2);\n\n    candidates = candidates.map((candidate) => candidate.slice(2));\n\n  }\n\n\n\n  let similar = [];\n\n  let bestDistance = maxDistance;\n\n  const minSimilarity = 0.4;\n\n  candidates.forEach((candidate) => {\n\n    if (candidate.length <= 1) return; // no one character guesses\n\n\n\n    const distance = editDistance(word, candidate);\n\n    const length = Math.max(word.length, candidate.length);\n\n    const similarity = (length - distance) / length;\n\n    if (similarity > minSimilarity) {\n\n      if (distance < bestDistance) {\n\n        // better edit distance, throw away previous worse matches\n\n        bestDistance = distance;\n\n        similar = [candidate];\n\n      } else if (distance === bestDistance) {\n\n        similar.push(candidate);\n\n      }\n\n    }\n\n  });\n\n\n\n  similar.sort((a, b) => a.localeCompare(b));\n\n  if (searchingOptions) {\n\n    similar = similar.map((candidate) => `--${candidate}`);\n\n  }\n\n\n\n  if (similar.length > 1) {\n\n    return `\\n(Did you mean one of ${similar.join(', ')}?)`;\n\n  }\n\n  if (similar.length === 1) {\n\n    return `\\n(Did you mean ${similar[0]}?)`;\n\n  }\n\n  return '';\n\n}\n",
            "line_range": [
                54,
                99
            ],
            "command_specific_fields": {
            "method_name": "suggestSimilar"
            },
            "language": "javascript",
            "commit": "970ecae402b253de691e6a9066fea22f38fe7431",
            "prompt": ""
        }
        
        model_response = """describe('suggestSimilar', () => {
  it('should return empty string for empty candidates array', () => {
    assert.strictEqual(suggestSimilar('test', []), '');
  });

  it('should return empty string for null candidates', () => {
    assert.strictEqual(suggestSimilar('test', null), '');
  });

  it('should suggest single similar word', () => {
    assert.strictEqual(suggestSimilar('tset', ['test']), '\n(Did you mean test?)');
  });

  it('should suggest multiple similar words', () => {
    assert.strictEqual(
      suggestSimilar('tset', ['test', 'tent']),
      '\n(Did you mean one of tent, test?)'
    );
  });

  it('should handle --option format', () => {
    assert.strictEqual(
      suggestSimilar('--tset', ['--test']),
      '\n(Did you mean --test?)'
    );
  });

  it('should remove duplicates from candidates', () => {
    assert.strictEqual(
      suggestSimilar('tset', ['test', 'test']),
      '\n(Did you mean test?)'
    );
  });

  it('should ignore single character candidates', () => {
    assert.strictEqual(suggestSimilar('a', ['b', 'c']), '');
  });

  it('should return empty string when no similar words found', () => {
    assert.strictEqual(suggestSimilar('xyz', ['abc', 'def']), '');
  });
});
    """
        
        result = test_score.score_test(
            base_path=f"{self.base_path}",
            repo_folder_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            language=test_case["language"],
            model_response=model_response,
            commit_sha=test_case["commit"],
            case_id=test_case["case_id"],
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
    # python -m unittest test_metrics.TestMetricsScoring.(test name e.g. test_fix_python)