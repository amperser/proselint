"""
All the checks are organized into modules and placed in subdirectories.

This file contains:
- a function set used by the linter
- utility functions for checks

This submodule is thread safe.

"""

from __future__ import annotations

import functools
import importlib
import pkgutil
import re
import string
from enum import Enum
from typing import Callable, NamedTuple, Optional, Union

from proselint.logger import log


class CheckResult(NamedTuple):
    """A check result."""

    start_pos: int
    end_pos: int
    check: str
    message: str
    replacements: Optional[str]


###############################################################################
# Check-Interface used by linter ##############################################
###############################################################################


# Regex-PADDINGS
# - these can be handed to the check-functions
# - most efficient is `words_in_txt` but it does not work
#   for all use-cases
# - test with tools like https://regex101.com/ and optimize for low step-count
class Pd(str, Enum):
    """Helper for padding."""

    disabled = r"{}"
    # choose for checks with custom regex

    safe_join = r"(?:{})"
    # can be filled with w1|w2|w3|...

    whitespace = r"\s{}\s"
    # req whitespace around (no punctuation!)

    sep_in_txt = r"(?:^|\W){}[\W$]"
    # finds item as long it is surrounded by any non-word character:
    # whitespace, punctuation, newline ...

    words_in_txt = r"\b{}\b"
    # much faster version of sep_in_txt, but more specialized, as
    # non A-z - characters at start & end of search-string don't match!
    # TODO: some cases can use faster non-word-boundary \B


class Consistency(NamedTuple):
    word_pairs: list[tuple[str, str]]


class PreferredForms(NamedTuple):
    items: dict[str, str]
    padding: Pd = Pd.words_in_txt


class PreferredFormsSimple(NamedTuple):
    items: dict[str, str]
    padding: Pd = Pd.words_in_txt


class Existence(NamedTuple):
    items: list[str]
    unicode: bool = False
    padding: Pd = Pd.words_in_txt
    dotall: bool = False
    exceptions: tuple[str, ...] = ()


class ExistenceSimple(NamedTuple):
    pattern: str
    unicode: bool = True
    exceptions: tuple[str, ...] = ()


class ReverseExistence(NamedTuple):
    allowed: list[str]


CheckFn = Callable[[str, "CheckSpec"], list[CheckResult]]


class CheckFlags(NamedTuple):
    """
    A collection of check flags.

    Currently, this supports:
    - `limit_results`: A limit that truncates the check results.
    - `ppm_threshold`: A threshold check comparing the number of results
      against the text length.
    """

    # TODO: it would be vastly more efficient if these could interrupt instead
    # of postprocessing - that is, halt searching if the limits are surpassed
    # instead of truncating / alerting if conditions are met after the fact.
    limit_results: int = 0
    ppm_threshold: int = 0


