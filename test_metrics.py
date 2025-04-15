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
        # Test case for fix scoring in javascript
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

    def test_test_gen_python_pass(self):
        # Test case for test gen scoring in python
        #case-1663
        test_case = {
    "case_id": "case-1663",
    "repo_name": "trekhleb/learn-python",
    "file_path": "src/modules/sound_package/formats/wav.py",
    "code_snippet": "\n\ndef wav_read():\n\n    \"\"\"WAV file reading function mock\"\"\"\n\n    return 'Read from WAV file'\n",
    "line_range": [
        2,
        6
    ],
    "command_specific_fields": {
        "method_name": "wav_read"
    },
    "language": "python",
    "commit": "52c3a655cc2efd5ac01004f6f529c3262812a84e",
    "prompt": ""
}
        
        model_response = """import unittest
from src.modules.sound_package.formats.wav import wav_read

class TestWavRead(unittest.TestCase):
    def test_wav_read_returns_string(self):
        result = wav_read()
        self.assertEqual(result, 'Read from WAV file')
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()"""
        
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
    
    def test_test_gen_python_fail(self):
        # Test case for test gen scoring in python
        #case-1679
        test_case = {
    "case_id": "case-1679",
    "repo_name": "lra/mackup",
    "file_path": "mackup/utils.py",
    "code_snippet": "\n\ndef is_process_running(process_name):\n\n    \"\"\"\n\n    Check if a process with the given name is running.\n\n\n\n    Args:\n\n        (str): Process name, e.g. \"Sublime Text\"\n\n\n\n    Returns:\n\n        (bool): True if the process is running\n\n    \"\"\"\n\n    is_running = False\n\n\n\n    # On systems with pgrep, check if the given process is running\n\n    if os.path.isfile(\"/usr/bin/pgrep\"):\n\n        dev_null = open(os.devnull, \"wb\")\n\n        returncode = subprocess.call([\"/usr/bin/pgrep\", process_name], stdout=dev_null)\n\n        is_running = bool(returncode == 0)\n\n\n\n    return is_running\n",
    "line_range": [
        271,
        291
    ],
    "command_specific_fields": {
        "method_name": "is_process_running"
    },
    "language": "python",
    "commit": "0def08b8543ac3a436257cce4426a5b109b31a2d",
    "prompt": ""
}
        
        model_response = """import os
import subprocess
from unittest import TestCase
from unittest.mock import patch

class TestIsProcessRunning(TestCase):

    @patch('os.path.isfile')
    @patch('subprocess.call')
    def test_process_running(self, mock_call, mock_isfile):
        mock_isfile.return_value = True
        mock_call.return_value = 0
        
        self.assertTrue(is_process_running("test_process"))
        mock_call.assert_called_once()
        mock_isfile.assert_called_once_with("/usr/bin/pgrep")

    @patch('os.path.isfile') 
    @patch('subprocess.call')
    def test_process_not_running(self, mock_call, mock_isfile):
        mock_isfile.return_value = True
        mock_call.return_value = 1
        
        self.assertFalse(is_process_running("test_process"))
        mock_call.assert_called_once()
        mock_isfile.assert_called_once_with("/usr/bin/pgrep")

    @patch('os.path.isfile')
    def test_pgrep_not_available(self, mock_isfile):
        mock_isfile.return_value = False
        
        self.assertFalse(is_process_running("test_process"))
        mock_isfile.assert_called_once_with("/usr/bin/pgrep")"""
        
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
        self.assertEqual(result["score"], 0)

    def test_test_gen_js_pass(self):
        # Test case for test gen scoring in python
        #case-
        #test_case = #TODO: find test_gen js pass case
        
        #model_response = #TODO: find test_gen js pass case
        
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
        
    def test_model_input_fix(self):
        # no optional prompt passed
        if not flags.FLAGS.is_parsed():
            flags.FLAGS(["test_metrics.py", "--metric=fix"])
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

        model_input = create_model_input(test_case, self.base_path)

        self.assertNotEqual(model_input.splitlines()[1], "</prompt>") # checks that prompt is not empty
        self.assertNotEqual(model_input.splitlines()[-2], "<code>") # checks that code is not empty

        self.assertEqual(model_input.splitlines()[1], f"Fix this error: {test_case['command_specific_fields']['analyzer_error']}. Format as ---FIND ```language <errored code>``` ---REPLACE ```language <fixed code>```---COMPLETE.") #checks that prompt is correct
    
    def test_model_input_test_gen(self):
        # no optional prompt passed
        if not flags.FLAGS.is_parsed():
            flags.FLAGS(["test_metrics.py", "--metric=test_gen"])
        test_case = {
    "case_id": "case-1663",
    "repo_name": "trekhleb/learn-python",
    "file_path": "src/modules/sound_package/formats/wav.py",
    "code_snippet": "\n\ndef wav_read():\n\n    \"\"\"WAV file reading function mock\"\"\"\n\n    return 'Read from WAV file'\n",
    "line_range": [
        2,
        6
    ],
    "command_specific_fields": {
        "method_name": "wav_read"
    },
    "language": "python",
    "commit": "52c3a655cc2efd5ac01004f6f529c3262812a84e",
    "prompt": ""
}
        model_input = create_model_input(test_case, self.base_path)

        self.assertNotEqual(model_input.splitlines()[1], "</prompt>") # checks that prompt is not empty
        self.assertNotEqual(model_input.splitlines()[-2], "<code>") # checks that code is not empty
        
        self.assertEqual(model_input.splitlines()[1], f"Write a unit test for the function {test_case['command_specific_fields']['method_name']} in the file {test_case['file_path']}. Only provide the unit test, with no excess text.") #checks that prompt is correct
    
    
if __name__ == '__main__':
    unittest.main() 
    # Usage for running a single test:
    # python -m unittest test_metrics.TestMetricsScoring.(test name e.g. test_fix_python)