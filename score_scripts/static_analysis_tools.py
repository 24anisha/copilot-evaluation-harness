# Copyright (c) Microsoft. All rights reserved.
""" Build test cases for a tool based on a list of repos """

import json
import os
import subprocess
import re
import random
import shutil
import traceback
import xml.etree.ElementTree as ET
from plum.environments.repository import Repository
from plum.actions.java_mvn_actions import JavaMavenActions
from dataclasses import dataclass
from pathlib import Path
from sarif import loader
from typing import Callable, List, Tuple, Dict
from tsc_diagnostic_messages import get_tsc_diagnostic_messages
from timeout import timeout
from os_helper import run_script


@dataclass
class ToolResult:
    """Captures the result of a tool run on a file"""

    tool: str
    repo_folder: str  # name of repo folder with no other path parts
    language: str
    file_path: str  # name of file path relative to the repo folder
    severity: int
    message: str
    rule: str
    start_line_index: int  # 0-indexed
    end_line_index: int  # 0-indexed
    start_col_index: int  # 0-indexed
    end_col_index: int  # 0-indexed


eslint_config = """export default [
    {
        languageOptions: {
            parserOptions: {
                ecmaFeatures: {
                    jsx: true
                }
            }
        },
        rules: {
            "constructor-super": "error",
            "for-direction": "error",
            "getter-return": "error",
            "no-async-promise-executor": "error",
            "no-class-assign": "error",
            "no-compare-neg-zero": "error",
            "no-cond-assign": "error",
            "no-const-assign": "error",
            "no-constant-condition": "error",
            "no-control-regex": "error",
            "no-dupe-args": "error",
            "no-empty-pattern": "error",
            "no-ex-assign": "error",
            "no-invalid-regexp": "error",
            "no-new-symbol": "error",
            "no-obj-calls": "error",
            "no-prototype-builtins": "error",
            "no-self-assign": "error",
            "no-setter-return": "error",
            "no-unreachable": "error",
            "no-unreachable-loop": "error",
            "no-unsafe-finally": "error",
            "no-unsafe-negation": "error",
            "no-unsafe-optional-chaining": "error",
            "use-isnan": "error",
        },
    }
];"""

tsconfig = {
    "compilerOptions": {
        "target": "es6",
        "module": "commonjs",
        "strict": True,
        "esModuleInterop": True,
        "skipLibCheck": True,
        "forceConsistentCasingInFileNames": True,
        "moduleResolution": "node",
        "resolveJsonModule": True,
        "outDir": "./dist",
        "lib": ["es2018", "dom"],
        "sourceMap": True,
    },
    "include": ["**/*.ts"],
    "exclude": ["node_modules", "dist"],
}


def make_path_relative_to_repo(path: Path, repo_name: str) -> Path:
    """Assume that the repo_name is a unique path part of path, and get the relative path to it"""
    part_index = path.parts.index(repo_name)
    relative_parts = path.parts[part_index + 1 :]
    return Path().joinpath(*relative_parts)


def get_tools_and_language() -> Dict[str, str]:
    """Return a dictionary of tools and the language they are used for"""
    return {
        "eslint": "javascript",
        "typescript_eslint": "typescript",
        "pyright": "python",
        "pylint": "python",
        "tsc": "typescript",
        "roslyn": "csharp",
        "spotbugs": "java",
        "cppcheck": "cpp",
    }


def get_supported_tools_by_language(language: str) -> List[str]:
    """Return a list of supported static analysis tools for a language"""
    return [tool for tool, lang in get_tools_and_language().items() if lang == language]


def get_supported_tools():
    """Return a list of supported static analysis tools"""
    return list(get_tools_and_language().keys())


def get_language_for_tool(tool: str) -> str:
    """Return the language for the given tool. """
    return get_tools_and_language()[tool]


def get_tool_run_fn(tool_name: str) -> Callable[[str], List[ToolResult]]:
    """Return the function to run a tool on a repo"""
    tool_fn = {
        "eslint": lambda repo_folder: run_eslint_on_repo("javascript", repo_folder),
        "typescript_eslint": lambda repo_folder: run_eslint_on_repo("typescript", repo_folder),
        "pyright": run_pyright_on_repo,
        "pylint": run_pylint_on_repo,
        "tsc": run_tsc_on_repo,
        "roslyn": run_roslyn_on_repo,
        "spotbugs": run_spotbugs_on_repo,
        "cppcheck": run_cppcheck_on_repo,
    }
    return tool_fn[tool_name]


