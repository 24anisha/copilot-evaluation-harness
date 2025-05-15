import textwrap
import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from score_scripts import fix_score, doc_score

from score_scripts.syntax_parser import SyntaxParser

def normalize_docstring(docstring: str, target_indent: int = 12) -> str:
    """
    Normalize a docstring to have a consistent target indentation.
    Args:
        docstring (str): Raw docstring block.
        target_indent (int): Number of spaces to indent each line.
    Returns:
        str: Re-indented, normalized docstring.
    """
    if not docstring:
        return ""

    lines = docstring.strip().splitlines()

    # Remove common leading whitespace
    stripped_lines = textwrap.dedent("\n".join(lines)).splitlines()

    indent = " " * target_indent
    return "\n".join(f"{indent}{line.lstrip()}" for line in stripped_lines)


class TestHelperScoring(unittest.TestCase):
    def setUp(self):
        # Common test data setup
        self.base_path = "out/repos/test_repo"  # Adjust path as needed

    def test_fix_find_replace(self):
        input_code = """class HTTPieHTTPSAdapter(HTTPAdapter):
        def __init__(
            self,
            verify: bool,
            ssl_version: str = None,
            ciphers: str = None,
            **kwargs
        ):
            self._ssl_context = self._create_ssl_context(
                verify=verify,
                ssl_version=ssl_version,
                ciphers=ciphers,
            )
            super().__init__(**kwargs)"""
        model_response = textwrap.dedent("""\
            ---FIND
            ```python
            ciphers: str = None,
            ```
            ---REPLACE
            ```python
            ciphers: str | None = None,
            ```
            ---COMPLETE
        """)
        expected_fixed_code = """class HTTPieHTTPSAdapter(HTTPAdapter):
        def __init__(
            self,
            verify: bool,
            ssl_version: str = None,
            ciphers: str | None = None,
            **kwargs
        ):
            self._ssl_context = self._create_ssl_context(
                verify=verify,
                ssl_version=ssl_version,
                ciphers=ciphers,
            )
            super().__init__(**kwargs)
        """
        output_fixed_code = fix_score.find_replace(input_code, "python", model_response)
        self.assertEqual(expected_fixed_code.strip(), output_fixed_code.strip())

    def test_doc_get_docstring(self):
        after_doc_file_1 = """
            /**
            * Creates a greeting message.
            *
            * @param {string} name - The name of the person to greet.
            * @returns {string} A personalized greeting.
            */
            function greet(name) {
                return `Hello, ${name}!`;
            }
        """
        after_doc_file_2 = """
            function greet(name) {
                /**
                * Creates a greeting message.
                *
                * @param {string} name - The name of the person to greet.
                * @returns {string} A personalized greeting.
                */
                return `Hello, ${name}!`;
            }
        """
        syntax_parser = SyntaxParser()
        parser = syntax_parser.get_treesitter_parser(language="javascript")
        for doc_file in [after_doc_file_1, after_doc_file_2]:
            after_tree = parser.parse(bytes(doc_file, "utf-8"))
            after_doc_nodes = [node for node in list(doc_score.traverse_tree(after_tree))]
            after_fn_node = doc_score.get_first_fn_with_name(after_doc_nodes, "greet", "javascript")
            expected_docstring = """/**
            * Creates a greeting message.
            *
            * @param {string} name - The name of the person to greet.
            * @returns {string} A personalized greeting.
            */"""
            output_docstring = doc_score.get_docstring(after_doc_nodes, after_fn_node, "javascript")
            self.assertEqual(normalize_docstring(expected_docstring), normalize_docstring(output_docstring.strip()))

if __name__ == '__main__':
    unittest.main() 
    # Usage for running a single test:
    # python -m unittest tests.test_helper_functions.TestHelperScoring.(test name e.g. test_doc_get_docstring)