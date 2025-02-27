from plum.environments import Repository
from plum.actions import Actions

import re
import json

from tree_sitter import Tree, Node
from pathlib import Path
from collections import Counter
from typing import Optional, Tuple, Dict, Any, List
from contextlib import contextmanager
from .static_analysis_tools import (
    ToolResult,
    get_supported_tools,
    get_tool_run_fn,
)
from .syntax_parser import SyntaxParser

def _get_post_files_by_suffix(working_dir_path: Path, post_file_path: Path) -> List[Path]:
    """Retrieve the post files from the working directory"""
    return list(working_dir_path.glob(f"*{post_file_path.suffix}"))

def get_first_post_file(working_dir_path: Path, post_file_path: Path) -> Optional[Path]:
    """Retrieve the first post file from the working directory"""
    post_files = _get_post_files_by_suffix(working_dir_path, post_file_path)
    return post_files[0] if post_files else None

def flat(l):
    """
    Flatten a list of lists.
    """
    return [item for sublist in l for item in sublist]

def traverse_tree(tree: Tree, ignore_node_types: List[str] = None) -> List[Node]:
    """
    Traverse a TreeSitter tree in a depth-first manner to yield all nodes.
    """
    cursor = tree.walk()

    reached_root = False
    while reached_root is False:
        yield cursor.node

        if ignore_node_types is None or cursor.node.type not in ignore_node_types:
            if cursor.goto_first_child():
                continue

        if cursor.goto_next_sibling():
            continue

        retracing = True
        while retracing:
            if not cursor.goto_parent():
                retracing = False
                reached_root = True

            if cursor.goto_next_sibling():
                retracing = False


def is_fn_node(node: Node, language: str) -> bool:
    """Check if a node is a function node according to the language (e.g., typescript, python)"""

    if language in ["javascript", "typescript"]:
        return node.type in ["function_declaration", "method_definition"]
    if language == "python":
        return node.type == "function_definition"
    if language == "java":
        return node.type == "method_declaration"
    if language == "csharp":
        return node.type in [
            "method_declaration",
            "constructor_declaration",
        ]
    if language == "cpp":
        return node.type == "function_definition"

    raise NotImplementedError


def is_comment_node(node: Node, language: str) -> bool:
    """Check if a node is a comment node according to the language"""

    if language in ["javascript", "typescript"]:
        return node.type == "comment"
    if language == "python":
        return node.type == "comment"
    if language == "java":
        return node.type in ["comment", "block_comment"]
    if language == "csharp":
        return node.type == "comment"
    if language == "cpp":
        return node.type in ["comment", "block_comment"]
    raise NotImplementedError


def is_identifier_node(node: Node, language: str) -> bool:
    """Check if a node is an identifier node according to the language (e.g., typescript, python)"""

    if language in ["javascript", "typescript"]:
        return "identifier" in node.type or node.type == "this"
    if language == "python":
        return "identifier" in node.type
    if language == "java":
        return node.type == "identifier"
    if language == "csharp":
        return node.type == "identifier"
    if language == "cpp":
        return node.type == "identifier"
    raise NotImplementedError


def get_first_identifier_node_text(node: Node, language: str, return_node=False) -> Optional[str]:
    """Obtain the first identifier node child in the walked tree of the given node.

    Traverse the tree and find the first identifier node.
    Ignore marker annotations (for java) and decorators (for python)"""

    id_node = next(
        (node for node in traverse_tree(node, ["marker_annotation", "decorator"]) if is_identifier_node(node, language) or node.type in ["predefined_type", "variable_declarator"]),
        None,
    )

    return id_node if return_node else id_node.text.decode("utf-8")


def get_first_fn(nodes: List[Node], language: str) -> Optional[Node]:
    """Obtain the first function node in the given list of nodes."""
    first_fn_node = next((node for node in nodes if is_fn_node(node, language)), None)
    return first_fn_node


def get_first_fn_with_name(nodes: List[Node], fn_name: str, language: str) -> Optional[Node]:
    """Obtain the first function node with the given name in the given list of nodes.

    Args:
        nodes: List of nodes to search for the function node.
        fn_name: Name of the function to search for.
        language: Language of the nodes (e.g., typescript, python).

    Returns:
        The first function node with the given name in the given list of nodes.
    """
    return next(
        (node for node in nodes if is_fn_node(node, language) and get_first_identifier_node_text(node, language) == fn_name),
        None,
    )


