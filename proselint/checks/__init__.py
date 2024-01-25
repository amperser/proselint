"""All the checks are organized into modules and placed in subdirectories.

This file contains:
- contained function-set called by linter
- _check-functions used by the checks

This submodule gets used for multiprocessing!
All custom code is contained in here.

"""

from __future__ import annotations

import functools
import importlib
import re
from enum import Enum
from typing import Callable
from typing import Optional
from typing import TypeAlias

from proselint.logger import log

ResultCheck: TypeAlias = tuple[int, int, str, str, Optional[str]]
# content: start_pos, end_pos, check_name, message, replacement)
# NOTE1: NewType() is too strict here
# NOTE2: py312 can use ->
# type ResultCheck = tuple[int, int, str, str, Optional[str]]


###############################################################################
# Check-Interface used by linter ##############################################
###############################################################################


def get_checks(options: dict) -> list[Callable[[str, str], list[ResultCheck]]]:
    """Extract the checks.
    Rule: fn-name must begin with "check", so check_xyz() is ok
    """
    # TODO: benchmark consecutive runs of this
    #       config should only translate once to check-list
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
        checks += [
            getattr(module, d) for d in dir(module) if re.match(r"^check", d)
        ]

    log.debug("Collected %d checks to run", len(checks))
    return checks


def run_checks(_check: Callable, _text: str, source: str = "") -> list:
    # TODO: frozenset is hashable (list without duplicates)
    # -> check-list, result-lists padding
    # -> some checks expect words in text and need something around it
    # -> this prevents edge-cases
    _text = f" \n{_text}\n "  # maybe not the fastest OP
    errors = []
    results = _check(_text)
    for result in results:
        (start, end, check_name, message, replacements) = result
        (line, column) = get_line_and_column(_text, start)
        if not is_quoted(start, _text):
            # note:
            #    - switch to 1based counting by adding +1
            #    - for line it cancels out with -1 from padding
            errors += [
                (
                    check_name,
                    message,
                    source,  # can't be Path, unless pickle changes
                    line,  # +1 -1, cancel out
                    column + 1,
                    start + 1,
                    end + 1,
                    end - start,
                    "warning",
                    replacements,
                ),
            ]
    return errors


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


def is_quoted(position: int, text: str) -> bool:
    """Determine if the position in the text falls within a quote."""

    def matching(quotemark1: str, quotemark2: str) -> bool:
        straight = "\"'"
        curly = "“”"
        return (quotemark1 in straight and quotemark2 in straight) or (
            quotemark1 in curly and quotemark2 in curly
        )

    def find_ranges(_text: str) -> list[tuple[int, int]]:
        # TODO: optimize, as it is top3 time-waster (of module-functions)
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

    def position_in_ranges(
        ranges: list[tuple[int, int]], _position: int
    ) -> bool:
        return any(start <= _position < end for start, end in ranges)

    return position_in_ranges(find_ranges(text), position)


###############################################################################
# The actual check-sub-functions used by the checks  ##########################
###############################################################################


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


def preferred_forms_check(  # noqa: PLR0913, PLR0917
    text: str,
    items: list,
    err: str,
    msg: str,
    ignore_case: bool = True,
    offset: int = 0,
) -> list[ResultCheck]:
    """Build a checker that suggests the preferred form."""
    flags = re.IGNORECASE if ignore_case else 0
    regex = r"[\W^]{}[\W$]"  # TODO: replace with enum below?

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
    # TODO: can we speed up str.format() ?
    #       fast-string? or do padding already in checks


# PADDINGS, add more if needed
class Pd(str, Enum):
    disabled = r"{}"
    # choose for checks with custom regex
    whitespace = r"\s{}\s"
    # -> req whitespace around (no punctuation!)
    sep_in_txt = r"(?:^|\W){}[\W$]"
    # req non-text character around
    # -> finds item as long it is surrounded by any non-word character:
    #       - whitespace
    #       - punctuation
    #       - newline ...


def existence_check(  # noqa: PLR0913, PLR0917
    text: str,
    re_items: list,
    err: str,
    msg: str,
    ignore_case: bool = True,
    string: bool = False,  # todo: why not default on?
    offset: int = 0,  # todo: some checks set this strangely
    padding: Pd = Pd.sep_in_txt,
    dotall: bool = False,
    excluded_topics: Optional[list] = None,
    exceptions=(),
) -> list[ResultCheck]:
    """Build a checker that prohibits certain words or phrases."""
    flags = 0
    if ignore_case:
        flags |= re.IGNORECASE
    if string:
        flags |= re.UNICODE
    if dotall:
        flags |= re.DOTALL

    errors: list[ResultCheck] = []

    # If the topic of the text is in the excluded list, return immediately.
    if excluded_topics:
        tps = topics(text)
        if any(t in excluded_topics for t in tps):
            return errors

    rx = "|".join(padding.format(_item) for _item in re_items)
    for m in re.finditer(rx, text, flags=flags):
        txt = m.group(0).strip()
        if any(re.search(exception, txt) for exception in exceptions):
            continue
        errors.append(
            (
                m.start() + 1 + offset,
                m.end() + offset,
                err,
                msg.format(txt),
                None,
            ),
        )
        # TODO: doesn't the padding alter the start+end?

    return errors


def simple_existence_check(
    text: str, pattern: str, err: str, msg: str, offset: int = 0
):
    """Build a checker for single patters.
    in comparison to existence_check:
        - does not work on lists
        - no padding
        - excluded topics or exceptions

        TODO: maybe add ignorecase
    """

    return [
        (inst.start() + offset, inst.end() + offset, err, msg, None)
        for inst in re.finditer(pattern, text)
    ]


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
