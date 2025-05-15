import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from end_to_end_script import create_model_input
from absl import flags

class TestModelInputs(unittest.TestCase):
    def setUp(self):
        # Common test data setup
        self.base_path = "out/repos/test_repo"  # Adjust path as needed

    def test_model_input_fix(self):
        # no optional prompt passed
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
    # python -m unittest tests.model_input_tests.TestModelInputs.(test name e.g. test_model_input_fix)