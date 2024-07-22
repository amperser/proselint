"""General-purpose tools shared across linting checks."""

from __future__ import annotations

import contextlib
import copy
import json
import os
import sys
from concurrent.futures import Executor, Future, ProcessPoolExecutor
from pathlib import Path
from typing import NamedTuple, Optional, Union
from warnings import showwarning as warn

from . import config_base
from .checks import CheckSpec, registry, run_check
from .config_base import Output
from .config_paths import config_global_path, config_user_paths
from .logger import log
from .memoizer import cache


class LintResult(NamedTuple):
    """A lint result."""

    # allows access by name and export ._asdict()
    # NOTE: const after instantiation & trouble with pickling
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
    """Merge dictionaries recursively. `overrides` takes priority."""
    # Note: this could be faster, just sum dicts -> not relevant here
    result = copy.deepcopy(base)

    for key, value in overrides.items():
        if isinstance(value, dict):
            result[key] = _deepmerge_dicts(result.get(key, {}), value)
        else:
            result[key] = value

    return result


def load_options(
    config_file_path: Optional[Path] = None,
) -> dict:
    """Read various proselintrc files, allowing user overrides."""
    # TODO: allow toml - json is a pain for user-configs
    cfg_default = config_base.proselint_base

    # global config will be a base for
    if config_global_path.is_file():
        log.debug("Config read from global '%s' (as base)", config_global_path)
        _cfg = json.load(config_global_path.open())
        cfg_default = _deepmerge_dicts(cfg_default, _cfg)

    if config_file_path:
        # place provided config as highest user input
        if not config_file_path.is_file():
            raise FileNotFoundError(
                f"Given config path {config_file_path} does not exist"
            )
        config_user_paths.insert(0, config_file_path)

    user_options = {}
    for path in config_user_paths:
        if path.is_file():
            log.debug("Config read from '%s'", path)
            user_options = json.load(path.open())
            break
        path_old = path.with_suffix("")
        if path_old.is_file() and path.suffix:
            warn(
                f"Found {path_old} instead of a JSON file. Rename to {path}.",
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
    valid_extensions = [".md", ".txt", ".rtf", ".html", ".tex", ".markdown"]

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
                    if _file_path.suffix.lower() in valid_extensions:
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
    _checks: Optional[list[CheckSpec]] = None,
    _exe: Optional[Executor] = None,
) -> list[LintResult]:
    """
    Run the linter on the input file.

    Arguments:
    ---------
        content: content to lint
        config: lint configuration (mostly which checks to enable)
        source_name: file path
        allow_futures: skip the internal memoizer, has to be done later manually

    """
    if not isinstance(content, str):
        raise ValueError("linter expects a string as content")

    if not isinstance(config, dict):
        config = config_base.proselint_base
    if _checks is None:
        registry.discover()
        _checks = registry.get_all_enabled(config["checks"])

    memoizer_key = cache.calculate_key(content, _checks)
    # TODO: filename enables more elegant 2d-dict
    #       d[funcSig,fileSig] = (input_hash,result)
    #                        -> smaller, more efficient dicts

    with contextlib.suppress(KeyError):
        # early exit if result is already cached
        return [LintResult(**_e) for _e in cache[memoizer_key]]

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
        # NOTE: ThreadPoolExecutor is concurrent, but not multi-cpu
        # NOTE: .map() is build on .submit(), harder to use here, same speed
        futures = [
            _exe.submit(run_check, check, content, source_name)
            for check in _checks
        ]
        if allow_futures:
            cache.name_to_key[source_name] = memoizer_key
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
    return [LintResult(**_e) for _e in errors]


def fetch_results(
    futures: Union[list[Future], list[LintResult]],
    config: dict,
    source_name: str,
) -> list[LintResult]:
    """Fetch a result from futures (required for multiprocessing)."""
    if len(futures) > 0 and isinstance(futures[0], Future):
        _errors = [_e for _ft in futures for _e in _ft.result()]
        _errors = sorted(
            _errors[: config["max_errors"]],
            key=lambda e: (e["line"], e["column"]),
        )
        # store results in cache
        key = cache.name_to_key.get(source_name)
        cache[key] = _errors
        return [LintResult(**_e) for _e in _errors]
    return futures


def lint_path(
    paths: Union[Path, list[Path]],
    config: Optional[dict] = None,
) -> dict[Path, list[LintResult]]:
    """Lint a path with files or a specific file."""
    # Expand the list of directories and files.
    filepaths = extract_files(paths)

    if not isinstance(config, dict):
        config = config_base.proselint_base
    registry.discover()
    checks = registry.get_all_enabled(config["checks"])

    results = {}
    chars = 0

    if len(filepaths) == 0:
        # Use stdin if no paths were specified
        log.info("No path specified -> will read from <stdin>")
        content = sys.stdin.read()
        results[Path("<stdin>")] = lint(content, config=config, _checks=checks)
    else:
        # offer "outer" executor, to make multiprocessing more effective
        exe = ProcessPoolExecutor() if config["parallelize"] else None
        for file in filepaths:
            log.debug("Analyzing '%s'", file.name)
            try:
                with file.open(encoding="utf-8", errors="replace") as _fh:
                    content = _fh.read()
            except Exception:
                log.exception(
                    "[LintPath] Error opening '%s' -> will skip", file.name
                )
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

    log.debug("[Lint] finished pooling, will wait for results now")
    # fetch result from futures, if needed
    results = {
        _file: fetch_results(_errors, config, _file.as_posix())
        for _file, _errors in results.items()
    }
    cache.to_file()

    # TODO: transform linter into class
    # bad style ... but
    global last_char_count  # noqa: PLW0603
    last_char_count = chars
    return results


def convert_to_json(
    # FIXME: incorrect type (not enough args for dict, too many for list)
    results: Union[dict[list[str, LintResult]], list[LintResult]],
) -> str:
    """
    Convert the errors to JSON.

    Note: previously this used a list, now it uses a dictionary with the
    same format as `LintResult`.
    """
    if isinstance(results, dict):
        out = [_rl.to_json() for _res in results.values() for _rl in _res]
    else:
        # assumed list
        out = [_rl._asdict() for _rl in results]

    return json.dumps(
        {"status": "success", "data": {"errors": out}}, sort_keys=True
    )


def print_to_console(  # noqa: PLR0912
    results: Union[dict[str, list[LintResult]], list[LintResult]],
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
            "[OutputError] no list or dictionary provided "
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
                        # TODO: would be nice to supress "file:///"
                        # https://gist.github.com/egmontkob/eb114294efbcd5adb1944c9f3cb5feda
                        # could consider using as_posix for this?
                        _source = _file.absolute().as_uri()
                elif out_fmt == Output.compact:
                    _source = ""

                log.info(
                    "%s:%d:%d: %s %s",
                    _source,
                    _e.line,
                    _e.column,
                    _e.check,
                    _e.message,
                )