def get_fn_arg_names(fn_node: Node, language: str) -> List[str]:
    """Obtain the argument names of the given function node.

    Args:
        fn_node: Function node to obtain the argument names from.
        language: Language of the function node (e.g., typescript, python).

    Returns:
        The argument names of the given function node.
    """

    if language in ["javascript", "typescript"]:
        formal_params = next(node for node in fn_node.children if node.type == "formal_parameters")
        arg_nodes = [node for node in formal_params.children if node.type in ["required_parameter", "optional_parameter", "identifier"]]
        arg_names = [get_first_identifier_node_text(arg_node, language) for arg_node in arg_nodes]
        return [arg_name.replace("...", "") for arg_name in arg_names if arg_name != "this"]
    if language == "python":
        parameters = next(node for node in fn_node.children if node.type == "parameters")
        parameter_tree = [x[1] for x in walk_tree_with_ignore(parameters, ["type"], returns="node")]
        return [node.text.decode("utf-8") for node in parameter_tree if is_identifier_node(node, language)]
    if language == "java":
        formal_params = next(node for node in fn_node.children if node.type == "formal_parameters")
        arg_nodes = [node for node in traverse_tree(formal_params) if is_identifier_node(node, language)]
        return [node.text.decode("utf-8") for node in arg_nodes]
    if language == "csharp":
        param_list = next(node for node in fn_node.children if node.type == "parameter_list")
        parameters = [node for node in param_list.children if node.type == "parameter"]
        result = [parameter.children[1].text.decode("utf-8") for parameter in parameters if is_identifier_node(parameter.children[1], language)]
        return result
    if language == "cpp":
        param_list = next(
            (node for node in traverse_tree(fn_node) if node.type == "parameter_list"),
            None,
        )
        param_decls = [decl for decl in param_list.children if decl.type == "parameter_declaration"]
        arg_nodes = flat([node for node in traverse_tree(param_decl) if is_identifier_node(node, language)] for param_decl in param_decls)
        return [node.text.decode("utf-8") for node in arg_nodes]
    raise NotImplementedError


def get_docstring(nodes: List[Node], fn_node: Node, language: str) -> Optional[str]:
    """Obtain the docstring of the given function node.

    In typescript, the docstring appears as a comment before the function so we search backwards for the first comment node.
    In python, the docstring can appear above or below the function so we search both ways for the first string node.

    Args:
        nodes: List of nodes surrounding the fn_node.
        fn_node: Function node to obtain the docstring from.
        language: Language of the function node (e.g., typescript, python).

    Returns:
        The docstring of the given function node.
    """
    if language in ["javascript", "typescript"]:
        fn_index = nodes.index(fn_node)
        nodes_before_fn = reversed(nodes[:fn_index])
        docstring = next((node for node in nodes_before_fn if is_comment_node(node, language)), None)
        if docstring:
            return docstring.text.decode("utf-8") 
        first_string_node = next((node for node in list(traverse_tree(fn_node)) if is_comment_node(node, language)), None)
        return first_string_node.text.decode("utf-8") if first_string_node else None
    if language == "python":
        # doc could be before the function
        first_string_node = next((node for node in list(traverse_tree(fn_node)) if node.type == "string"), None)
        return first_string_node.text.decode("utf-8") if first_string_node else None
    if language == "java":
        fn_index = nodes.index(fn_node)
        nodes_before_fn = reversed(nodes[:fn_index])
        docstring = next((node for node in nodes_before_fn if is_comment_node(node, language)), None)
        return docstring.text.decode("utf-8") if docstring else None
    if language == "csharp":
        # Comments are separated by newlines, so we search backwards for comment nodes from fn_node until we find a non-comment node
        fn_index = nodes.index(fn_node)
        nodes_before_fn = list(reversed(nodes[:fn_index]))
        i = 0
        while i < len(nodes_before_fn) and is_comment_node(nodes_before_fn[i], language):
            i += 1
        docstring_nodes = nodes_before_fn[:i]
        docstring = "\n".join([node.text.decode("utf-8") for node in docstring_nodes])
        return docstring
    if language == "cpp":
        fn_index = nodes.index(fn_node)
        nodes_before_fn = reversed(nodes[:fn_index])
        docstring = next((node for node in nodes_before_fn if is_comment_node(node, language)), None)
        return docstring.text.decode("utf-8") if docstring else None
    raise NotImplementedError


