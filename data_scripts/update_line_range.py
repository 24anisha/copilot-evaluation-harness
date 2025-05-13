import os
import json
from plum.environments import Repository
from plum.utils import helpers
from pathlib import Path


REPOS_DIR = os.path.join(".", "out", "repos")
invalid = []
invalid_commit = 0
good = []
good_commit = 0
case_path = "test_gen_java_new"
for file_name in os.listdir(case_path):
    try:
        with open(f"{case_path}/{file_name}", "r") as file:
            test_case = json.load(file)
    except FileNotFoundError:
        invalid.append(file_name)
        invalid_commit += 1
        continue

    base_path=os.path.join(REPOS_DIR, test_case["repo_name"])
    language = test_case["language"]
    repo_name = test_case["repo_name"]

    repo = Repository(language, base_path, repo_name, commit_sha = test_case["commit"])
    try:
        repo.setup(install_reqs=False)
    except FileNotFoundError:
        invalid.append(file_name)
        invalid_commit += 1
        continue
    repo_folder = Path(base_path) / repo_name.replace('/', '--')

    file_path = os.path.join(repo_folder, test_case["file_path"])
    start_line, end_line = test_case["line_range"]
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            extracted_lines = lines[start_line:end_line +1]
            result = ''.join(extracted_lines)
    except:
        invalid.append(file_name)
        invalid_commit += 1
        continue

    test_case["new_code_snippet"] = result

    with open(f"{case_path}/{file_name}", "w") as file:
        json.dump(test_case, file, indent=4)
    
    good.append(file_name)
    good_commit += 1

print(invalid)
print(invalid_commit)
print(good)
print(good_commit)