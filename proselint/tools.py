"""General-purpose tools shared across linting checks."""

from __future__ import annotations

import contextlib
import copy
import functools
import hashlib
import importlib
import json
import pickle
import re
import shutil
import sys
import traceback
from datetime import datetime
from pathlib import Path
from typing import IO, Callable, Optional, TypeAlias, Union
from warnings import showwarning as warn

from typing_extensions import Self

from . import config
from .logger import log
from .paths import (
    cache_user_path,
    config_global_path,
    config_user_paths,
    proselint_path,
)

ResultCheck: TypeAlias = tuple[int, int, str, str, Optional[str]]
# content: start_pos, end_pos, check_name, message, replacement)
ResultLint: TypeAlias = tuple[str, str, int, int, int, int, int, str, str]
# content: check_name, message, line, column, start, end, length, type, replacement
# note1: NewType() is too strict here
# note2: py312 can use -> type ResultCheck = tuple[int, int, str, str, Optional[str]]

###############################################################################
############################# Caching #########################################
###############################################################################


class Cache:
    save_path = cache_user_path / "cache.pickle"

    def __init__(self) -> None:
        self.data: dict[str, list[ResultCheck]] = {}
        self.age: dict[str, datetime] = {}
        self.ts_now: datetime = datetime.now()

    def __exit__(self) -> None:
        """Close previously opened cache shelves."""
        self.to_file()
        self.data.clear()

    def __del__(self):
        self.to_file()

    def to_file(self) -> None:
        if len(self.data) < 1:
            return
        if not cache_user_path.is_dir():
            cache_user_path.mkdir(parents=True)
        # TODO: sort out aged entries
        with self.save_path.open("wb", buffering=-1) as fd:
            pickle.dump(
                [self.data, self.age],
                fd,
                fix_imports=False,
                protocol=pickle.HIGHEST_PROTOCOL,
            )
        log.debug(" -> stored cache")

    @classmethod
    def from_file(cls) -> Self:
        # TODO: this should catch exceptions and switch to a fresh instance on fail
        instance = cls()
        if cls.save_path.exists():
            with cls.save_path.open("rb", buffering=-1) as fd:
                data = pickle.load(fd, fix_imports=False)  # noqa: S301
            instance.data = data[0]
            instance.age = data[1]
            log.debug(" -> found & restored cache")
        return instance

    def clear(self) -> None:
        """Delete the contents of the cache."""
        log.debug("Deleting the cache...")
        with contextlib.suppress(OSError):
            shutil.rmtree(cache_user_path)
        self.data.clear()
        self.age.clear()


cache = Cache.from_file()


def memoize(  # new
    fn: Callable,
) -> Callable:
    """Cache results of computations on disk.
    Note: fn-signature gets changed! bad design, but good speed-improvement
        -> wrapped_fn(text: str) -> list[Results]
        -> called_fn(text: str, text_hash: str) -> list[Results]
    TODO: decide what to do: extend args of wrapped fn, feed dict into fn?
    """
    _filename = f"{fn.__module__}.{fn.__name__}"

    @functools.wraps(fn)
    def wrapped(text: str, hash_text: str):
        key = _filename + hash_text

        try:
            return cache.data[key]
        except KeyError:
            value = fn(text)
            cache.data[key] = value
            # cache.age[key] = cache.
            return value
        except TypeError:
            log.error(
                "Warning: could not disk cache call to %s;"
                "it probably has unhashable args. Error: %s",
                _filename,
                traceback.format_exc(),
            )
            return fn(text)

    return wrapped


###############################################################################
############################# Config ##########################################
###############################################################################


def deepmerge_dicts(
    base: dict,
    overrides: dict,
) -> dict:  # TODO: this can be faster, we can just add dicts
    """Deep merge dictionaries, second dict will take priority."""
    result = copy.deepcopy(base)

    for key, value in overrides.items():
        if isinstance(value, dict):
            result[key] = deepmerge_dicts(result.get(key) or {}, value)
        else:
            result[key] = value

    return result


def load_options(
    config_file_path: Optional[Path] = None,
) -> dict:
    """Read various proselintrc files, allowing user overrides."""
    cfg_default = config.default

    if config_global_path.is_file():
        log.debug("Config read from global '%s' (as base)", config_global_path)
        _cfg = json.load(config_global_path.open())
        cfg_default = deepmerge_dicts(cfg_default, _cfg)

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

    return deepmerge_dicts(cfg_default, user_options)


###############################################################################
############################# Linting #########################################
###############################################################################


def get_checks(options: dict) -> list[Callable[[str, str], list[ResultCheck]]]:
    """Extract the checks."""
    sys.path.append(proselint_path.as_posix())
    checks = []
    check_names = [key for (key, val) in options["checks"].items() if val]

    for check_name in check_names:
        module = importlib.import_module("." + check_name, "proselint.checks")
        for d in dir(module):
            if re.match("check", d):
                checks.append(getattr(module, d))

    return checks


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
        cfg = config.default

    # Get the checks.
    checks = get_checks(cfg)
    _hash = hashlib.md5(_text.encode("utf-8")).hexdigest()
    # _args = {"hash_text": _hash, "text": text}

    # Apply all the checks.
    errors = []
    for check in checks:
        # TODO: can be run this in parallel
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


def assert_error(text: str, check, n=1):
    """Assert that text has n errors of type check."""
    assert_error.description = f"No {check} error for '{text}'"
    assert check in [error[0] for error in lint(text)]


###############################################################################
############################# Checks ##########################################
###############################################################################
# TODO: refactor into lint_checks, lint_main, lint_cache, ...