def get_ignored_eslint_rules():
    """Return a list of eslint rules that should be ignored"""
    return [
        "node/no-unpublished-require",
        "node/no-unsupported-features/es-syntax",
        "import/no-unresolved",
        "import/extensions",
        "import/named",
        "import/namespace",
        "import/no-extraneous/dependencies",
        "no-unresolved",
        "no-unused-vars",
        "no-undef",
    ]


def parse_sarif_result(file_path: Path, sarif_result: dict) -> Tuple[int, int, int, int]:
    """Parse a sarif result and return the file contents and location

    Args:
        file_path (Path): Path to the file
        sarif_result (dict): Sarif result to parse

    Returns:
        Tuple[int, int, int, int]: Start line, start column, end line, end column
    """

    file_contents = Path(file_path).read_text()
    start_line = sarif_result["locations"][0]["physicalLocation"]["region"]["startLine"]
    end_line = sarif_result["locations"][0]["physicalLocation"]["region"].get("endLine", start_line)
    start_column = sarif_result["locations"][0]["physicalLocation"]["region"].get("startColumn", 1)
    end_column = sarif_result["locations"][0]["physicalLocation"]["region"].get("endColumn", len(file_contents.splitlines()[end_line - 1]))
    return start_line, start_column, end_line, end_column


def is_eligible_file_for_eslint_check(file_path: Path) -> bool:
    """Check if a file is eligible (not part of a min.js or library code) for eslint check"""
    if "-min." in str(file_path) or ".min." in str(file_path) or ".spec." in str(file_path) or "node_modules" in str(file_path):
        return False

    try:
        contents = file_path.read_text()
        if any(len(line) > 500 for line in contents.splitlines()):
            return False
        return True
    except Exception as e:
        print(f"Failed to read file {file_path}: {e}")
        return False