# pylint: disable=too-many-return-statements
def get_return_type(fn_node: Node, language: str) -> Optional[Node]:
    """Obtain the return type of the given function node.

    In typescript, we can check the type annotation of the function return value.
    In python, we can check the type annotation of the function return value by searching for the arrow node.

    Args:
        fn_node: Function node to obtain the return type from.
        language: Language of the function node (e.g., typescript, python).

    Returns:
        The return type of the given function node.
    """
    if language in ["typescript", "javascript"]:
        return_type_annotation_idx = next(
            (i for i, node in enumerate(fn_node.children) if node.type == "type_annotation"),
            None,
        )

        if return_type_annotation_idx is not None and fn_node.children[return_type_annotation_idx - 1].type == "formal_parameters":
            return_type = fn_node.children[return_type_annotation_idx]
            if return_type is not None and return_type.text.decode("utf-8") == "void":
                return None
            return return_type
        return None
    if language == "python":
        return_type_annotation_idx = next(
            (i for i, node in enumerate(fn_node.children) if node.type == "type"),
            None,
        )

        if return_type_annotation_idx is not None and fn_node.children[return_type_annotation_idx - 1].type == "->":
            return_type = fn_node.children[return_type_annotation_idx]
            if return_type is not None and return_type.text.decode("utf-8") == "None":
                return None
            return return_type
        return None
    if language == "java":
        return_type_node = next(
            (node for i, node in enumerate(fn_node.children) if "type" in node.type and i + 1 < len(fn_node.children) and is_identifier_node(fn_node.children[i + 1], language)),
            None,
        )

        if return_type_node is not None:
            if return_type_node.text.decode("utf-8") == "void":
                return None
            return return_type_node
        return None
    if language == "csharp":
        if fn_node.type == "constructor_declaration":
            return None
        return_type_node = next(
            (
                node
                for i, node in enumerate(fn_node.children)
                if is_identifier_node(node, language) or node.type in ["predefined_type", "generic_name"] and is_identifier_node(fn_node.children[i + 1], language)
            ),
            None,
        )

        if return_type_node is not None:
            if return_type_node.text.decode("utf-8") == "void":
                return None
            if return_type_node.type != "identifier":
                return_type_node = get_first_identifier_node_text(return_type_node, language, return_node=True)
            return return_type_node
        return None
    if language == "cpp":
        return_type_node = next(
            (node for i, node in enumerate(fn_node.children) if "type" in node.type and i + 1 < len(fn_node.children) and is_identifier_node(fn_node.children[i + 1], language)),
            None,
        )

        if return_type_node is not None:
            if return_type_node.text.decode("utf-8") == "void":
                return None
            return return_type_node
        return None

    raise NotImplementedError
# pylint: enable=too-many-return-statements


# pylint: disable=dangerous-default-value
def walk_tree_with_ignore(node: Node, ignore_node_types: List[str] = [], returns="text") -> List[Tuple[str, Node]]:
    """Perform a depth-first traversal of the given tree, ignoring nodes of the given types. Only return child nodes.

    Args:
        node: Node to start the traversal from.
        ignore_node_types: List of node types to ignore.
        returns: Whether to return the text of the node or the node itself.

    Returns:
        A list of tuples of the node type and the node text or node itself.
    """
    cursor = node.walk()
    queue = [cursor.node]
    result = []
    while queue:
        node = queue.pop()
        if node.children:
            if node.type not in ignore_node_types:
                for ch in node.children:
                    queue.append((ch))
        else:
            result.append((node.type, node.text.decode("utf-8") if returns == "text" else node))
    return result
# pylint: enable=dangerous-default-value


def get_counter_diff(a: Counter, b: Counter) -> Counter:
    """Returns the XOR difference between two counters"""
    diff = (a - b) + (b - a)
    return diff


def get_fn_node_diff(before_fn_node: Node, after_fn_node: Node) -> Counter:
    """Returns the difference between the children of two function nodes"""
    before_children = Counter(n.type for n in traverse_tree(before_fn_node))
    after_children = Counter(n.type for n in traverse_tree(after_fn_node))
    return get_counter_diff(before_children, after_children)


def has_error(nodes: List[Node]) -> bool:
    """Check if the given list of nodes contains an error node."""
    return any(node.type == "ERROR" for node in nodes)