class CheckSpec(NamedTuple):
    type: Union[
        Consistency,
        PreferredForms,
        PreferredFormsSimple,
        Existence,
        ExistenceSimple,
        ReverseExistence,
        CheckFn,
    ]
    path: str
    msg: str
    flags: CheckFlags = CheckFlags()
    ignore_case: bool = True
    offset: tuple[int, int] = (0, 0)

    @property
    def path_segments(self) -> list[str]:
        return self.path.split(".")

    def matches_partial(self, partial: str) -> bool:
        partial_segments = partial.split(".")
        if len(partial_segments) > len(self.path_segments):
            return False
        # NOTE: this can be replaced with itertools.pairwise for versions >=3.10
        return all(
            self.path_segments[i] == partial_segments[i]
            for i in range(len(partial_segments))
        )

    def dispatch_with_flags(self, text: str) -> list[CheckResult]:
        results = self.dispatch(text)
        if self.flags.ppm_threshold > 0:
            results = _threshold_check(
                results, self.flags.ppm_threshold, len(text)
            )
        if self.flags.limit_results > 0:
            results = _truncate_errors(results, self.flags.limit_results)
        return results

    # TODO: attempt to simplify this
    def dispatch(self, text: str) -> list[CheckResult]:  # noqa: PLR0911
        if isinstance(self.type, Consistency):
            return consistency_check(
                text,
                self.type.word_pairs,
                self.path,
                self.msg,
                self.ignore_case,
                self.offset,
            )
        if isinstance(self.type, PreferredForms):
            return preferred_forms_check_regex(
                text,
                self.type.items,
                self.path,
                self.msg,
                self.ignore_case,
                self.offset,
                self.type.padding,
            )
        if isinstance(self.type, PreferredFormsSimple):
            return preferred_forms_check_opti(
                text,
                self.type.items,
                self.path,
                self.msg,
                self.ignore_case,
                self.offset,
                self.type.padding,
            )
        if isinstance(self.type, Existence):
            return existence_check(
                text,
                self.type.items,
                self.path,
                self.msg,
                self.ignore_case,
                self.type.unicode,
                self.offset,
                self.type.padding,
                self.type.dotall,
                exceptions=self.type.exceptions,
            )
        if isinstance(self.type, ExistenceSimple):
            return existence_check_simple(
                text,
                self.type.pattern,
                self.path,
                self.msg,
                self.ignore_case,
                self.type.unicode,
                self.type.exceptions,
            )
        if isinstance(self.type, ReverseExistence):
            return reverse_existence_check(
                text,
                self.type.allowed,
                self.path,
                self.msg,
                self.ignore_case,
                self.offset,
            )
        if isinstance(self.type, Callable):
            return self.type(text, self)
        raise ValueError(
            "Check type must be valid, found %s (type %s)",
            self.type,
            type(self.type),
        )


class CheckRegistry:
    _checks: list[CheckSpec]
    enabled_checks: Optional[dict[str, bool]]
    start: Optional[float]

    def __init__(self) -> None:
        self._checks = []
        self.enabled_checks = None
        self.start = None

    def register(self, check: CheckSpec) -> None:
        self._checks.append(check)

    def register_many(self, checks: tuple[CheckSpec, ...]) -> None:
        self._checks.extend(checks)

    def discover(self) -> None:
        # TODO: add a search for plugins and user defined checks
        for info in pkgutil.iter_modules(__path__, "."):
            if info.name.startswith("._"):
                continue
            try:
                module = importlib.import_module(info.name, "proselint.checks")
                self.register_many(module.__register__)
            except Exception:
                log.exception(
                    "Error encountered while registering module %s.",
                    info.name,
                )
                continue
            log.debug("Registered from module %s.", module.__name__)

    @property
    def checks(self) -> list[CheckSpec]:
        log.debug("Collected %d checks to run.", len(self._checks))
        return self._checks

    def get_all_enabled(
        self, enabled: Optional[dict[str, bool]] = None
    ) -> list[CheckSpec]:
        if enabled is not None:
            self.enabled_checks = enabled
        if self.enabled_checks is None:
            return []

        enabled_checks = []
        skipped_checks = []
        for key, key_enabled in self.enabled_checks.items():
            if key_enabled:
                enabled_checks.append(key)
            else:
                skipped_checks.append(key)

        # TODO: review potential optimizations for this
        filtered_enabled = [
            x
            for x in self.checks
            if not any(x.matches_partial(key) for key in skipped_checks)
            and any(
                x.path == key or x.matches_partial(key)
                for key in enabled_checks
            )
        ]
        log.debug("Collected %d enabled checks.", len(filtered_enabled))
        return filtered_enabled


registry = CheckRegistry()


def run_check(_check: CheckSpec, _text: str, source: str = "") -> list[dict]:
    """Run a check on the source."""
    errors = []
    results: list[CheckResult] = _check.dispatch_with_flags(_text)
    for _r in results:
        (line, column) = get_line_and_column(_text, _r.start_pos)
        if not is_quoted(_r.start_pos, _text):
            # NOTE:
            #    - switch to 1based counting -> +1 for line, column, start, end
            #    - padding was added to text -> -1 for all except column
            #    - +1 -1 cancel out
            errors += [
                {
                    "check": _r.check,
                    "message": _r.message,
                    "source": source,
                    "line": line,
                    "column": column + 1,
                    "start": _r.start_pos,
                    "end": _r.end_pos,
                    "extent": _r.end_pos - _r.start_pos,
                    "severity": "warning",
                    "replacements": _r.replacements,
                }
            ]
    return errors


