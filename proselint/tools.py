"""General-purpose tools shared across linting checks."""

from __future__ import annotations

import copy
import importlib
import json
import os
import re
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import IO, Callable, Optional, TypeAlias, Union
from warnings import showwarning as warn

from . import config_base
from .checks import ResultCheck, run_checks
from .config_paths import config_global_path, config_user_paths
from .memoizer import memoize_lint
from .logger import log

ResultLint: TypeAlias = tuple[str, str, int, int, int, int, int, str, str]
# content: check_name, message, line, column, start, end, length, type, replacement


###############################################################################
# Config ######################################################################
###############################################################################


def _deepmerge_dicts(
    base: dict,
    overrides: dict,
) -> dict:  # TODO: this can be faster, we can just add dicts
    """Deep merge dictionaries, second dict will take priority."""
    result = copy.deepcopy(base)

    for key, value in overrides.items():
        if isinstance(value, dict):
            result[key] = _deepmerge_dicts(result.get(key) or {}, value)
        else:
            result[key] = value

    return result


def load_options(
    config_file_path: Optional[Path] = None,
) -> dict:
    """Read various proselintrc files, allowing user overrides."""
    cfg_default = config_base.proselint_base

    if config_global_path.is_file():
        log.debug("Config read from global '%s' (as base)", config_global_path)
        _cfg = json.load(config_global_path.open())
        cfg_default = _deepmerge_dicts(cfg_default, _cfg)

    if config_file_path:
        if not config_file_path.is_file():
            raise FileNotFoundError(f"Config file {config_file_path} does not exist")
        config_user_paths.insert(0, config_file_path)

    user_options = {}
    for path in config_user_paths:
        if path.is_file():
            log.debug("Config read from '%s'", path)
            user_options = json.load(path.open())
            break
        path_old = path.with_suffix("")
        if path_old.is_file() and path.suffix != "":
            warn(
                f"{path_old} was found instead of a JSON file. Rename to {path}.",
                DeprecationWarning,
                "",
                0,
            )
            user_options = json.load(path_old.open())
            break

    return _deepmerge_dicts(cfg_default, user_options)


def get_checks(options: dict) -> list[Callable[[str, str], list[ResultCheck]]]:
    """Extract the checks.
    Rule: fn-name must begin with "check", so check_xyz() is ok
    """
    # TODO: benchmark consecutive runs of this
    # TODO: config should only translate once to check-list
    checks = []
    check_names = [key for (key, val) in options["checks"].items() if val]

    for check_name in check_names:
        try:
            module = importlib.import_module("." + check_name, "proselint.checks")
        except ModuleNotFoundError:
            log.exception(
                "requested config-flag '%s' not found in proselint.checks",
                check_name,
            )
            continue
        checks += [getattr(module, d) for d in dir(module) if re.match(r"^check", d)]
        # todo: name should start with check

    log.debug("Collected %d checks to run", len(checks))
    return checks


###############################################################################
# Linting #####################################################################
###############################################################################


def extract_files(paths: list[Path]) -> list[Path]:
    """Expand list of paths to include all text files matching the pattern."""
    expanded_files = []
    legal_extensions = [".md", ".txt", ".rtf", ".html", ".tex", ".markdown"]

    for _path in paths:
        # If it's a directory, recursively walk through it and find the files.
        if _path.is_dir():
            for _dir, _, _filenames in os.walk(_path):
                _path = Path(_dir)
                for filename in _filenames:
                    _file_path = _path / filename
                    if _file_path.suffix.lower() in legal_extensions:
                        expanded_files.append(_file_path)

        # Otherwise add the file directly.
        else:
            expanded_files.append(_path)

    return expanded_files