def run_eslint_on_repo(language: str, repo_folder: Path) -> Tuple[List[ToolResult], str]:
    """Run eslint or tslint on a repo and return the results as ToolResults"""

    # If existing eslint json file exists, delete it
    existing_config_files = list(repo_folder.rglob("*eslint*"))
    for f in existing_config_files:
        if f.is_file():
            f.unlink()

    with open(repo_folder / "eslint.config.mjs", "w") as f:
        f.write(eslint_config)

    # 1. Collect eligible files (e.g. .js files)
    eligible_files = [f"{str(f.resolve())}" for f in repo_folder.rglob(f"*.{'js' if language == 'javascript' else 'ts'}") if is_eligible_file_for_eslint_check(f)]

    # 2. Lint them
    cwd = os.getcwd()
    os.chdir(repo_folder)
    subprocess_result = subprocess.run(
        ["npx", "eslint", "-f", "json", "-o", "lint_output.json", *eligible_files],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    subprocess_stdout = subprocess_result.stdout.decode('utf-8')
    os.chdir(cwd)

    # 3. Parse the output
    lint_output_path = repo_folder / "lint_output.json"
    if not lint_output_path.exists():
        print("No eslint output found")
        return [], subprocess_stdout

    lint_output = json.loads(lint_output_path.read_text())
    results = []
    for result in lint_output:
        messages = [message for message in result["messages"] if message.get("ruleId", None) is not None]
        relative_file_path = make_path_relative_to_repo(Path(result["filePath"]), repo_folder.parts[-1])
        lint_results = [
            ToolResult(
                tool="eslint" if language == "javascript" else "typescript_eslint",
                repo_folder=repo_folder.parts[-1],
                language=language,
                file_path=str(relative_file_path),
                severity=message["severity"],
                rule=message["ruleId"],
                message=message["message"],
                start_line_index=message["line"] - 1,
                end_line_index=message.get("endLine", message["line"]) - 1,
                start_col_index=message["column"] - 1,
                end_col_index=message["endColumn"] - 1,
            )
            for message in messages
        ]
        results.extend(
            [
                r
                for r in lint_results
                if r.rule not in get_ignored_eslint_rules()
                and not r.file_path.endswith("jsx")
                and not r.file_path.endswith("tsx")
                and "tsx" not in r.message
                and "jsx" not in r.message
            ]
        )
    print("Got ", len(results), "results")

    return results, subprocess_stdout

def setup_venv_on_repo(repo_folder: Path):
    """Setup a virtual environment on a repo"""
    pcmd = [
        f"if [ ! -d '{repo_folder}/.venv' ]; then python3 -m venv '{repo_folder}/.venv'; fi",
        f"source {repo_folder}/.venv/bin/activate",
    ]
    for requirements_txt in repo_folder.rglob("requirements.txt"):
        pcmd.append(f"python3 -m pip install -r '{requirements_txt}' > /dev/null")
    run_script("setup_venv_on_repo.sh", os.linesep.join(pcmd))

def clean_python_repo(repo_folder: Path) -> None:
    """Clean up a python repo from git and virtual environment info."""
    shutil.rmtree(f"{repo_folder}/.venv")
    shutil.rmtree(f"{repo_folder}/.git")
    for gitignore in repo_folder.rglob(".gitignore"):
        gitignore.unlink(missing_ok=False)

def run_pyright_on_repo(repo_folder: Path) -> Tuple[List[ToolResult], str]:
    """Run pyright on a repo and return the results as ToolResults"""
    setup_venv_on_repo(repo_folder)
    pcmd = [
        f"source {repo_folder}/.venv/bin/activate",
        f"pyright --outputjson {repo_folder}",
    ]
    # errors from pyright are expected
    pyright_cmd = run_script("run_pyright_on_repo.sh", os.linesep.join(pcmd), throw_on_error=False, return_subprocess_output=True)
    pyright_stdout = pyright_cmd.stdout.decode("utf-8")
    try:
        pyright_report = json.loads(pyright_stdout)
    except:
        print("Unable to run pyright on", repo_folder)
        return [], pyright_stdout

    results = []
    for diagnostic in pyright_report["generalDiagnostics"]:
        if diagnostic.get("file", None).endswith(".py") and diagnostic.get("severity", None) == "error":
            rule = diagnostic.get("rule", None)
            message = diagnostic.get("message", "")
            if rule is not None and rule not in ["reportMissingImports"] and "module" not in message:
                # If --outputjson is used, then pyright outputs diagnostics with 0-indexed lines and characters
                assert diagnostic["range"]["start"]["line"] >= 0
                assert diagnostic["range"]["end"]["line"] >= 0
                assert diagnostic["range"]["start"]["character"] >= 0
                assert diagnostic["range"]["end"]["character"] >= 0
                try:
                    relative_file_path = make_path_relative_to_repo(Path(diagnostic["file"]), repo_folder.parts[-1])
                    results.append(
                        ToolResult(
                            tool="pyright",
                            repo_folder=repo_folder.parts[-1],
                            language="python",
                            file_path=str(relative_file_path),
                            severity=diagnostic["severity"],
                            message=diagnostic["message"],
                            rule=diagnostic["rule"],
                            start_line_index=diagnostic["range"]["start"]["line"],
                            end_line_index=diagnostic["range"]["end"]["line"],
                            start_col_index=diagnostic["range"]["start"]["character"],
                            end_col_index=diagnostic["range"]["end"]["character"],
                        )
                    )
                except Exception as e:
                    print("Error when creating test case:", e)
                    print("the above error is related to the diagnostic:", diagnostic)
                    raise e

    random.shuffle(results)
    return results, pyright_stdout


def run_tsc_on_repo(repo_folder: Path) -> Tuple[List[ToolResult], str]:
    """Run the TypeScript compiler on a repo and return the results as ToolResults"""

    tsc_diagnostics = get_tsc_diagnostic_messages()
    diagnostic_codes = {f"TS{d['code']}": f"{d['category']} TS{d['code']}: {k}" for k, d in tsc_diagnostics.items() if d["category"] == "Error" and "import" not in k.lower()}
    results = []

    # Install typescript to repo folder
    cwd = os.getcwd()
    os.chdir(repo_folder)
    # Remove package.json folder if it exists
    Path("package.json").unlink(missing_ok=True)
    Path("package-lock.json").unlink(missing_ok=True)
    Path("tsconfig.json").write_text(json.dumps(tsconfig))
    subprocess.run(["npm", "install", "typescript"], check=False)

    tsc_cmd = subprocess.run(
        "npx tsc -p tsconfig.json".split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    tsc_stdout = tsc_cmd.stdout.decode("utf-8")

    if ": error TS" not in tsc_stdout:
        return [], tsc_stdout

    errors = tsc_stdout.splitlines()

    ignore_errors = ["TS2307:"]  # ignore cannot find module errors
    for error in errors:
        path = Path(error.split("(")[0].strip())
        if path.suffix != ".ts":
            continue
        file_contents = path.read_text()

        if len(file_contents.splitlines()) > 500:
            continue

        loc = re.findall(r"\([0-9]+,[0-9]+\)", error)
        if loc:
            loc = loc[0].lstrip("(").rstrip(")").split(",")
            if len(loc) == 2:
                line = int(loc[0])
                character = int(loc[1])
                if line > len(file_contents.splitlines()):
                    end_character = len(file_contents.splitlines()[len(file_contents.splitlines()) - 1])
                else:
                    end_character = len(file_contents.splitlines()[line - 1])
                end_character = max(character + 1, end_character)
            else:
                continue
        else:
            continue

        if any(ignore_error in error for ignore_error in ignore_errors):
            # print("SKIP due to ignore")
            continue

        rule = error.split(": error ")
        if len(rule) <= 1:
            continue
        rule = rule[1].split(":")[0].strip()
        error_code = diagnostic_codes.get(rule, None)
        if error_code is None:
            continue

        message = ":".join(error.split(": error TS")[1].split(":")[1:]).strip()
        # TODO use ts-server or more robust parsing for tsc

        if any(
            exp in error
            for exp in [
                "import",
                "module",
                "tsx",
                "jsx",
                "need to install",
                "has no exported member",
            ]
        ):
            continue

        results.append(
            ToolResult(
                tool="tsc",
                repo_folder=repo_folder.parts[-1],
                language="typescript",
                file_path=str(path),
                severity="error",
                message=message,
                rule=error_code,
                start_line_index=line - 1,
                end_line_index=line - 1,
                start_col_index=character - 1,
                end_col_index=end_character,  # already 0 indexed from calculation above
            )
        )
    os.chdir(cwd)
    return results, tsc_stdout


def run_pylint_on_repo(repo_folder: Path) -> Tuple[List[ToolResult], str]:
    """Run pylint on a repo and return the results as ToolResults"""

    # ensure an init file exists in repo_folder for pylint to run on the directory
    if not (repo_folder / "__init__.py").exists():
        (repo_folder / "__init__.py").write_text("")

    setup_venv_on_repo(repo_folder)

    # TODO: pyright is pre-installed; should pylint also be in the global environment?
    pcmd = [
        f"source {repo_folder}/.venv/bin/activate",
        "python3 -m pip install pylint > /dev/null",
    ]
    run_script("install_pylint.sh", os.linesep.join(pcmd), throw_on_error=True)
    pcmd = [
        f"source {repo_folder}/.venv/bin/activate",
        f"python3 -m pylint --output-format=json {repo_folder}",
    ]
    # errors from pyright are expected
    pylint_cmd = run_script("run_pylint_on_repo.sh", os.linesep.join(pcmd), throw_on_error=False, return_subprocess_output=True)
    pylint_stdout = pylint_cmd.stdout.decode("utf-8")

    try:
        pylint_report = json.loads(pylint_cmd.stdout.decode("utf-8"))
    except:
        print("Unable to run pylint on", repo_folder)
        print(pylint_cmd.stdout.decode("utf-8"))
        return [], pylint_stdout

    results = []
    for diagnostic in pylint_report:
        if diagnostic.get("path", None).endswith(".py") and diagnostic.get("type", None) == "error":
            rule = diagnostic.get("symbol", None)
            if rule is not None and rule not in ["import-error"]:
                # When --output-format=json is used, pylint lines are 1-indexed but columns are 0-indexed.
                assert diagnostic["line"] >= 0
                assert diagnostic["column"] >= 0
                end_line = diagnostic.get("endLine", diagnostic["line"]) or diagnostic["line"]
                relative_file_path = make_path_relative_to_repo(Path(diagnostic["path"]), repo_folder.parts[-1])
                try:
                    results.append(
                        ToolResult(
                            tool="pylint",
                            repo_folder=repo_folder.parts[-1],
                            language="python",
                            file_path=str(relative_file_path),
                            severity=diagnostic["type"],
                            message=diagnostic["message"],
                            rule=diagnostic["symbol"],
                            start_line_index=diagnostic["line"] - 1,
                            end_line_index=end_line - 1,
                            start_col_index=diagnostic["column"],
                            end_col_index=diagnostic.get("endColumn", diagnostic["column"]),
                        )
                    )
                except Exception as e:
                    print("Error when creating test case:", e)
                    print("the above error is related to the diagnostic:", diagnostic)

    if not results:
        print(f"\n\nNO PYLINT RESULTS FOUND in {repo_folder}")
        print(pylint_stdout)
        print("\n")

    return results, pylint_stdout


@timeout(1800)
def run_roslyn_on_repo(repo_folder: Path) -> Tuple[List[ToolResult], str]:
    """Run Roslyn analyzers on a repo and return the results as ToolResults"""
    csproj_files = list(repo_folder.rglob("*.csproj"))
    output_sarif_path = "error_list.sarif"
    results = []
    output_stdout = ""
    cwd = os.getcwd()
    for csproj_file_abs in csproj_files:
        os.chdir(csproj_file_abs.parent)
        csproj_file = Path(csproj_file_abs.name)

        # Modify the csproj file to include the Roslyn analyzers
        csproj_contents = csproj_file.read_text()
        if 'Include="Microsoft.CodeAnalysis.CSharp"' not in csproj_contents:
            csproj_contents = csproj_contents.replace(
                "</Project>",
                """
        <ItemGroup>
            <PackageReference Include="Microsoft.CodeAnalysis.CSharp" Version="3.2.1" />
            <PackageReference Include="System.Runtime.Loader" Version="4.0.0-*" />
        </ItemGroup>
    </Project>""",
            )

        if f"<ErrorLog>{output_sarif_path},version=2.1</ErrorLog>" not in csproj_contents:
            csproj_contents = csproj_contents.replace(
                "</PropertyGroup>",
                f"""<ErrorLog>{output_sarif_path},version=2.1</ErrorLog>
    </PropertyGroup>""",
            )

        csproj_file.write_text(csproj_contents)

        # nuget restore requires an artifacts directory in the root of the project folder, so make it if it doesn't exist
        (repo_folder / "artifacts").mkdir(exist_ok=True)

        # Run the Roslyn analyzers
        output = subprocess.run(
            ["dotnet", "build", "--no-incremental"],
            capture_output=True,
            text=True,
            check=False,
        )

        if output.returncode != 0:
            output_stdout += str(csproj_file) + os.linesep + output.stdout + os.linesep
            os.chdir(cwd)
            print(output)
            continue

        sarif_path = Path(output_sarif_path)
        if sarif_path.exists():
            try:
                sarif_set = loader.load_sarif_files(sarif_path)
                sarif = sarif_set.files[0]
            except Exception as err:
                print(err)
                print(output)
                os.chdir(cwd)
                continue

            errors = sarif.get_results()
            for error in errors:
                physical_location = error["locations"][0]["physicalLocation"]
                file_path = physical_location["artifactLocation"]["uri"].strip("file:")
                relative_file_path = make_path_relative_to_repo(Path(file_path).resolve(), repo_folder.parts[-1])
                (
                    start_line,
                    start_column,
                    end_line,
                    end_column,
                ) = parse_sarif_result(file_path, error)
                results.append(
                    ToolResult(
                        tool="roslyn",
                        repo_folder=repo_folder.parts[-1],
                        language="csharp",
                        file_path=str(relative_file_path),
                        severity=error["level"],
                        message=error["message"]["text"],
                        rule=error["ruleId"],
                        start_line_index=start_line - 1,
                        end_line_index=end_line - 1,
                        start_col_index=start_column - 1,
                        end_col_index=end_column - 1,
                    )
                )

        os.chdir(cwd)
    print("Found", len(results), "results")
    return results, output_stdout


def run_spotbugs_on_repo(repo_folder: Path) -> Tuple[List[ToolResult], str]:
    """Run spotbugs on a repo and return the results as ToolResults"""

    # TODO use Microsoft Container image
    docker_image = "maven"
    docker_tag = "3.3-jdk-8"

    try:
        repo = Repository("java", repo_folder)
        repo.setup(cleanup=False, install_reqs=True)
        plum = JavaMavenActions(repo, docker_image, docker_tag)
        compile_result = ""
        compile_result = plum.compile()
        assert compile_result["status_result"] == "SUCCESS"
    except Exception as e:
        print("Failed to compile")
        print(e)
        print(compile_result)
        traceback.print_exc()
        return None, compile_result

    try:
        # The spotbugs installation does not get cleaned up because other test case evaluations may re-use it
        spotbugs_path = Path(__file__).parent / "spotbugs_installation"
        error_report = plum.spotbugs(spotbugs_path)
    except Exception as e:
        print("Failed to run spotbugs")
        print(e)
        return None, str(e)

    sarif_path = error_report["spotbugs_sarif"]
    sarif = loader.load_sarif_files(sarif_path)
    sarif_results = sarif.get_results()

    tool_results = []
    for sarif_result in sarif_results:
        physical_location = sarif_result["locations"][0]["physicalLocation"]
        sarif_location = physical_location["artifactLocation"]["uri"]

        # Check that the sarif region exists and reject if not
        if "region" not in physical_location:
            print("NO REGION")
            continue

        search_results = list(repo_folder.rglob(sarif_location))
        if len(search_results) == 0:
            print("UNABLE TO FIND FILE PATH")
            continue

        file_path = search_results[0]
        relative_file_path = make_path_relative_to_repo(file_path, repo_folder.parts[-1])

        # Check if the bug is in any generated source code and reject if so
        if any(forbidden in str(file_path.resolve()) for forbidden in ["generated-", "/target/", "/obj/", "/bin/"]):
            continue

        (
            start_line,
            start_column,
            end_line,
            end_column,
        ) = parse_sarif_result(file_path, sarif_result)
        tool_results.append(
            ToolResult(
                tool="spotbugs",
                repo_folder=repo_folder.parts[-1],
                language="java",
                file_path=str(relative_file_path),
                severity=sarif_result["level"],
                message=sarif_result["message"]["text"],
                rule=sarif_result["ruleId"],
                start_line_index=start_line - 1,
                end_line_index=end_line - 1,
                start_col_index=start_column - 1,
                end_col_index=end_column - 1,
            )
        )

    plum.clean()
    print(f"# Tool results {len(tool_results)} for {repo_folder}")
    return tool_results, error_report


def run_cppcheck_on_repo(repo_folder: Path) -> Tuple[List[ToolResult], str]:
    """Run cppcheck on a repo and return the results as ToolResults"""

    cpp_files = repo_folder.rglob("*.cpp")
    results = []
    for cpp_path in cpp_files:
        output = subprocess.run(
            ["cppcheck", "--xml-version=2", "--enable=warning", str(cpp_path), "--quiet"],
            capture_output=True,
            text=True,
            check=False,
        )

        if output.returncode != 0:
            continue

        # Read the report.xml
        Path("report.xml").write_text(output.stderr)
        report = ET.parse("report.xml")
        root = report.getroot()
        errors = root.find("errors")
        if not errors:
            continue

        for error in errors.findall("error"):
            location = error.find("location")
            if location is None:
                continue

            msg = error.attrib["verbose"]
            rule_id = error.attrib["id"]
            file_abs_path = Path(location.attrib["file"]).resolve()
            relative_path = Path(location.attrib["file"]).relative_to(repo_folder.resolve())
            file_contents = file_abs_path.read_text()
            start_line_index = int(location.attrib["line"]) - 1
            end_line_index = start_line_index + 1
            start_col_index = int(location.attrib["column"]) - 1
            end_col_index = len(file_contents.splitlines()[start_line_index]) - 1

            if "configure" in msg.lower() or rule_id in ("cppcheckError", "syntaxError"):
                continue

            results.append(
                ToolResult(
                    tool="cppcheck",
                    repo_folder=repo_folder.parts[-1],
                    language="cpp",
                    file_path=str(relative_path),
                    severity=error.attrib["severity"],
                    message=error.attrib["verbose"],
                    rule=rule_id,
                    start_line_index=start_line_index,
                    end_line_index=end_line_index,
                    start_col_index=start_col_index,
                    end_col_index=end_col_index,
                )
            )

    print(f"Found {len(results)} test cases")
    return results, output.stdout.decode('utf-8') + "\n" + output.stderr.decode('utf-8')
