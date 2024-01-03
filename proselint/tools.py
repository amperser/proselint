"""General-purpose tools shared across linting checks."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import sys
import time
import traceback
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import IO, Callable, Optional, TypeAlias, Union
from warnings import showwarning as warn

from . import config_base
from .config_paths import config_global_path, config_user_paths
from .lint_cache import memoize_lint
from .lint_checks import get_checks
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


def get_line_and_column(text, position):
    """Return the line number and column of a position in a string."""
    position_counter = 0
    line_no = 0
    for line in text.splitlines(True):
        if (position_counter + len(line.rstrip())) >= position:
            break
        position_counter += len(line)
        line_no += 1
    return line_no, position - position_counter


def _lint_loop(_check: Callable, _text: str, _hash: str) -> list[ResultLint]:
    # TODO: frozenset is hashable (list without duplicates) -> check-list, result-lists
    errors = []
    results = _check(_text)
    for result in results:
        (start, end, check_name, message, replacements) = result
        (line, column) = get_line_and_column(_text, start)
        if not is_quoted(start, _text):
            errors += [
                (
                    check_name,
                    message,
                    line,
                    column,
                    start,
                    end,
                    end - start,
                    "warning",
                    replacements,
                ),
            ]
    return errors


@memoize_lint
def lint(
    content: Union[str, IO],
    config: Optional[dict] = None,
    checks: Optional[list[Callable]] = None,
    hash_: Optional[str] = None,
) -> list[ResultLint]:
    """Run the linter on the input file."""
    # TODO: better candidate for the memoizer (on matching content + cfg)
    # TODO: this seems now also just like a wrapper
    if isinstance(content, str):
        _text = content
    else:
        _text = content.read()

    if not isinstance(config, dict):
        config = config_base.proselint_base

    if checks is None:
        checks = get_checks(config)

    if hash_ is None:
        hash_ = hashlib.sha224(_text.encode("utf-8")).hexdigest()

    # Apply all the checks.
    if config["parallelize_checks"]:
        # freeze_support() todo
        with ProcessPoolExecutor() as exe:
            # note1: ThreadPoolExecutor is only concurrent, but not multi-cpu
            # note2: .map() is build on .submit(), harder to use here, same speed
            futures = [exe.submit(_lint_loop, check, _text, hash_) for check in checks]
            # exe.shutdown(wait=True)  # precaution todo
        errors = [_e for _ft in futures for _e in _ft.result()]
        # errors.extend([_ft.result for _ft in futures]), try it
    else:
        results = [_lint_loop(check, _text, hash_) for check in checks]
        errors = [_e for _res in results for _e in _res]

    # Sort the errors by line and column number.
    return sorted(errors[: config["max_errors"]], key=lambda e: (e[2], e[3]))


def _lint_path_loop(
    path: Path,
    config: dict,
    checks: list[Callable],
) -> list[ResultLint]:
    log.debug("Processing '%s'", path.name)
    try:
        with path.open(encoding="utf-8", errors="replace") as _fh:
            content = _fh.read()
    except Exception:
        traceback.print_exc()
        return []
    return lint(content, config=config, checks=checks)


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

    if len(filepaths) < 2:
        config["parallelize_lints"] = False
        log.info("Disabled parallelize_lints (only single file)")

    results = {}
    ts_start = time.time()
    if len(paths) == 0:
        # Use stdin if no paths were specified
        log.info("No path specified -> will read from <stdin>")
        results["<stdin>"] = lint(sys.stdin, config=config, checks=checks)
    elif config["parallelize_lints"]:
        _workers = max(min(os.cpu_count(), len(filepaths)), 1)
        with ProcessPoolExecutor(_workers) as exe:
            # note1: ThreadPoolExecutor is only concurrent, but not multi-cpu
            # note2: .map() is build on .submit(), harder to use here, same speed
            futures = {
                file: exe.submit(_lint_path_loop, file, config, checks)
                for file in filepaths
            }
            # exe.shutdown(wait=True)  # precaution
            # TODO: should probably disable check-paralleling or use same executor?
        results = {_file: _ft.result() for _file, _ft in futures.items()}
    else:
        results = {file: _lint_path_loop(file, config, checks) for file in filepaths}

    error_num = 0
    for _file, _errors in results.items():
        # todo: include filename in ResultLint?
        print_errors(_file, _errors, output_json, compact)
        error_num += len(_errors)

    duration = time.time() - ts_start
    log.info("Found %d lint-warnings in %.3f s", error_num, duration)
    return results


def is_quoted(position: int, text: str) -> bool:
    """Determine if the position in the text falls within a quote."""

    def matching(quotemark1: str, quotemark2: str) -> bool:
        straight = "\"'"
        curly = "“”"
        return (quotemark1 in straight and quotemark2 in straight) or (
            quotemark1 in curly and quotemark2 in curly
        )

    def find_ranges(_text: str) -> list[tuple[int, int]]:
        # TODO: optimize, as it is top3 time-waster (of user-functions)
        #       this could be a 1d array / LUT
        s = 0
        q = pc = ""
        start = None
        ranges = []
        seps = " .,:;-\r\n"
        quotes = ['"', "“", "”", "'"]
        for i, c in enumerate(_text + "\n"):
            if s == 0 and c in quotes and pc in seps:
                start = i
                s = 1
                q = c
            elif s == 1 and matching(c, q):
                s = 2
            elif s == 2:
                if c in seps:
                    ranges.append((start + 1, i - 1))
                    start = None
                    s = 0
                else:
                    s = 1
            pc = c
        return ranges

    def position_in_ranges(ranges: list[tuple[int, int]], _position: int) -> bool:
        return any(start <= _position < end for start, end in ranges)

    return position_in_ranges(find_ranges(text), position)


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
