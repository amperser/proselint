"""Check types."""

from collections.abc import Callable, Generator, Iterable, Iterator
from functools import partial
from itertools import chain, filterfalse, zip_longest
from typing import NamedTuple, TypeVar

from proselint.registry.checks import Check, CheckResult, Padding
from proselint.registry.checks.engine import Anchor, Match, MatchSet, PatternSet

CheckFn = Callable[[str, Check], Iterator[CheckResult]]

T = TypeVar("T")


def _takewhile_peek(
    predicate: Callable[[T], bool], iterable: Iterable[T]
) -> Generator[T]:
    """Take elements from `iterable` while `predicate` is consecutively true."""
    prev = True
    for x in iterable:
        current = predicate(x)
        if not prev and not current:
            break
        yield x
        prev = current


class Consistency(NamedTuple):
    """Carry consistency check information."""

    term_pairs: tuple[tuple[str, str], ...]

    # TODO: from 3.11+, flag should be a RegexFlag
    @staticmethod
    def process_pair(
        text: str,
        check: Check,
        pair: tuple[str, str],
    ) -> Iterator[CheckResult]:
        """Check a term pair over `text`."""
        # Unzip the zip of pair matches while both of the last pair were truthy
        # Reads the minimum possible elements to generate results
        matches: tuple[tuple[Match | None, ...], ...] = tuple(
            zip(
                *_takewhile_peek(
                    all,
                    zip_longest(
                        *(check.engine.finditer(term, text) for term in pair)
                    ),
                ),
                strict=True,
            )
        )

        if not matches:
            return iter(())

        idx_minority = matches[1][-1] is None
        majority_term = pair[not idx_minority]
        return (
            CheckResult(
                span=(m.start() + check.offset[0], m.end() + check.offset[1]),
                check_path=check.path,
                message=check.message.format(majority_term, m.group(0)),
                replacements=majority_term,
            )
            for m in filter(None, matches[idx_minority])
        )

    def check(self, text: str, check: Check) -> Iterator[CheckResult]:
        """Check the consistency of given term pairs in `text`."""
        process_pair = partial(Consistency.process_pair, text, check)

        return chain.from_iterable(map(process_pair, self.term_pairs))


class PreferredForms(NamedTuple):
    """Carry preferred forms check information."""

    items: dict[str, str]
    padding: Padding = Padding.WORDS_IN_TEXT

    def check(self, text: str, check: Check) -> Iterator[CheckResult]:
        """Check for terms to be replaced with a preferred form in `text`."""
        return (
            CheckResult(
                span=(m.start() + check.offset[0], m.end() + check.offset[1]),
                check_path=check.path,
                message=check.message.format(replacement, m.group(0).strip()),
                replacements=replacement,
            )
            for original, replacement in self.items.items()
            for m in check.engine.finditer(self.padding.format(original), text)
        )


class PreferredFormsSimple(NamedTuple):
    """Carry simplified preferred forms check information."""

    items: dict[str, str]
    padding: Padding = Padding.WORDS_IN_TEXT

    def map_match(self, check: Check, match: Match) -> CheckResult:
        """Convert a `re.Match` object to a `CheckResult`."""
        original = match.group(0).strip()
        replacement = self.items.get(
            original.lower() if check.engine.opts.case_insensitive else original
        )

        return CheckResult(
            span=(
                match.start() + check.offset[0],
                match.end() + check.offset[1],
            ),
            check_path=check.path,
            message=check.message.format(replacement, original),
            replacements=replacement,
        )

    def check(self, text: str, check: Check) -> Iterator[CheckResult]:
        """Check for terms to be replaced with a preferred form in `text`."""
        map_match = partial(self.map_match, check)

        pattern = check.engine.make_set(self.padding, tuple(self.items.keys()))

        return map(map_match, pattern.finditer(text))


def _process_existence(
    pattern: str | MatchSet[PatternSet],
    exceptions: MatchSet[PatternSet],
    text: str,
    check: Check,
) -> Iterator[CheckResult]:
    """Match against `pattern` respecting `offset` in `text`."""
    match_iter = (
        check.engine.finditer(pattern, text)
        if isinstance(pattern, str)
        else pattern.finditer(text)
    )
    return (
        CheckResult(
            span=(m.start() + check.offset[0], m.end() + check.offset[1]),
            check_path=check.path,
            message=check.message.format(m_text),
            replacements=None,
        )
        for m in match_iter
        if not exceptions.exists_in(m_text := m.group(0).strip())
    )


class Existence(NamedTuple):
    """Carry existence check information."""

    items: tuple[str, ...]
    padding: Padding = Padding.WORDS_IN_TEXT
    exceptions: tuple[str, ...] = ()

    def check(self, text: str, check: Check) -> Iterator[CheckResult]:
        """Check for the existence of terms in `text`."""
        pattern_set = check.engine.make_set(self.padding, self.items)
        exception_set = check.engine.make_set(
            self.padding, self.exceptions, Anchor.ANCHOR_BOTH
        )

        return _process_existence(pattern_set, exception_set, text, check)


class ExistenceSimple(NamedTuple):
    """Carry simplified existence check information."""

    pattern: str
    exceptions: tuple[str, ...] = ()

    def check(self, text: str, check: Check) -> Iterator[CheckResult]:
        """Check for the existence of a single pattern in `text`."""
        exception_set = check.engine.make_set(
            Padding.RAW, self.exceptions, Anchor.ANCHOR_BOTH
        )
        return _process_existence(self.pattern, exception_set, text, check)


_DEFAULT_TOKENIZER = Padding.WORDS_IN_TEXT.format(
    r"[a-zA-Z_][a-zA-Z_'-]+[a-zA-Z_]"
)


class ReverseExistence(NamedTuple):
    """Carry reverse existence check information."""

    allowed: set[str]

    TOKENIZER: str = _DEFAULT_TOKENIZER

    @staticmethod
    def _allowed_match(
        allowed: set[str], match: Match, *, case_insensitive: bool = True
    ) -> bool:
        m_text = match.group(0)
        return (m_text.lower() if case_insensitive else m_text) in allowed

    def check(self, text: str, check: Check) -> Iterator[CheckResult]:
        """Check for words in `text` that are not `allowed`."""
        allowed_match = partial(
            ReverseExistence._allowed_match,
            self.allowed,
            case_insensitive=check.engine.opts.case_insensitive,
        )

        return (
            CheckResult(
                span=(
                    m.start() + check.offset[0] + 1,
                    m.end() + check.offset[1],
                ),
                check_path=check.path,
                message=check.message.format(m.group(0)),
                replacements=None,
            )
            for m in filterfalse(
                allowed_match, check.engine.finditer(self.TOKENIZER, text)
            )
        )


CheckType = (
    CheckFn
    | Consistency
    | PreferredForms
    | PreferredFormsSimple
    | Existence
    | ExistenceSimple
    | ReverseExistence
)
