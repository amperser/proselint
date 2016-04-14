"""Check that the CLI returns the appropriate exit code."""

import subprocess


def test_exit_code_demo():
    """Ensure that linting the demo returns an exit code of 1."""
    try:
        subprocess.check_output(["proselint", "--demo"])

    except subprocess.CalledProcessError as grepexc:
        assert(grepexc.returncode == 1)


def test_exit_code_version():
    """Ensure that getting the version returns an exit code of 0."""
    try:
        subprocess.check_output(["proselint", "--version"])

    except subprocess.CalledProcessError:
        assert(False)