def check_if_params_documented(docstring: str, arg_names: List[str], language: str) -> bool:
    """Check if the given docstring contains documentation for all the given parameters.

    In typescript, ensure that the arg name exists in a line with the @param tag.
    In python, simply check if the arg name exists in the docstring because there are multiple Python docstring formats

    Args:
        docstring: Docstring to check.
        arg_names: List of argument names to check.
        language: Language of the function node (e.g., typescript, python).

    Returns:
        True if the docstring contains documentation for all the given parameters, False otherwise.
    """
    if language in ["javascript", "typescript", "java", "cpp"]:
        docstring_lines = docstring.splitlines()
        param_lines = [line for line in docstring_lines if "@param" in line]
        if len(param_lines) != len(arg_names):
            return False
        is_params_documented = all(any(arg_name in line for line in param_lines) for arg_name in arg_names)
        return is_params_documented
    if language == "python":
        params_documented = all(arg_name in docstring for arg_name in arg_names if arg_name not in ["self", "args", "kwargs"])
        return params_documented
    if language == "csharp":
        docstring_lines = docstring.splitlines()
        param_lines = [line for line in docstring_lines if "<param" in line]
        is_params_documented = all(any(arg_name in line for line in param_lines) for arg_name in arg_names)
        has_summary = "<summary>" in docstring
        return is_params_documented and has_summary
    raise NotImplementedError


def check_if_return_type_documented(docstring: str, return_type: Node, language: str) -> bool:
    """Check if the given docstring contains documentation for the return type.

    In typescript, ensure that the return type exists in a line with the @return tag.
    In python, check if any of the common returns keywords exist in the docstring.

    Args:
        docstring: Docstring to check.
        return_type: Return type to check.
        language: Language of the function node (e.g., typescript, python).

    Returns:
        True if the docstring contains documentation for the return type, False otherwise.
    """
    if language in ["javascript", "typescript"]:
        docstring_lines = docstring.splitlines()
        is_return_documented_if_applicable = return_type is None or any("@return" in line for line in docstring_lines)
        return is_return_documented_if_applicable
    if language == "python":
        return return_type is None or any(keyword in docstring for keyword in ["Returns", "Yields", ":return"])
    if language == "java":
        docstring_lines = docstring.splitlines()
        is_return_documented_if_applicable = return_type is None or any("@return" in line for line in docstring_lines)
        return is_return_documented_if_applicable
    if language == "csharp":
        docstring_lines = docstring.splitlines()
        is_return_documented_if_applicable = return_type is None or any("<returns>" in line for line in docstring_lines)
        return is_return_documented_if_applicable
    if language == "cpp":
        docstring_lines = docstring.splitlines()
        is_return_documented_if_applicable = return_type is None or any("@return" in line or "returns" in line.lower() for line in docstring_lines)
        return is_return_documented_if_applicable
    raise NotImplementedError


def check_if_fn_structure_is_preserved(before_fn_node: Node, after_fn_node: Node) -> bool:
    """Check if the structure of the function is preserved after the docstring is added.

    This is done by comparing the children of the function nodes before and after the docstring is added, while ignoring strings and comments
    If the children are the same, then the structure is preserved.

    Args:
        before_fn_node: Function node before the docstring is added.
        after_fn_node: Function node after the docstring is added.

    Returns:
        True if the structure of the function is preserved, False otherwise.
    """
    before_counts = Counter(walk_tree_with_ignore(before_fn_node, ["comment", "string", "block_comment"]))
    after_counts = Counter(walk_tree_with_ignore(after_fn_node, ["comment", "string", "block_comment"]))
    before_after_diff = get_counter_diff(before_counts, after_counts)
    return all(k[0] in ["comment", "string", "block_comment"] for k in before_after_diff.keys())

