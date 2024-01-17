import os
import subprocess
from pathlib import Path

import pytest


@pytest.fixture
def project_path() -> Path:
    path = Path(__file__).resolve().parent.parent
    os.chdir(path)
    return path


scripts = [
    "scripts/benchmark_checks.py",
    "scripts/benchmark_constants.py",
    "scripts/benchmark_hashes.py",
    "scripts/benchmark_linter.py",
    "scripts/benchmark_list_alternatives.py",
    "scripts/benchmark_regex.py",
    "scripts/benchmark_str_format.py",
    "scripts/test_hyperlinks_on_shell.py",
]


@pytest.mark.parametrize("file", scripts)
def test_scripts(project_path: Path, file) -> None:
    subprocess.check_call(f"python3 {project_path / file}", shell=True)


examples = [
    "examples/use_as_module.py",
]


@pytest.mark.parametrize("file", examples)
def test_examples(project_path: Path, file) -> None:
    subprocess.check_call(f"python3 {project_path / file}", shell=True)
