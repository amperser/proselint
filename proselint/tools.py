"""General-purpose tools shared across linting checks."""

from __future__ import annotations

import contextlib
import copy
import json
import os
import sys
from concurrent.futures import Executor
from concurrent.futures import Future
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Callable
from typing import NamedTuple
from typing import Optional
from typing import Union
from warnings import showwarning as warn

from . import config_base
from .checks import get_checks
from .checks import run_check
from .config_base import Output
from .config_paths import config_global_path
from .config_paths import config_user_paths
from .logger import log
from .memoizer import cache


class ResultLint(NamedTuple):
    # allows access by name and export ._asdict()
    # note: const after instantiation & trouble with pickling
    check: str
    message: str
    source: str
    line: int
    column: int
    start: int
    end: int
    extent: int
    severity: str
    replacements: Optional[str]


###############################################################################
# Config ######################################################################
###############################################################################


def _deepmerge_dicts(
    base: dict,
    overrides: dict,
) -> dict:
    """Deep merge dictionaries, second dict will take priority.
    # Note: this could be faster, just sum dicts -> not relevant here
    """
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

last_char_count: int = 0


def extract_files(paths: Union[Path, list[Path]]) -> list[Path]:
    """Expand list of paths to include all text files matching the pattern."""
    legal_extensions = [".md", ".txt", ".rtf", ".html", ".tex", ".markdown"]

    if isinstance(paths, Path):
        paths = [paths]

    expanded_files = []
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


def lint(
    content: str,
    config: Optional[dict] = None,
    source_name: str = "",
    allow_futures: bool = False,
    *,  # internals from here on, caution
    _checks: Optional[list[Callable]] = None,
    _exe: Optional[Executor] = None,
) -> list[ResultLint]:
    """Run the linter on the input file.

    arguments:
        allow_futures: skip the internal memoizer, has to be done later manually
    """
    if not isinstance(content, str):
        raise ValueError("linter expects a string as content")

    if not isinstance(config, dict):
        config = config_base.proselint_base
    if _checks is None:
        _checks = get_checks(config)

    memoizer_key = cache.calculate_key(content, _checks)
    # TODO: filename enables more elegant 2d-dict
    #       d[funcSig,fileSig] = (input_hash,result)
    #                        -> smaller, more efficient dicts

    with contextlib.suppress(KeyError):
        # early exit if result is already cached
        errors = cache[memoizer_key]
        return [ResultLint(**_e) for _e in errors]

    # padding
    # -> some checks expect words in text and expect something around it
    # -> this prevents edge-cases
    # -> is considered in run_checks()
    content = f"\n{content}\n "  # benchmarked the fastest OP

    # Apply all the checks.
    if config["parallelize"]:
        # TODO: simplify always multi, thread, benchmark performance
        if _exe is None:
            _exe = ProcessPoolExecutor()
            log.debug("[Lint] created inner Executor for parallelization")
        else:
            log.debug("[Lint] used outer Executor for parallelization")
        # NOTE: ThreadPoolExecutor is only concurrent, but not multi-cpu processed
        # NOTE: .map() is build on .submit(), harder to use here, same speed
        futures = [
            _exe.submit(run_check, check, content, source_name) for check in _checks
        ]
        if allow_futures:
            cache.name2key[source_name] = memoizer_key
            return futures
        errors = [_e for _ft in futures for _e in _ft.result()]
        # errors.extend([_ft.result for _ft in futures]), try it
    else:  # single process
        results = [run_check(check, content) for check in _checks]
        errors = [_e for _res in results for _e in _res]

    # Sort the errors by line and column number.
    errors = sorted(
        errors[: config["max_errors"]], key=lambda e: (e["line"], e["column"])
    )
    cache[memoizer_key] = errors
    # return user-friendly format
    return [ResultLint(**_e) for _e in errors]