# pylint: disable=too-many-return-statements
def evaluate_documented_fn(
    before_doc_file: str,
    after_doc_file: str,
    start_line: int,
    language: str,
) -> Tuple[bool, str]:
    """
    Evaluates whether the after_doc_fn is a valid documentation of the before_doc_fn.

    Args:
        before_doc_file (str): The contents of the file before the docstring was added
        after_doc_file (str): The contents of the file after the docstring was added
        start_line (int): The line number of the function to evaluate
        language (str): given language
    """
    syntax_parser = SyntaxParser()
    parser = syntax_parser.get_treesitter_parser(language=language)
    before_tree = parser.parse(bytes(before_doc_file, "utf-8"))
    after_tree = parser.parse(bytes(after_doc_file, "utf-8"))
    before_doc_nodes = [node for node in list(traverse_tree(before_tree)) if node.start_point[0] >= start_line]
    after_doc_nodes = [node for node in list(traverse_tree(after_tree))]

    before_fn_node = get_first_fn(before_doc_nodes, language)
    fn_name = get_first_identifier_node_text(before_fn_node, language)
    after_fn_node = get_first_fn_with_name(after_doc_nodes, fn_name, language)
    extra_data = {"fn_name": fn_name}

    if before_fn_node is None or after_fn_node is None:
        if has_error(after_doc_nodes):
            return False, "Error in code", extra_data
        return False, "Function name was changed", extra_data

    arg_names = get_fn_arg_names(before_fn_node, language)
    docstring = get_docstring(after_doc_nodes, after_fn_node, language)
    return_type = get_return_type(before_fn_node, language)

    failure_reasons = []

    is_args_preserved = arg_names == get_fn_arg_names(after_fn_node, language)
    if not is_args_preserved:
        failure_reasons.append("Args were changed")

    is_fn_structure_preserved = check_if_fn_structure_is_preserved(before_fn_node, after_fn_node)
    if not is_fn_structure_preserved:
        failure_reasons.append("Function structure was changed")

    is_docstring_added = docstring is not None
    if not is_docstring_added:
        failure_reasons.append("Docstring was not added")

    is_params_documented = is_docstring_added and check_if_params_documented(docstring, arg_names, language)
    if not is_params_documented:
        failure_reasons.append("Params were not documented")

    is_return_documented_if_applicable = is_docstring_added and check_if_return_type_documented(docstring, return_type, language)
    if not is_return_documented_if_applicable:
        failure_reasons.append("Return type was not documented")

    syntax_correct = syntax_parser.file_contents_syntax_check(after_doc_file, language)
    if not syntax_correct:
        failure_reasons.append("Syntax error in code")

    extra_data["arg_names"] = arg_names
    extra_data["return_type"] = return_type.text.decode("utf-8") if return_type is not None else None
    extra_data["docstring"] = docstring

    if len(failure_reasons) > 0:
        return False, ",".join(failure_reasons), extra_data
    return True, "Success", extra_data

# pylint: disable=too-many-arguments
def evaluate_test_case(
    start_line: int,
    language: str,
    document_abs_path: Path,
    model_output: str,
) -> dict:
    """Score the responses for docstring quality."""

    if not model_output:
        return {
            "metric": "doc",
            "success": False,
            "score": -1,
            "language": language,
            "reason": "Missing model output",
            "original_file_syntax_pass": None,
            "post_file_syntax_pass": None,
            "extra_data_json": json.dumps({})
        }

    syntax_parser = SyntaxParser()

    output_source_file_contents = model_output
    input_source_file_path = document_abs_path
    if not input_source_file_path:
        raise ValueError(
            f"Could not find input source file for {input_source_file_path.name}"
        )
    input_source_file_contents = Path(input_source_file_path).read_text()

    if language not in syntax_parser.supported_languages:
        score, reason, extra_data = -1, "Language not supported", {}
    else:
        score, reason, extra_data = evaluate_documented_fn(
            input_source_file_contents,
            output_source_file_contents,
            start_line,
            language,
        )

    return {
            "metric": "doc",
            "success": score,
            "score": score,
            "language": language,
            "reason": reason,
            "original_file_syntax_pass": syntax_parser.check_syntax_by_file([Path(document_abs_path)], language),
            "post_file_syntax_pass": syntax_parser.file_contents_syntax_check(model_output, language),
            "extra_data_json": 
                json.dumps(
                    {
                        "arg_names": extra_data.get("arg_names", []),
                        "return_type": extra_data.get("return_type", None),
                        "docstring": extra_data.get("docstring", None),
                    }
                ),
        }
    

def score_doc(base_path, start_line: int, language: str, relative_file_path, model_output: str) -> dict:

    return evaluate_test_case(
        start_line=start_line,
        language=language,
        document_abs_path = base_path + "/data/doc/" + relative_file_path,
        model_output= model_output
    )


if __name__ == "__main__":
    # Example usage
    base_path = Path("/path/to/repository")
    relative_file_path = Path("test_file")
    language = "python"
    model_output = "model response"
    
    result = score_doc(base_path, relative_file_path=relative_file_path, language=language, model_output=model_output)
    print(result)
