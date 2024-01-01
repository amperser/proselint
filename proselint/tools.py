"""General-purpose tools shared across linting checks."""

from __future__ import annotations

import copy
import hashlib
import json
import os
from pathlib import Path
from typing import IO, Optional, TypeAlias, Union
from warnings import showwarning as warn

from . import config_default
from .config_paths import config_global_path, config_user_paths
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
    cfg_default = config_default.proselint_base

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


def lint(
    content: Union[str, IO],
    debug: bool = False,
    cfg: Optional[dict] = None,
) -> list[ResultLint]:
    """Run the linter on the input file."""
    if isinstance(content, str):
        _text = content
    else:
        _text = content.read()

    if not isinstance(cfg, dict):
        cfg = config_default.proselint_base

    # Get the checks.
    checks = get_checks(cfg)
    _hash = hashlib.sha224(_text.encode("utf-8")).hexdigest()

    # Apply all the checks.
    errors = []
    for check in checks:
        # TODO: can be run in parallel
        results = check(_text, _hash)

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

        if len(errors) > cfg["max_errors"]:
            break

    # Sort the errors by line and column number.
    return sorted(errors[: cfg["max_errors"]], key=lambda e: (e[2], e[3]))


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
        for start, end in ranges:
            if start <= _position < end:
                return True
        return False

    return position_in_ranges(find_ranges(text), position)


def errors_to_json(items: list[ResultLint]) -> str:
    """Convert the errors to JSON."""
    out = []
    for item in items:
        out.append(
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
            },
        )

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