def fetch_results(
    futures: Union[list[Future], list[ResultLint]], config: dict, source_name: str
) -> list[ResultLint]:
    """fetch result from futures, needed when working with multiprocessing"""
    if len(futures) > 0 and isinstance(futures[0], Future):
        _errors = [_e for _ft in futures for _e in _ft.result()]
        _errors = sorted(
            _errors[: config["max_errors"]],
            key=lambda e: (e["line"], e["column"]),
        )
        # store results in cache
        key = cache.name2key.get(source_name)
        cache[key] = _errors
        return [ResultLint(**_e) for _e in _errors]
    return futures


def lint_path(
    paths: Union[Path, list[Path]],
    config: Optional[dict] = None,
) -> dict[Path, list[ResultLint]]:
    """Lint path with files or point to specific file"""
    # Expand the list of directories and files.
    filepaths = extract_files(paths)

    if not isinstance(config, dict):
        config = config_base.proselint_base
    checks = get_checks(config)

    results = {}
    chars = 0

    if len(filepaths) == 0:
        # Use stdin if no paths were specified
        log.info("No path specified -> will read from <stdin>")
        content = sys.stdin.read()
        results["<stdin>"] = lint(content, config=config, _checks=checks)
    else:
        # offer "outer" executor, to make multiprocessing more effective
        exe = ProcessPoolExecutor() if config["parallelize"] else None
        for file in filepaths:
            log.debug("Analyzing '%s'", file.name)
            try:
                with file.open(encoding="utf-8", errors="replace") as _fh:
                    content = _fh.read()
            except Exception:
                log.exception("[LintPath] Error opening '%s' -> will skip", file.name)
                continue
            results[file] = lint(
                content,
                config,
                source_name=file.as_posix(),
                allow_futures=True,
                _checks=checks,
                _exe=exe,
            )
            chars += len(content)

    # fetch result from futures, if needed
    results = {
        _file: fetch_results(_errors, config, _file.as_posix())
        for _file, _errors in results.items()
    }

    # bad style ... but
    global last_char_count
    last_char_count = chars
    return results


def convert_to_json(
    results: Union[dict[list[str, ResultLint]], list[ResultLint]],
) -> str:
    """Convert the errors to JSON.

    Note: old items was just a list, now it's a named tuple with the names as below

    out = [
        {
            "check": item[0],
            "message": item[1],
            "source": item[2],
            "line": item[3],
            "column": item[4],
            "start": item[5],
            "end": item[6],
            "extent": item[7],
            "severity": item[8],
            "replacements": item[9],
        }
        for item in items
    ]
    """
    if isinstance(results, dict):
        out = [_rl.to_json() for _res in results.values() for _rl in _res]
    else:
        # assumed list
        out = [_rl._asdict() for _rl in results]

    return json.dumps({"status": "success", "data": {"errors": out}}, sort_keys=True)


def print_to_console(  # noqa: PLR0912
    results: Union[dict[str, list[ResultLint]], list[ResultLint]],
    config: Optional[dict] = None,
    file_path: Optional[Path] = None,
) -> None:
    """Print the errors, resulting from lint, for filename."""
    if config is None:
        config = config_base.proselint_base

    try:
        out_fmt = Output[config["output_format"]]
    except KeyError:
        out_fmt = Output[config_base.proselint_base["output_format"]]

    if not isinstance(results, (list, dict)):
        log.error(
            "[OutputError] no list or provided "
            "(guess: results of lint_path() need to be extracted first)"
        )
        return
    # encapsulate output of lint() to match that of lint_path()
    if isinstance(results, list):
        results = {file_path: results}

    for _file, _results in results.items():
        if out_fmt == Output.json:
            log.info(convert_to_json(_results))
        else:
            for _e in _results:
                _source = _e.source
                if isinstance(_file, Path):
                    if out_fmt == Output.compact:
                        _source = _file.name
                    else:
                        _source = _file.absolute().as_uri()
                        # TODO: would be nice to supress "file:///"
                        # https://gist.github.com/egmontkob/eb114294efbcd5adb1944c9f3cb5feda
                elif out_fmt == Output.compact:
                    _source = ""

                log.info(
                    "%s:%d:%d: %s %s", _source, _e.line, _e.column, _e.check, _e.message
                )
