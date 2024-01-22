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
# NOTE2: py312 can use -> type ResultCheck = tuple[int, int, str, str, Optional[str]]


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
        checks += [getattr(module, d) for d in dir(module) if re.match(r"^check", d)]

    log.debug("Collected %d checks to run", len(checks))
    return checks


def run_check(_check: Callable, _text: str, source: str = "") -> list[dict]:
    errors = []
    results = _check(_text)
    for result in results:
        (start, end, check_name, message, replacements) = result
        (line, column) = get_line_and_column(_text, start)
        if not is_quoted(start, _text):
            # note:
            #    - switch to 1based counting -> +1 for line, column, start, end
            #    - padding was added to text -> -1 for all except column
            #    - +1 -1 cancel out
            errors += [
                {
                    "check": check_name,
                    "message": message,
                    "source": source,
                    "line": line,
                    "column": column + 1,
                    "start": start,
                    "end": end,
                    "extent": end - start,
                    "severity": "warning",
                    "replacements": replacements,
                }
            ]
    return errors


def get_line_and_column(text, position):
    """Return the line number and column of a position in a string.

    # could also just:
    _t=text[:pos].splitlines(True)
    line_no=len(_t)
    column=len(_t[-1])
    # todo: test this fn
     TODO: like LUT in in_quoted(), it shows that the text should be pre-analyzed
           just use a list with line-start-positions, store all in text_meta: dict
    """
    line_start_pos = 0
    line_no = 0
    for line in text.splitlines(True):
        if (line_start_pos + len(line)) >= position:
            break
        line_start_pos += len(line)
        line_no += 1
    return line_no, position - line_start_pos


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

    def position_in_ranges(ranges: list[tuple[int, int]], _position: int) -> bool:
        return any(start <= _position < end for start, end in ranges)

    return position_in_ranges(find_ranges(text), position)


###############################################################################
# The actual check-sub-functions used by the checks  ##########################
###############################################################################


# PADDINGS, add more if needed
# Notes:
# - () make it safe to put '|'.join(strings) inside (safe for str with whitespace)
# - TODO: if data is precompiled and
#           - len(strings)==0 -> skip
#           - len(strings)==1 -> pad.format("string")
#           - len(strings)>1 -> pad.format("(" + "|".join(strings) + ")")
# NOTE: v0.16 turned join-format inside-out for less computation
# example orig: (?:^|\W)w1[\W$]|(?:^|\W)w2[\W$]|(?:^|\W)w3[\W$]
# example new:  (?:^|\W)(w1|w2|w3)[\W$]
# second one runs much more efficient
class Pd(str, Enum):
    disabled = r"{}"
    # choose for checks with custom regex
    safe_join = r"(?:{})"
    # can be filled with w1|w2|w3|...

    whitespace = r"\s{}\s"
    # -> req whitespace around (no punctuation!)

    # sep_in_txt = r"[\W^]{}[\W$]"  # prev. version r"(?:^|\W){}[\W$]"
    sep_in_txt = r"(?:^|\W){}[\W$]"
    # req non-text character around
    # -> finds item as long it is surrounded by any non-word character:
    #       - whitespace
    #       - punctuation
    #       - newline ...
    # TODO: some cases can use faster non-word-boundary \B
    words_in_txt = r"\b{}\b"
    # much faster version of sep_in_txt, but a bit unsafer / specialized, as
    # non A-z - characters at start & end of search-string don't match!


