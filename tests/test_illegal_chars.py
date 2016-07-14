"""Check that the CLI can handle invalid characters."""

import subprocess


def test_invalid_characters():
    """Ensure that a file with illegal characters does not break us."""
    try:
        # We only print out exception text and continue after printing a trace,
        # so the only way (currently) to test for failure is to look for the
        # exception text. Refactoring the command line function would let us
        # write better tests (one day).
        output = subprocess.check_output(
            ["proselint", "illegal-chars.txt"]
        )
        assert("UnicodeDecodeError" not in str(output))
    except:
        assert(False)