def get_line_and_column(text: str, position: int) -> tuple[int, int]:
    """
    Return the line number and column of a position in a string.

    implementation: ~10x faster than v1, but still splits
    NOTE: could be further optimized, but it's not worth it atm
          pre-analyze with lookup-table, list with line-start-positions
    """
    # TODO: test this fn
    # NOTE: fixes a special case where IndexError would occur for position = 0
    if position == 0:
        return (0, 0)
    _t = text[:position].splitlines(True)
    return (len(_t) - 1, len(_t[-1]))


def check_matching_quotes(chars: tuple[str, str]) -> bool:
    """Check if a pair of quotes match."""
    straight = "\"'"
    curly = "“”"
    return (chars[0] in straight and chars[0] == chars[1]) or (
        chars[0] in curly and chars[1] in curly and chars[0] != chars[1]
    )


@functools.lru_cache
def find_quoted_ranges(text: str) -> list[tuple[int, int]]:
    """Find the range of a quote pair."""
    # NOTE: regex implementation is ~3x faster than previously, but this could
    # still be optimized further.
    return find_spans(text, r"[\"'“”]", check_matching_quotes)


# TODO: allow this to return unmatched spans, to provide a way to check for
# entries that are unmatched, like in misc.braces
def find_spans(
    text: str, regex: str, predicate: Callable[[tuple[str, str]], bool]
) -> list[tuple[int, int]]:
    """Find spans of matching characters (e.g. braces, quotes)."""
    active: list[tuple[str, int]] = [
        (_m.group(0), _m.start()) for _m in re.finditer(regex, text)
    ]
    prev: list[tuple[str, int]] = []
    spans: list[tuple[int, int]] = []
    for char, span_end in active:
        for potential, span_start in reversed(prev):
            if predicate((char, potential)):
                prev.pop()
                spans.append((span_start, span_end))
                break
        else:
            prev.append((char, span_end))
    return spans


def is_quoted(position: int, text: str) -> bool:
    """Determine if the position in the text falls within a quote."""
    ranges = find_quoted_ranges(text)
    return any(start <= position < end for start, end in ranges)


###############################################################################
# The actual check-sub-functions used by the checks  ##########################
###############################################################################


def consistency_check(  # noqa: PLR0913, PLR0917
    text: str,
    word_pairs: list,
    err: str,
    msg: str,
    ignore_case: bool = True,
    offset: tuple[int, int] = (0, 0),
) -> list[CheckResult]:
    """
    Build a consistency checker for the given `word_pairs`.

    Note: offset-usage corrects for pre-added padding-chars
    """
    flags = re.IGNORECASE if ignore_case else 0
    results: list[CheckResult] = []

    for w in word_pairs:
        matches = [
            list(re.finditer(w[0], text, flags)),
            list(re.finditer(w[1], text, flags)),
        ]

        if len(matches[0]) > 0 and len(matches[1]) > 0:
            idx_minority = len(matches[0]) > len(matches[1])

            results += [
                CheckResult(
                    start_pos=m.start() + offset[0],
                    end_pos=m.end() + offset[1],
                    check=err,
                    message=msg.format(w[not idx_minority], m.group(0)),
                    replacements=w[not idx_minority],
                )
                for m in matches[idx_minority]
            ]

    return results


def preferred_forms_check_regex(  # noqa: PLR0913, PLR0917
    text: str,
    items: dict[str, str],
    err: str,
    msg: str,
    ignore_case: bool = True,
    offset: tuple[int, int] = (0, 0),
    padding: str = Pd.words_in_txt,
) -> list[CheckResult]:
    """
    Build a checker that suggests the preferred form.

    Note: offset-usage corrects for manually added padding-chars
    """
    flags = re.IGNORECASE if ignore_case else 0
    if padding not in {Pd.disabled, Pd.safe_join, Pd.words_in_txt}:
        # Pd.whitespace & Pd.sep_in_text each add 1 char before and after
        offset = (offset[0] + 1, offset[1] - 1)

    return [
        CheckResult(
            start_pos=m.start() + offset[0],
            end_pos=m.end() + offset[1],
            check=err,
            message=msg.format(_repl, m.group(0).strip()),
            replacements=_repl,
        )
        for _orig, _repl in items.items()
        for m in re.finditer(
            padding.format(_orig),
            text,
            flags=flags,
        )
    ]


