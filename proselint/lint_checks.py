from __future__ import annotations

import functools
import importlib
import logging
import re
from typing import Callable, Optional, TypeAlias

ResultCheck: TypeAlias = tuple[int, int, str, str, Optional[str]]
# content: start_pos, end_pos, check_name, message, replacement)
# note1: NewType() is too strict here
# note2: py312 can use -> type ResultCheck = tuple[int, int, str, str, Optional[str]]


def consistency_check(
    text: str,
    word_pairs: list,
    err: str,
    msg: str,
    offset: int = 0,
) -> list[ResultCheck]:
    """Build a consistency checker for the given word_pairs."""
    results = []

    for w in word_pairs:
        matches = [
            list(re.finditer(w[0], text)),
            list(re.finditer(w[1], text)),
        ]

        if len(matches[0]) > 0 and len(matches[1]) > 0:
            idx_minority = len(matches[0]) > len(matches[1])

            results += [
                (
                    m.start() + offset,
                    m.end() + offset,
                    err,
                    msg.format(w[not idx_minority], m.group(0)),
                    w[not idx_minority],
                )
                for m in matches[idx_minority]
            ]

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
    flags = re.IGNORECASE if ignore_case else 0
    regex = r"[\W^]{}[\W$]"

    return [
        (
            m.start() + 1 + offset,
            m.end() + offset,
            err,
            msg.format(item[0], m.group(0).strip()),
            item[0],
        )
        for item in items
        for r in item[1]
        for m in re.finditer(regex.format(r), text, flags=flags)
    ]


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
    join: bool = False,  # TODO: some checker use this, meaning unknown
) -> list[ResultCheck]:
    """Build a checker that prohibits certain words or phrases."""
    flags = 0
    if ignore_case:
        flags |= re.IGNORECASE
    if string:
        flags |= re.UNICODE
    if dotall:
        flags |= re.DOTALL

    regex = r"(?:^|\W){}[\W$]" if require_padding else r"{}"

    errors: list[ResultCheck] = []

    # If the topic of the text is in the excluded list, return immediately.
    if excluded_topics:
        tps = topics(text)
        if any(t in excluded_topics for t in tps):
            return errors

    rx = "|".join(regex.format(_item) for _item in items)
    for m in re.finditer(rx, text, flags=flags):
        txt = m.group(0).strip()
        if any(re.search(exception, txt) for exception in exceptions):
            continue
        errors.append(
            (m.start() + 1 + offset, m.end() + offset, err, msg.format(txt), None),
        )

    return errors


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
    ts = [detector(text) for detector in detectors]
    return [t[0] for t in ts if t[1] > 0.95]


def context(text, position, level="paragraph"):
    """Get sentence or paragraph that surrounds the given position."""
    if level == "sentence":
        pass
    elif level == "paragraph":
        pass

    return ""


def get_checks(options: dict) -> list[Callable[[str, str], list[ResultCheck]]]:
    """Extract the checks."""
    checks = []
    check_names = [key for (key, val) in options["checks"].items() if val]

    for check_name in check_names:
        try:
            module = importlib.import_module("." + check_name, "proselint.checks")
        except ModuleNotFoundError:
            logging.exception(
                "requested config-flag '%s' not found in proselint.checks", check_name,
            )
            continue
        checks += [getattr(module, d) for d in dir(module) if re.match("check", d)]

    return checks


###############################################################################
# Wrapper #####################################################################
###############################################################################


def limit_results(value: int):
    """Decorate a check to truncate error output to a specified limit."""

    def wrapper(fn):
        @functools.wraps(fn)
        def wrapped(*args, **kwargs):
            return _truncate_errors(fn(*args, **kwargs), value)

        return wrapped

    return wrapper


def _truncate_errors(
    errors: list[ResultCheck],
    limit: int,
) -> list[ResultCheck]:
    """If limit was specified, truncate the list of errors.

    Give the total number of times that the error was found elsewhere.
    """
    if len(errors) > limit:
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
            _len = 0  # neutral element
            if "text" in kwargs:
                _len = len(kwargs["text"])
            elif len(args) > 0:
                _len = len(args[0])
            return _threshold_check(fn(*args, **kwargs), threshold, _len)

        return wrapper

    return wrapped


def _threshold_check(errors: list, threshold: float, length: int):
    """Check that returns an error if the PPM threshold is surpassed."""
    if length > 0:
        errcount = len(errors)
        # statistics only work with big numbers, so add some workarounds
        if errcount < 2:
            return []
        length = max(length, 1000)

        ppm = (errcount / length) * 1e6
        if ppm > threshold:
            return [errors[0]]
    return []
