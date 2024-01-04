import os
import subprocess
from pathlib import Path
import pytest


@pytest.fixture
def script_path() -> Path:
    path = Path(__file__).resolve().parent.parent / "scripts"
    os.chdir(path)
    return path


scripts = [
    "benchmark_checks.py",
    "benchmark_constants.py",
    "benchmark_hashes.py",
    "benchmark_linter.py",
    "benchmark_list_alternatives.py",
    "benchmark_test_hyperlinks_on_shell.py",
]


@pytest.mark.parametrize("file", scripts)
def test_scripts(script_path: Path, file) -> None:
    subprocess.check_call(f"python {script_path / file}", shell=True)