# TODO: test will all provided entries and check if not-None replacement gets
# returned
def preferred_forms_check_opti(  # noqa: PLR0913, PLR0917
    text: str,
    items: dict[str, str],
    err: str,
    msg: str,
    ignore_case: bool = True,
    offset: tuple[int, int] = (0, 0),
    padding: str = Pd.words_in_txt,
) -> list[CheckResult]:
    """
    Build a checker that suggests the preferred form.

    The provided items can't contain active regex
    -> use normal preferred_forms_check() for that

    Note: offset-usage corrects for manually added padding-chars
    """
    if ignore_case:
        flags = re.IGNORECASE
        items = {key.lower(): value for key, value in items.items()}
    else:
        flags = 0

    if padding not in {Pd.disabled, Pd.safe_join, Pd.words_in_txt}:
        # Pd.whitespace & Pd.sep_in_text each add 1 char before and after
        offset = (offset[0] + 1, offset[1] - 1)

    if len(items) > 1:
        rx = Pd.safe_join.format("|".join(items.keys()))
    else:
        rx = next(iter(items))
    rx = padding.format(rx)

    results: list[CheckResult] = []
    for m in re.finditer(rx, text, flags=flags):
        _orig = m.group(0).strip()
        _repl = items.get(_orig.lower() if ignore_case else _orig)

        results.append(
            CheckResult(
                start_pos=m.start() + offset[0],
                end_pos=m.end() + offset[1],
                check=err,
                message=msg.format(_repl, _orig),
                replacements=_repl,
            )
        )
    return results


def existence_check(  # noqa: PLR0913, PLR0917
    text: str,
    re_items: list,
    err: str,
    msg: str,
    ignore_case: bool = True,
    unicode: bool = True,
    offset: tuple[int, int] = (0, 0),
    padding: Pd = Pd.words_in_txt,
    dotall: bool = False,
    exceptions: tuple = (),
) -> list[CheckResult]:
    """Build a checker that prohibits certain words or phrases."""
    flags = 0
    if ignore_case:
        flags |= re.IGNORECASE
    if unicode:
        flags |= re.UNICODE
    if dotall:
        flags |= re.DOTALL

    errors: list[CheckResult] = []

    if padding not in {Pd.disabled, Pd.safe_join, Pd.words_in_txt}:
        # Pd.whitespace & Pd.sep_in_text each add 1 char before and after
        offset = (offset[0] + 1, offset[1] - 1)

    if len(re_items) > 1:
        re_items = Pd.safe_join.format("|".join(re_items))
    else:
        re_items = re_items[0]
    rx = padding.format(re_items)
    for m in re.finditer(rx, text, flags=flags):
        txt = m.group(0).strip()
        if any(
            re.search(exception, txt, flags=flags) for exception in exceptions
        ):
            continue
        errors.append(
            CheckResult(
                start_pos=m.start() + offset[0],
                end_pos=m.end() + offset[1],
                check=err,
                message=msg.format(txt),
                replacements=None,
            ),
        )
        # TODO: group(1) already offers padless word (when turned inside out)
    return errors


def existence_check_simple(  # noqa: PLR0913, PLR0917
    text: str,
    pattern: str,
    err: str,
    msg: str,
    ignore_case: bool = True,
    unicode: bool = True,
    exceptions: tuple = (),
) -> list[CheckResult]:
    """
    Build a checker for single patterns.

    in comparison to existence_check:
        - does not work on lists
        - has no padding & offset
    """
    flags = 0
    if unicode:
        flags |= re.UNICODE
    if ignore_case:
        flags |= re.IGNORECASE
    return [
        CheckResult(
            start_pos=_m.start(),
            end_pos=_m.end(),
            check=err,
            message=msg.format(_m.group(0).strip()),
            replacements=None,
        )
        for _m in re.finditer(pattern, text, flags=flags)
        if not any(
            re.search(exception, _m.group(0), flags=flags)
            for exception in exceptions
        )
    ]


