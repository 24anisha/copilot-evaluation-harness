# Copyright (c) Microsoft. All rights reserved.
"""Abstraction for state.json file"""

from pathlib import Path
from typing import Optional

def get_language_id(state: dict) -> Optional[str]:
    """Retrieve the language id (e.g., typescript, javascript, python) from the state file"""
    return state.get("activeTextEditor", {}).get("languageId")

def get_document_file_path(state: dict, default: str=None) -> Optional[Path]:
    """Retrieve the file path from the state file"""
    filename = state.get("activeTextEditor", {}).get("documentFilePath", {})
    if filename:
        return Path(filename)
    return default

def get_workspace_folder(state: dict) -> list:
    """Retrieve the workspace folders from the state file"""
    return state.get("workspaceFoldersFilePaths", [None])[0]

def get_original_repo_name(state: dict) -> Optional[str]:
    """Retrieve the original repo name from the state file"""
    workspace_folder = get_workspace_folder(state)
    original_repo_name = (
        Path(workspace_folder).parts[-1].split("__")[-1]
        if workspace_folder is not None
        else None
    )
    return original_repo_name

def get_terminal_output(state: dict) -> Optional[str]:
    """Retrieve the terminal output from the state file"""
    return state.get("terminalOutput")

def get_active_line(state: dict) -> Optional[int]:
    """Retrieve the active line from the state file"""
    return state["activeTextEditor"]["selections"][0]["active"]["line"]

def get_anchor_line(state: dict) -> Optional[int]:
    """Retrieve the anchor line from the state file"""
    return state["activeTextEditor"]["selections"][0]["anchor"]["line"]
