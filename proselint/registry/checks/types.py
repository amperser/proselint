"""Check types."""

from functools import partial
from itertools import chain, filterfalse
from re import (
    Match,
    Pattern,
    RegexFlag,
    finditer,
    search,
)
from re import compile as rcompile
from typing import Callable, NamedTuple, Union

from proselint.registry.checks import Check, CheckResult, Padding

CheckFn = Callable[[str, Check], list[CheckResult]]


class Consistency(NamedTuple):
    """Carry consistency check information."""

    term_pairs: tuple[tuple[str, str], ...]

    @staticmethod
    def process_pair(
        text: str,
        check: Check,
        flag: RegexFlag,
        pair: tuple[str, str],
    ) -> list[CheckResult]:
        """Check a term pair over `text`."""
        matches = [list(finditer(term, text, flag)) for term in pair]

        if not len(matches[0]) and not len(matches[1]):
            return []

        idx_minority = len(matches[0]) > len(matches[1])
        majority_term = pair[not idx_minority]
        return [
            CheckResult(
                start_pos=m.start() + check.offset[0],
                end_pos=m.end() + check.offset[1],
                check_path=check.path,
                message=check.message.format(majority_term, m.group(0)),
                replacements=majority_term,
            )
            for m in matches[idx_minority]
        ]

    def check(self, text: str, check: Check) -> list[CheckResult]:
        """Check the consistency of given term pairs in `text`."""
        flag = check.re_flag
        process_pair = partial(Consistency.process_pair, text, check, flag)

        return list(chain.from_iterable(map(process_pair, self.term_pairs)))


class PreferredForms(NamedTuple):
    """Carry preferred forms check information."""

    items: dict[str, str]
    padding: Padding = Padding.WORDS_IN_TEXT

    def check(self, text: str, check: Check) -> list[CheckResult]:
        """Check for terms to be replaced with a preferred form in `text`."""
        offset = self.padding.to_offset_from(check.offset)
        flag = check.re_flag

        return [
            CheckResult(
                start_pos=m.start() + offset[0],
                end_pos=m.end() + offset[1],
                check_path=check.path,
                message=check.message.format(replacement, m.group(0).strip()),
                replacements=replacement,
            )
            for original, replacement in self.items.items()
            for m in finditer(self.padding.format(original), text, flag)
        ]


class PreferredFormsSimple(NamedTuple):
    """Carry simplified preferred forms check information."""

    items: dict[str, str]
    padding: Padding = Padding.WORDS_IN_TEXT

    def map_match(
        self, check: Check, offset: tuple[int, int], match: Match[str]
    ) -> CheckResult:
        """Convert a `re.Match` object to a `CheckResult`."""
        original = match.group(0).strip()
        replacement = self.items.get(
            original.lower() if check.ignore_case else original
        )

        return CheckResult(
            start_pos=match.start() + offset[0],
            end_pos=match.end() + offset[1],
            check_path=check.path,
            message=check.message.format(replacement, original),
            replacements=replacement,
        )

    def check(self, text: str, check: Check) -> list[CheckResult]:
        """Check for terms to be replaced with a preferred form in `text`."""
        offset = self.padding.to_offset_from(check.offset)
        flag = check.re_flag
        map_match = partial(self.map_match, check, offset)

        pattern = self.padding.format(
            Padding.SAFE_JOIN.format("|".join(self.items.keys()))
            if len(self.items) > 1
            else next(iter(self.items))
        )

        return list(map(map_match, finditer(pattern, text, flag)))


class Existence(NamedTuple):
    """Carry existence check information."""

    items: tuple[str, ...]
    padding: Padding = Padding.WORDS_IN_TEXT
    exceptions: tuple[str, ...] = ()

    def check(self, text: str, check: Check) -> list[CheckResult]:
        """Check for the existence of terms in `text`."""
        offset = self.padding.to_offset_from(check.offset)
        flag = check.re_flag

        pattern = self.padding.format(
            Padding.SAFE_JOIN.format("|".join(self.items))
            if len(self.items) > 1
            else next(iter(self.items))
        )

        return [
            CheckResult(
                start_pos=m.start() + offset[0],
                end_pos=m.end() + offset[1],
                check_path=check.path,
                message=check.message.format(m.group(0).strip()),
                replacements=None,
            )
            for m in finditer(pattern, text, flag)
            if not any(
                search(exception, m.group(0).strip(), flag)
                for exception in self.exceptions
            )
        ]


class ExistenceSimple(NamedTuple):
    """Carry simplified existence check information."""

    pattern: str
    exceptions: tuple[str, ...] = ()

    def check(self, text: str, check: Check) -> list[CheckResult]:
        """Check for the existence of a single pattern in `text`."""
        flag = check.re_flag

        return [
            CheckResult(
                start_pos=m.start() + check.offset[0],
                end_pos=m.end() + check.offset[1],
                check_path=check.path,
                message=check.message.format(m.group(0).strip()),
                replacements=None,
            )
            for m in finditer(self.pattern, text, flag)
            if not any(
                search(exception, m.group(0).strip(), flag)
                for exception in self.exceptions
            )
        ]


_DEFAULT_TOKENIZER = rcompile(
    Padding.WORDS_IN_TEXT.format(r"[a-zA-Z_][a-zA-Z_'-]+[a-zA-Z_]")
)


class ReverseExistence(NamedTuple):
    """Carry reverse existence check information."""

    allowed: set[str]

    TOKENIZER: Pattern[str] = _DEFAULT_TOKENIZER

    @staticmethod
    def _allowed_match(
        allowed: set[str], match: Match[str], *, ignore_case: bool = True
    ) -> bool:
        m_text = match.group(0)
        return (m_text.lower() if ignore_case else m_text) in allowed

    def check(self, text: str, check: Check) -> list[CheckResult]:
        """Check for words in `text` that are not `allowed`."""
        allowed_match = partial(
            ReverseExistence._allowed_match,
            self.allowed,
            ignore_case=check.ignore_case,
        )

        return [
            CheckResult(
                start_pos=m.start() + check.offset[0] + 1,
                end_pos=m.end() + check.offset[1],
                check_path=check.path,
                message=check.message.format(m.group(0)),
                replacements=None,
            )
            for m in filterfalse(allowed_match, self.TOKENIZER.finditer(text))
        ]


CheckType = Union[
    CheckFn,
    Consistency,
    PreferredForms,
    PreferredFormsSimple,
    Existence,
    ExistenceSimple,
    ReverseExistence,
]
