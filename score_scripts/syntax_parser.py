# Copyright (c) Microsoft. All rights reserved.
"""Source parsing utilities for score scripts"""
import pandas as pd
from pathlib import Path
from typing import List
from tree_sitter import Language, Parser
from source_parser.parsers.language_parser import has_correct_syntax


class SyntaxParser:
    """Utility class for parsing source code syntax using tree-sitter"""
    supported_languages = [
            "typescript",
            "python",
            "java",
            "csharp",
            "javascript",
            "cpp",
        ]

    def __init__(self):
        self.parsers = {}
        self.supported_languages = [
            "typescript",
            "python",
            "java",
            "csharp",
            "javascript",
            "cpp",
        ]

    def get_treesitter_parser(self, language: str) -> Parser:
        """Retrieve the treesitter parser for this language"""

        if language in self.parsers:
            return self.parsers[language]
        assert language in self.supported_languages, f"Requested treesitter parser is not among supported languages {self.supported_languages}"

        tree_sitter_lang = Language(
            str(Path(__file__).parent.resolve() / "languages.so"),
            "c_sharp" if language == "csharp" else language,
        )

        parser = Parser()
        parser.set_language(tree_sitter_lang)
        self.parsers[language] = parser
        return parser

    def file_contents_syntax_check(self, file_contents: str, language: str) -> bool:
        """Process a code snippet to see whether it has correct syntax or not

        Args:
            file_contents (str): The string to check for syntax
            language (str): the programming language the string is written in

        Returns:
            bool: True if no errors in the parsed tree, otherwise False
        """

        if not isinstance(file_contents, str):
            return False

        parser = self.get_treesitter_parser(language)
        tree = parser.parse(bytes(file_contents, "utf-8"))
        syntax_pass = has_correct_syntax(tree.root_node)
        return syntax_pass

    def check_syntax_by_file(self, file_paths: List[Path], language: str):
        """Check the syntax of each file path and return in a dict"""
        syntax_results = {}
        for path in file_paths:
            if path.exists():
                syntax_results[str(path)] = self.file_contents_syntax_check(path.read_text(), language)
        return syntax_results

    def calculate_syntax_pass_rate(self, syntax_pass_info: pd.Series) -> float:
        """Calculate the syntactic pass rate for a given set of responses

        Args:
            syntax_pass_info (Series): dictionary of syntax pass rate per file path

        Returns:
            float: the mean syntax pass rate
        """

        results = syntax_pass_info[syntax_pass_info.apply(lambda x: x is not None and len(x) > 0)]
        numerator = results.apply(lambda x: sum(x.values())).sum()
        denominator = results.apply(len).sum()
        return numerator / denominator if denominator > 0 else 0