def _has_digits(text: str) -> bool:
    """
    Determine if a string contains digits.

    This is used in reverse_existence_check due to being nearly three times as
    fast as the previous regex implementation, which is called on every result.
    """
    # TODO: confirm below, generator expressions should not do this, but
    # benchmarks show any() as being slower

    # loop instead of any() is used for performance - any iterates again after
    # results are generated, instead of just iterating once
    for char in text:  # noqa: SIM110
        if char in string.digits:
            return True
    return False


def _allowed_word(
    permitted: set[str], match: re.Match, ignore_case: bool = True
) -> bool:
    """Determine if a match object result is in a set of strings."""
    matched = match.group(0)
    if ignore_case:
        return matched.lower() in permitted
    return matched in permitted


def reverse_existence_check(  # noqa: PLR0913, PLR0917
    text: str,
    allowed: list[str],
    err: str,
    msg: str,
    ignore_case: bool = True,
    offset: tuple[int, int] = (0, 0),
) -> list[CheckResult]:
    """Find all words in `text` that aren't in the list of `allowed` words."""
    permitted = set(
        [word.lower() for word in allowed] if ignore_case else allowed
    )
    allowed_word = functools.partial(
        _allowed_word, permitted, ignore_case=ignore_case
    )

    # TODO: benchmark performance of this and _has_digits compared with
    # excluding digits from results in the first place
    # Match all 3+ character words that contain a hyphen or apostrophe
    # only in the middle (not as the first or last character)
    tokenizer = re.compile(r"\w[\w'-]+\w")

    return [
        CheckResult(
            start_pos=m.start() + 1 + offset[0],
            end_pos=m.end() + offset[1],
            check=err,
            message=msg.format(m.group(0)),
            replacements=None,
        )
        for m in tokenizer.finditer(text)
        if not _has_digits(m.group(0)) and not allowed_word(m)
    ]


def context(_text: str, _position: int, level: str = "paragraph") -> str:
    """Get sentence or paragraph that surrounds the given position."""
    if level == "sentence":  # noqa: SIM114
        pass
    elif level == "paragraph":
        pass

    return ""


###############################################################################
# Experimental ################################################################
###############################################################################


def _detect_language(text: str) -> str:
    """Detect the source language."""
    # TODO: add language to text.metadata, some checks are language agnostic
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


def limit_results(value: int) -> Callable:
    """Decorate a check to truncate error output to a specified threshold."""
    if value < 0:
        raise ValueError("Value for @limit_results() must be >= 0")

    def wrapper(fn: Callable) -> Callable:
        @functools.wraps(fn)
        def wrapped(*args: list, **kwargs: dict) -> list[CheckResult]:
            return _truncate_errors(fn(*args, **kwargs), value)

        return wrapped

    return wrapper


def _truncate_errors(
    errors: list[CheckResult],
    limit: int,
) -> list[CheckResult]:
    """
    Truncate a list of errors to a given threshold.

    This also notes how many times the error was raised prior to truncation.
    """
    if len(errors) > limit:
        e0 = errors[0]
        m0 = e0.message

        if len(errors) == limit + 1:
            m0 += " Found once elsewhere."
        else:
            m0 += f" Found {len(errors)} times elsewhere."

        errors = [
            CheckResult(
                start_pos=e0.start_pos,
                end_pos=e0.end_pos,
                check=e0.check,
                message=m0,
                replacements=e0.replacements,
            )
        ] + errors[1:limit]

    return errors


def ppm_threshold(threshold: float) -> Callable:
    """Decorate a check to error if the PPM threshold is surpassed."""
    if threshold < 0:
        raise ValueError("Value for @ppm_threshold() must be >= 0")

    def wrapped(fn: Callable) -> Callable:
        @functools.wraps(fn)
        def wrapper(*args: list, **kwargs: dict) -> list[CheckResult]:
            _len = 0  # neutral element
            if "text" in kwargs:
                _len = len(kwargs["text"])
            elif len(args) > 0:
                _len = len(args[0])
            return _threshold_check(fn(*args, **kwargs), threshold, _len)

        return wrapper

    return wrapped


def _threshold_check(
    errors: list[CheckResult], threshold: float, length: int
) -> list[CheckResult]:
    """Return an error if the specified PPM threshold is surpassed."""
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
