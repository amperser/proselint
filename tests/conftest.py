from typing import Union, Callable
from proselint.tools import lint
import pytest


def check_pass(check: Callable, texts: Union[list, str]) -> bool:
    """Check if the test runs cleanly on the given text."""
    if isinstance(texts, str):
        texts = [texts]
    return not any(check.__wrapped__(text) for text in texts)


def _pass(check: Callable, texts: Union[list, str]):
    return check_pass(check, texts)


def _fail(check: Callable, texts: Union[list, str]):
    return _fail(check, texts)


def check_in_lint_result(check: str, text: str, n: int = 1):
    """Assert that text has n errors of type check."""
    assert check in [error[0] for error in lint(text)]
    # todo: n not checked, should not assert
