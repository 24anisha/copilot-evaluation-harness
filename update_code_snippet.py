import os
import json
from plum.environments import Repository
from plum.utils import helpers
from pathlib import Path


REPOS_DIR = os.path.join("out", "repos")
invalid = []
fix_path = "data/test_gen"
for file_name in os.listdir(fix_path):
    try:
        with open(f"{fix_path}/{file_name}", "r") as file:
            test_case = json.load(file)
    except FileNotFoundError:
        invalid.append(file_name)
        continue

    base_path=os.path.join(REPOS_DIR, test_case["repo_name"])
    language = test_case["language"]
    repo_name = test_case["repo_name"]

    repo = Repository(language, base_path, repo_name, commit_sha = test_case["commit"])
    try:
        repo.setup(install_reqs=False)
    except FileNotFoundError:
        invalid.append(file_name)
        continue
    repo_folder = Path(base_path) / repo_name.replace('/', '--')

    file_path = os.path.join(repo_folder, test_case["file_path"])
    start_line, end_line = test_case["line_range"]
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            extracted_lines = lines[start_line - 1:end_line]
            result = '\n'.join(extracted_lines)
    except:
        invalid.append(file_name)
        continue

    test_case["code_snippet"] = result

    with open(f"{fix_path}/{file_name}", "w") as file:
        json.dump(test_case, file, indent=4)

print(invalid)