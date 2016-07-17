"""Check that the CLI can handle invalid characters."""

import os.path as pth
import subprocess


def test_invalid_characters():
    """Ensure that a file with illegal characters does not break us."""
    try:
        output = ""
        curr_dir = pth.dirname(pth.abspath(__file__))
        test_file = pth.join(curr_dir, "illegal-chars.txt")
        # We only print out exception text and continue after printing a trace,
        # so the only way (currently) to test for failure is to look for the
        # exception text. Refactoring the command line function would let us
        # write better tests (one day).
        output = str(subprocess.check_output(
            ["proselint", test_file],
            stderr=subprocess.STDOUT
        ))
    except subprocess.CalledProcessError as e:
        # Non-zero return codes are OK, but what did we catch?
        print("Non-zero return value: will proceed. %s" % e)
        output += str(e.output)
    except Exception:
        assert(not "Unknown Exception Occurred")

    assert("UnicodeDecodeError" not in output)  # Failed to process the file
    assert("FileNotFoundError" not in output)   # Failed to find our test file
