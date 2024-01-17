"""Check that a check is working."""

import os
from pathlib import Path

from proselint.tools import lint


def assert_error(check: str, text: str, n: int = 1):
    # todo: check_in_result - replace remaining
    """Assert that text has n errors of type check."""
    assert_error.description = f"No {check} error for '{text}'"
    assert check in [error[0] for error in lint(text)]


class Check:
    """All tests inherit from Check."""

    def wpe_too_high(check) -> None:  # todo is this salvageable?
        """Check whether the check is too noisy."""
        min_wpe = 50

        examples_path = (
            Path.cwd() / "tests" / "corpus"
        )  # TODO: probably old path to corpus
        examples = os.listdir(examples_path)

        for example in examples:
            example_path = examples_path / example

            if ".DS_Store" in example_path:
                break

            # Compute the number of words per (wpe) error.
            with example_path.open(encoding="utf-8") as fh:
                text = fh.read()
                num_errors = len(check.__wrapped__(text))
                num_words = len(text)

            try:
                wpe = 1.0 * num_words / num_errors
            except ZeroDivisionError:
                wpe = float("Inf")

            # Make sure that
            assert wpe > min_wpe, f"{example} has only {round(wpe, 2)} wpe."