def consistency_check(
    text: str,
    word_pairs: list,
    err: str,
    msg: str,
    offset: int = 0,
) -> list[ResultCheck]:
    """Build a consistency checker for the given word_pairs."""
    results = []

    msg = " ".join(msg.split())

    for w in word_pairs:
        matches = [
            list(re.finditer(w[0], text)),
            list(re.finditer(w[1], text)),
        ]

        if len(matches[0]) > 0 and len(matches[1]) > 0:
            idx_minority = len(matches[0]) > len(matches[1])

            for m in matches[idx_minority]:
                results.append(
                    (
                        m.start() + offset,
                        m.end() + offset,
                        err,
                        msg.format(w[not idx_minority], m.group(0)),
                        w[not idx_minority],
                    ),
                )

    return results


def preferred_forms_check(
    text: str,
    items: list,
    err: str,
    msg: str,
    ignore_case: bool = True,
    offset: int = 0,
) -> list[ResultCheck]:
    """Build a checker that suggests the preferred form."""
    # TODO: optimize, as it is top1 time-waster (of user-functions)
    if ignore_case:
        flags = re.IGNORECASE
    else:
        flags = 0

    msg = " ".join(msg.split())

    results = []
    regex = r"[\W^]{}[\W$]"
    for item in items:
        for r in item[1]:
            for m in re.finditer(regex.format(r), text, flags=flags):
                txt = m.group(0).strip()
                results.append(
                    (
                        m.start() + 1 + offset,
                        m.end() + offset,
                        err,
                        msg.format(item[0], txt),
                        item[0],
                    ),
                )

    return results


def existence_check(
    text: str,
    items: list,
    err: str,
    msg: str,
    ignore_case: bool = True,
    string: bool = False,
    offset: int = 0,
    require_padding: bool = True,
    dotall: bool = False,
    excluded_topics: Optional[list] = None,
    exceptions=(),
    join: bool = False,
) -> list[ResultCheck]:
    """Build a checker that prohibits certain words or phrases."""
    # TODO: optimize, as it is top2 time-waster (of user-functions)
    msg = " ".join(msg.split())

    flags = 0
    if ignore_case:
        flags |= re.IGNORECASE
    if string:
        flags |= re.UNICODE
    if dotall:
        flags |= re.DOTALL

    if require_padding:
        regex = r"(?:^|\W){}[\W$]"
    else:
        regex = r"{}"

    errors: list[ResultCheck] = []

    # If the topic of the text is in the excluded list, return immediately.
    if excluded_topics:
        tps = topics(text)
        if any([t in excluded_topics for t in tps]):
            return errors

    rx = "|".join(regex.format(w) for w in items)
    for m in re.finditer(rx, text, flags=flags):
        txt = m.group(0).strip()
        if any([re.search(exception, txt) for exception in exceptions]):
            continue
        errors.append(
            (m.start() + 1 + offset, m.end() + offset, err, msg.format(txt), None),
        )

    return errors


def max_errors(limit: int):  # TODO: should be called limit_returned_items()
    """Decorate a check to truncate error output to a specified limit."""

    def wrapper(fn):
        @functools.wraps(fn)
        def wrapped(*args, **kwargs):
            return truncate_errors(fn(*args, **kwargs), limit)

        return wrapped

    return wrapper


def truncate_errors(
    errors: list[ResultCheck],
    limit: Optional[int] = None,
) -> list[ResultCheck]:
    """If limit was specified, truncate the list of errors.

    Give the total number of times that the error was found elsewhere.
    """
    if limit and len(errors) > limit:
        start1, end1, err1, msg1, replacements = errors[0]

        if len(errors) == limit + 1:
            msg1 += " Found once elsewhere."
        else:
            msg1 += f" Found {len(errors)} times elsewhere."

        errors = [(start1, end1, err1, msg1, replacements)] + errors[1:limit]

    return errors


def ppm_threshold(threshold: float):
    """Decorate a check to error if the PPM threshold is surpassed."""

    def wrapped(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            return threshold_check(fn(*args, **kwargs), threshold, len(args[0]))

        return wrapper

    return wrapped


def threshold_check(errors: list, threshold: float, length: int):
    """Check that returns an error if the PPM threshold is surpassed."""
    if length > 0:
        errcount = len(errors)
        ppm = (errcount / length) * 1e6

        if ppm >= threshold and errcount >= 1:
            return [errors[0]]
    return []


def is_quoted(position: int, text: str) -> bool:
    """Determine if the position in the text falls within a quote."""

    def matching(quotemark1: str, quotemark2: str) -> bool:
        straight = "\"'"
        curly = "“”"
        if quotemark1 in straight and quotemark2 in straight:
            return True
        if quotemark1 in curly and quotemark2 in curly:
            return True
        else:
            return False

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


def detector_50_Cent(text: str) -> tuple[str, float]:
    """Determine whether 50 Cent is a topic."""
    keywords = [
        "50 Cent",
        "rap",
        "hip hop",
        "Curtis James Jackson III",
        "Curtis Jackson",
        "Eminem",
        "Dre",
        "Get Rich or Die Tryin'",
        "G-Unit",
        "Street King Immortal",
        "In da Club",
        "Interscope",
    ]
    num_keywords = sum(word in text for word in keywords)
    return "50 Cent", float(num_keywords > 2)


def topics(text: str) -> list[str]:
    """Return a list of topics."""
    detectors = [
        detector_50_Cent,
    ]
    ts = []
    for detector in detectors:
        ts.append(detector(text))

    return [t[0] for t in ts if t[1] > 0.95]


def context(text, position, level="paragraph"):
    """Get sentence or paragraph that surrounds the given position."""
    if level == "sentence":
        pass
    elif level == "paragraph":
        pass

    return ""
