from typing import Callable, Union

from proselint.tools import lint


def check_pass(check: Callable, texts: Union[list, str]) -> bool:
    """Check if the test runs cleanly on the given text."""
    if isinstance(texts, str):
        texts = [texts]
    return not any(len(check(text)) > 0 for text in texts)


def assert_pass(check: Callable, texts: Union[list, str]) -> None:
    """Check if the test runs cleanly on the given text."""
    if isinstance(texts, str):
        texts = [texts]
    for _text in texts:
        assert check(_text) == []


def assert_fail(check: Callable, texts: Union[list, str]) -> None:
    """Check if the test runs triggers on the given text."""
    if isinstance(texts, str):
        texts = [texts]
    for _text in texts:
        assert check(_text) != []


def check_in_lint_result(check: str, text: str, n: int = 1):
    """Assert that text has n errors of type check."""
    assert check in [error[0] for error in lint(text)]
    # todo: n not checked, should not assert


def print_invoke_return(result) -> None:
    print(f"result::{result}")

    print(f"exit::{result.exit_code}")
    print(f"retvalt::{result.return_value}")

    print(f"output::{result.output}")
    print(f"stdout::{result.stdout}")
    print(f" _bytes::{result.stdout_bytes}")