@memoize_lint
def lint(
    content: Union[str, IO],
    config: Optional[dict] = None,
    checks: Optional[list[Callable]] = None,
    hash_: Optional[str] = None,
) -> list[ResultLint]:
    """Run the linter on the input file."""

    if isinstance(content, str):
        _text = content
    else:
        _text = content.read()

    if not isinstance(config, dict):
        config = config_base.proselint_base

    if checks is None:
        checks = get_checks(config)

    # Apply all the checks.
    if config["parallelize"]:  # and __name__ == '__main__':
        exe = ProcessPoolExecutor()
        # NOTE: ThreadPoolExecutor is only concurrent, but not multi-cpu
        # NOTE: .map() is build on .submit(), harder to use here, same speed
        futures = [exe.submit(run_checks, check, _text) for check in checks]
        errors = [_e for _ft in futures for _e in _ft.result()]
        # errors.extend([_ft.result for _ft in futures]), try it
    else:  # single process
        results = [run_checks(check, _text) for check in checks]
        errors = [_e for _res in results for _e in _res]

    # TODO: might still possible to optimize by handing out futures
    #       and adding to cache later
    # Sort the errors by line and column number.
    return sorted(errors[: config["max_errors"]], key=lambda e: (e[2], e[3]))


def lint_path(
    paths: Union[Path, list[Path]],
    config: Optional[dict] = None,
) -> dict[str, list[ResultLint]]:
    # Expand the list of directories and files.
    filepaths = extract_files(paths)

    if not isinstance(config, dict):
        config = config_base.proselint_base
    checks = get_checks(config)
    output_json = False  # TODO, derive from config
    compact = False  # TODO: feed config into printer()

    results = {}
    chars = 0
    ts_start = time.time()
    if len(paths) == 0:
        # Use stdin if no paths were specified
        log.info("No path specified -> will read from <stdin>")
        results["<stdin>"] = lint(sys.stdin, config=config, checks=checks)
    else:
        for file in filepaths:
            log.debug("Analyzing '%s'", file.name)
            try:
                with file.open(encoding="utf-8", errors="replace") as _fh:
                    content = _fh.read()
            except Exception:
                # traceback.print_exc()
                log.exception("Error while opening '%s'", file.name)
                continue
            results[file] = lint(content, config=config, checks=checks)
            chars += len(content)
        # results = {file: _lint_path_loop(file, config, checks) for file in filepaths}

    error_num = 0
    for _file, _errors in results.items():
        # todo: include filename in ResultLint?
        print_errors(_file, _errors, output_json, compact)
        error_num += len(_errors)

    duration = time.time() - ts_start
    log.info(
        "Found %d lint-warnings in %.3f s (%d files, %.2f kiByte)",
        error_num,
        duration,
        len(filepaths),
        chars / 1024,
    )
    return results


def errors_to_json(items: list[ResultLint]) -> str:
    """Convert the errors to JSON."""
    out = [
        {
            "check": item[0],
            "message": item[1],
            "line": 1 + item[2],
            "column": 1 + item[3],
            "start": 1 + item[4],
            "end": 1 + item[5],
            "extent": item[6],
            "severity": item[7],
            "replacements": item[8],
        }
        for item in items
    ]

    return json.dumps({"status": "success", "data": {"errors": out}}, sort_keys=True)


def print_errors(
    filename: Union[Path, str],
    errors: list[ResultLint],
    output_json: bool = False,
    compact: bool = False,
) -> None:
    """Print the errors, resulting from lint, for filename."""
    if output_json:
        log.info(errors_to_json(errors))

    else:
        for error in errors:
            (
                check,
                message,
                line,
                column,
                _,  # start,
                _,  # end,
                _,  # extent,
                _,  # severity,
                _,  # replacements,
            ) = error

            if isinstance(filename, Path):
                if compact:
                    filename = filename.name
                else:
                    filename = filename.absolute().as_uri()
                    # TODO: would be nice to supress "file:///"
                    # https://gist.github.com/egmontkob/eb114294efbcd5adb1944c9f3cb5feda
            elif compact:
                filename = ""

            log.info("%s:%d:%d: %s %s", filename, 1 + line, 1 + column, check, message)
