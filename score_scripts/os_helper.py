"""Base class for scorers. Scorers contain implementation of predict, eval, and/or simulate methods."""
import io
import re
import os
import subprocess
from multiprocessing import Lock
from uuid import uuid4

# This must be an instance of multiprocess.Lock
PRINT_LOCK: Lock = None

# Pylint intends to force us to use classes instead of globals. This is part of work item 291.
# pylint: disable=global-statement
def set_print_lock(lock: Lock) -> None:
    """Sets the module lock used to make printing messages to log files safe for multiprocessing."""
    global PRINT_LOCK
    PRINT_LOCK = lock
# pylint: enable=global-statement

def _log_print(*args, **kwargs):
    """Print a message to stdout."""
    if PRINT_LOCK:
        PRINT_LOCK.acquire()
    try:
        print(*args, **kwargs)
        with open("base_score.log", "+a", encoding="utf-8") as log_file:
            print(*args, **kwargs, file=log_file)
    finally:
        if PRINT_LOCK:
            PRINT_LOCK.release()

def sanitize_print(*args, **kwargs):
    """Print a message to stdout after sanitizing it."""

    def print_to_string(*args, **kwargs):
        output = io.StringIO()
        print(*args, file=output, **kwargs)
        contents = output.getvalue()
        output.close()
        return contents.rstrip("\n")

    msg = print_to_string(*args, **kwargs)
    msg = re.sub(r"--password \S+", "--password ***", msg)
    msg = re.sub(r"--token \S+", "--token ***", msg)
    msg = re.sub(r"--hmac-key \S+", "--hmac-key ***", msg)
    msg = re.sub(r"accessToken=\S+", "accessToken=***", msg)
    msg = re.sub(r"AUTHORIZATION: bearer \S+", "AUTHORIZATION: bearer ***", msg)
    _log_print(msg)


def run_script(script_fname: str, script_contents: str, throw_on_error: bool = True, return_subprocess_output: bool = False):
    """Run a shell script. The script is printed, written to a file and then run."""

    prepend = ""

    # ensure that we're using bash
    if not script_contents.startswith("#!"):
        prepend = prepend + "#!/bin/bash\n"

    # add set -xe to the top of the script to exit the script immediately if anything fails.
    if throw_on_error:
        prepend = prepend + "set -xe\n"

    if prepend:
        script_contents = prepend + script_contents

    script_fname = str(uuid4()) + script_fname

    sanitize_print(f"{script_fname}\n{script_contents}")

    try:
        with open(script_fname, "wt", encoding="utf-8") as script_file:
            script_file.write(script_contents)
        os.chmod(script_fname, 0o777)
        # redirecting to a pipe will cause nothing to print until the script is done. So if a script prompts for input, it will seem to hang.
        # AML kills the script after an hour, so if you see an hour long hang, this is likely the cause.
        result = subprocess.run(["./" + script_fname], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, check=False)
        if not return_subprocess_output:
            sanitize_print(result.stdout.decode('utf-8'))
        sanitize_print(f"Script {script_fname} {'exited' if not result.returncode else 'failed'} with code {result.returncode}")
        if throw_on_error:
            result.check_returncode()
        return result.returncode if not return_subprocess_output else result
    finally:
        os.remove(script_fname)