def consistency_check(
    text: str,
    word_pairs: list,
    err: str,
    msg: str,
    ignore_case: bool = True,
    offset: tuple[int, int] = (0, 0),
) -> list[ResultCheck]:
    """Build a consistency checker for the given word_pairs.
    Note: offset-usage corrects for pre-added padding-chars
    """
    flags = re.IGNORECASE if ignore_case else 0
    results = []

    for w in word_pairs:
        matches = [
            list(re.finditer(w[0], text, flags)),
            list(re.finditer(w[1], text, flags)),
        ]

        if len(matches[0]) > 0 and len(matches[1]) > 0:
            idx_minority = len(matches[0]) > len(matches[1])

            results += [
                (
                    m.start() + offset[0],
                    m.end() + offset[1],
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
    offset: tuple[int, int] = (0, 0),
    padding: str = Pd.words_in_txt,
) -> list[ResultCheck]:
    """Build a checker that suggests the preferred form.
    Note: offset-usage corrects for pre-added padding-chars
    """
    flags = re.IGNORECASE if ignore_case else 0
    if padding not in {Pd.disabled, Pd.safe_join, Pd.words_in_txt}:
        # Pd.whitespace & Pd.sep_in_text each add 1 char before and after
        offset = (offset[0] + 1, offset[1] - 1)

    return [
        (
            m.start() + offset[0],
            m.end() + offset[1],
            err,
            msg.format(item[0], m.group(0).strip()),
            item[0],
        )
        for item in items
        for m in re.finditer(
            padding.format(
                Pd.safe_join.format("|".join(item[1]))
                if len(item[1]) > 1
                else item[1][0]
            ),
            text,
            flags=flags,
        )
    ]
    # TODO: can we speed up str.format() ?
    #       fast-string? or do padding already in checks -> see test below
    #       just optimizing the slowest test improved performance by 5%
    #       alternative: checks() just return config-data to use (can be pickled)
    #                    it's possible to compile regex and do 'regex.finditer(text)'


def preferred_forms_check2_pre(
    items: list, ignore_case: bool = True, padding: str = Pd.words_in_txt
) -> list:
    flags = re.IGNORECASE if ignore_case else 0
    return [
        [
            item[0],
            re.compile(
                padding.format(
                    Pd.safe_join.format("|".join(item[1]))
                    if len(item[1]) > 1
                    else item[1][0]
                ),
                flags=flags,
            ),
        ]
        for item in items
    ]


def preferred_forms_check2_main(
    text: str,
    items: list,
    err: str,
    msg: str,
) -> list[ResultCheck]:
    """Build a checker that suggests the preferred form.
    Note: offset-usage corrects for pre-added padding-chars
    """
    return [
        (
            m.start(),  # todo: offset is currently not adapted to pattern
            m.end(),
            err,
            msg.format(item[0], m.group(0).strip()),
            item[0],
        )
        for item in items
        for m in item[1].finditer(text)
    ]


def existence_check(  # noqa: PLR0913, PLR0917
    text: str,
    re_items: list,
    err: str,
    msg: str,
    ignore_case: bool = True,
    string: bool = False,  # todo: why not default on?
    offset: tuple[int, int] = (0, 0),
    padding: Pd = Pd.words_in_txt,
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

    if padding not in {Pd.disabled, Pd.safe_join, Pd.words_in_txt}:
        # Pd.whitespace & Pd.sep_in_text each add 1 char before and after
        offset = (offset[0] + 1, offset[1] - 1)

    if len(re_items) > 1:
        re_items = Pd.safe_join.value.format("|".join(re_items))
    else:
        re_items = re_items[0]
    rx = padding.format(re_items)
    for m in re.finditer(rx, text, flags=flags):
        txt = m.group(0).strip()
        if any(re.search(exception, txt, flags=flags) for exception in exceptions):
            continue
        errors.append(
            (m.start() + offset[0], m.end() + offset[1], err, msg.format(txt), None),
        )
        # todo: group(1) offers word already without padding (when turned inside out)
    return errors


def simple_existence_check(  # noqa: PLR0913, PLR0917
    text: str,
    pattern: str,
    err: str,
    msg: str,
    ignore_case: bool = True,
    unicode: bool = True,
    exceptions=(),
) -> list[ResultCheck]:
    """Build a checker for single patters.
    in comparison to existence_check:
        - does not work on lists
        - no padding
        - excluded topics
        - offset

    """
    flags = 0
    if unicode:
        flags |= re.UNICODE
    if ignore_case:
        flags |= re.IGNORECASE
    return [
        (
            _m.start(),
            _m.end(),
            err,
            msg.format(_m.group(0).strip()),
            None,
        )
        for _m in re.finditer(pattern, text, flags=flags)
        if not any(
            re.search(exception, _m.group(0), flags=flags) for exception in exceptions
        )
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
    num_keywords = sum(word in text for word in keywords)  # TODO: regex
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
# Experimental ################################################################
###############################################################################


def detect_language(text: str) -> str:
    # TODO: add language to text.metadata, some checks are independent from language
    lang_regex = {
        # latin script, sorted by number of native speakers
        # https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers
        "es": Pd.words_in_txt.format("(y|es|la|el)"),
        "en": Pd.words_in_txt.format("(and|is|the)"),
        "pt": Pd.words_in_txt.format("(e|é|o|a)"),
        "fr": Pd.words_in_txt.format("(et|est|la|le)"),
        "de": Pd.words_in_txt.format("(und|ist|der|die|das)"),
    }
    count_max = 0
    lang_max = "en"
    for _lang, _regex in lang_regex.items():
        _count = len(re.findall(_regex, text))
        if _count > count_max:
            lang_max = _lang
            count_max = _count
    return lang_max


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
