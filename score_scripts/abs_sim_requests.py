"""Abstraction for sim_requests.txt file"""

import json
import re
from pathlib import Path
from typing import List

def find_retrieved(simulator_output_folder: Path, outcome: dict) -> List[str]:
    """Find retrieved messages from request messages."""

    srp = outcome.get("sim_requests_path")
    if not srp:
        return [""]
    sim_requests_path = Path(srp)
    sim_requests = json.loads((simulator_output_folder / sim_requests_path).read_text())
    request_messages = sim_requests[0]["requestMessages"]

    if len(request_messages) < 3:
        return [""]
    context = request_messages[1]["content"]
    if "relevant code samples" not in context:
        return [""]
    retrieved = context.split("relevant code samples")[1].strip().split("File:")
    return [retrieve.strip() for retrieve in retrieved if retrieve.strip()]

def find_sim_requests_files(search_path: Path, outcome_folder: str) -> List[Path]:
    """Retrieve the sim_requests.txt file from the simulator output folder"""
    return sorted(
        list(
            search_path.rglob(f"{outcome_folder}/sim-requests-*.txt")
        ),
        key=lambda x: x.name,
    )

def find_sim_requests_files_with_case_number(search_path: Path, case_number: int) -> List[Path]:
    """Retrieve the sim_requests.txt file paths from the search path"""
    candidate_sim_requests = list(search_path.rglob("*sim-requests*.txt"))
    sim_requests = []
    rex = re.compile(r"case[^\d]*(\d+).*sim-requests.*[.]txt")
    for candidate in candidate_sim_requests:
        match = rex.search(candidate.name)
        if match and case_number == int(match.group(1)):
            sim_requests.append(Path(candidate))
    if not sim_requests:
        print(f"""
No sim_requests.txt file found for case number {case_number}
    candidate_sim_requests: {list(candidate_sim_requests)}
    print(f"sim_requests: {sim_requests}
        """)
    return sim_requests
