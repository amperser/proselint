import importlib
import os
import re
from pathlib import Path

import proselint
from proselint.tools import lint
from proselint.tools import load_options


def test_config_flag_ignore_unavailable():
    """program should not crash with faulty config -> just inform"""
    cfg = load_options()
    cfg["checks"]["misc.santa_clause_is_real"] = True
    lint("Smoke phrase with nothing flagged.", config=cfg)


def test_config_default_flag_for_check_missing():
    """test default-config for completeness
    Note: if triggered the default config has a flag that points to a missing check
          -> remove it!
    """
    checks = []
    check_names = load_options()["checks"].keys()

    for check_name in check_names:
        module = importlib.import_module("." + check_name, "proselint.checks")
        checks += [
            getattr(module, d) for d in dir(module) if re.match("check", d)
        ]


def is_check(file_path: Path) -> bool:
    """Check whether a file contains a check."""
    if file_path.suffix != ".py":
        return False
    if file_path.name == "__init__.py":
        return False
    if "inprogress" in file_path.as_posix():
        return False
    return True


def test_config_default_check_for_flag_missing():
    """test default-config for completeness
    Note: if triggered the flag / key is missing in default config
          -> add it!
    """
    cfg = load_options()
    checks_path = (proselint.path / "checks").absolute()
    listing = os.walk(checks_path)
    # todo: this should recurse in sub-dirs

    for _root, _, _files in listing:
        root_path = Path(_root)
        for _file in _files:
            file_path = root_path / _file
            if is_check(file_path):
                if not (file_path.parent / "__init__.py").exists():
                    raise FileNotFoundError(
                        "Check-Directory is missing '__init__.py'"
                    )

                flag_name = (
                    str(
                        file_path.absolute()
                        .with_suffix("")
                        .relative_to(checks_path),
                    )
                    .replace("\\", ".")
                    .replace("/", ".")
                )

                assert flag_name in cfg["checks"]
