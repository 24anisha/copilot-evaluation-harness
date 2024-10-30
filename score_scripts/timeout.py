# Copyright (c) Microsoft. All rights reserved.
""" Timeout utilities """

import os
import errno
import signal
import functools


class EvalTimeoutError(Exception):
    """Exception to raise on a timeout"""

    def __init__(self, message):
        super().__init__(message)


def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    """Timeout decorator from https://stackoverflow.com/a/22348885/119527"""

    def decorator(func):
        def _handle_timeout(_, __):
            raise EvalTimeoutError(error_message + f" after {seconds} seconds")

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wrapper

    return decorator
