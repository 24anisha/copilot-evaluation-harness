# Copyright (c) Microsoft. All rights reserved.
"""Abstraction for conversation.json file"""

import re
from pathlib import Path
from typing import List, Optional
from os_helper import run_script

def get_language(conversation: dict) -> Optional[str]:
    """Retrieve the language id (e.g., typescript, javascript, python) from the conversation if available otherwise state file"""
    if conversation and isinstance(conversation, list) and conversation[0] and isinstance(conversation[0], dict):
        return conversation[0].get("language")
    return None

def get_keywords(conversation: dict) -> List[str]:
    """Retrieve the keywords from the conversation"""
    if conversation and isinstance(conversation, list) and conversation[0] and isinstance(conversation[0], dict):
        return [kw.lower() for kw in conversation[0].get("keywords", [])]
    return []

def get_method_original_string(conversation: dict) -> str:
    """Retrieve the original method from the conversation"""
    if conversation and isinstance(conversation, list) and conversation[0] and isinstance(conversation[0], dict):
        return conversation[0].get("method_original_string", "")
    return ""

def get_task(conversation: dict) -> str:
    """Retrieve the task from the conversation"""
    if conversation and isinstance(conversation, list) and conversation[0] and isinstance(conversation[0], dict):
        return conversation[0].get("task", "")
    return ""

def find_conversation_file_paths(search_path: Path) -> List[Path]:
    """Retrieve the conversation file paths from the search path"""
    return set(search_path.rglob("*.conversation.json"))

def find_conversation_file_paths_with_case_number(search_path: Path, case_number: int) -> List[Path]:
    """Retrieve the conversation file paths that contain the given case number from the search path"""
    # tests/doc/case-6253/case-6253.conversation.json/1/...
    # tests/doc/case-53/case-53.conversation.json/1/...
    rex = re.compile(rf".*[^\d]+{case_number}[^\d]+")
    case_folder_paths0 = [p.iterdir() for p in search_path.rglob(f"*{case_number}*conversation*") if p.is_dir()]
    case_folder_paths1 = [p for sublist in case_folder_paths0 for p in sublist]
    case_folder_paths2 = [p for p in case_folder_paths1 if rex.match(str(p))]
    case_folder_paths = sorted(case_folder_paths2, key=lambda p: int(p.name))
    if not case_folder_paths:
        print(f"No conversation file paths found for case number {case_number} under {search_path}. Did the schema change?")
        print(f"    case_folder_paths0: {case_folder_paths0}")
        print(f"    case_folder_paths1: {case_folder_paths1}")
        print(f"    case_folder_paths2: {case_folder_paths2}")
        run_script("find_conversation_file_paths_with_case_number.sh", f"find {search_path} -name SimulationResult.yml", throw_on_error=False)
    return case_folder_paths

def get_case_number_from_conversation_file_path(conversation_file_path: Path) -> Optional[int]:
    """Retrieve the case number from the conversation file path"""
    case_search = re.search(r"(\d+).conversation.json", conversation_file_path.name)
    case_number = int(case_search.group(1)) if case_search else None
    return case_number

def get_test_case_name_from_conversation_filename(conversation_filename: str) -> str:
    """Retrieve the test case name from the conversation file name"""
    test_case_name_from_conversation = conversation_filename.replace(".conversation.json", "")
    return test_case_name_from_conversation

def get_state_file(conversation: dict) -> Optional[str]:
    """Retrieve the state file from the conversation"""
    if conversation and isinstance(conversation, list) and conversation[0] and isinstance(conversation[0], dict):
        return conversation[0].get("stateFile", "")
    return ""
