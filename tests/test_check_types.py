"""Verify check types."""
# pyright: reportUnusedCallResult=false

from bisect import bisect_right
from dataclasses import dataclass
from itertools import accumulate, chain, combinations, repeat
from re import escape
from string import ascii_letters, ascii_lowercase

from hypothesis import assume, given
from hypothesis import strategies as st
from rstr import xeger

from proselint.registry.checks import BATCH_COUNT, Check, Padding, engine, types
from tests.common import engine_from

PADDING_STRATEGY = st.sampled_from(Padding)


@dataclass(frozen=True)
class _TermStrategies:
    item_text: st.SearchStrategy[str]
    term_pair: st.SearchStrategy[tuple[str, str]]
    term_pairs: st.SearchStrategy[list[tuple[str, str]]]

    @staticmethod
    def _not_substring(pair: tuple[str, str]) -> bool:
        a, b = (s.lower() for s in pair)
        return a not in b and b not in a

    @classmethod
    def from_alphabet(cls, alphabet: str) -> "_TermStrategies":
        item: st.SearchStrategy[str] = st.text(min_size=1, alphabet=alphabet)
        pair: st.SearchStrategy[tuple[str, str]] = st.tuples(item, item).filter(
            cls._not_substring
        )
        pairs: st.SearchStrategy[list[tuple[str, str]]] = st.lists(
            pair, min_size=1, max_size=BATCH_COUNT
        ).filter(
            lambda xs: all(map(cls._not_substring, combinations(chain(*xs), 2)))
        )

        return cls(item, pair, pairs)


def n_counts(data: st.DataObject, n: int) -> list[int]:
    """Generate a list of repetition counts for a collection of items."""
    return data.draw(st.lists(st.integers(1, 100), min_size=n, max_size=n))


LOWER_STRATEGIES = _TermStrategies.from_alphabet(ascii_lowercase)
ITEM_TEXT_STRATEGY = LOWER_STRATEGIES.item_text
TERM_PAIR_STRATEGY = LOWER_STRATEGIES.term_pair
TERM_PAIRS_STRATEGY = LOWER_STRATEGIES.term_pairs


CASED_STRATEGIES = _TermStrategies.from_alphabet(ascii_letters)


# Consistency
@given(TERM_PAIR_STRATEGY, st.text(), st.text())
def test_consistency_smoke(
    term_pair: tuple[str, str], path: str, noise: str
) -> None:
    """Return no matches when no elements are present."""
    assume(all(term not in noise.lower() for term in term_pair))
    check_type = types.Consistency(term_pairs=(term_pair,))
    check = Check(check_type=check_type, path=path, message="{} || {}")
    assert list(check.check(noise)) == []


@given(TERM_PAIR_STRATEGY, st.text(), st.integers(0, 1))
def test_consistency_one_in_text(
    term_pair: tuple[str, str], path: str, choice: int
) -> None:
    """Return no matches when only one element is present."""
    check_type = types.Consistency(term_pairs=(term_pair,))
    check = Check(check_type=check_type, path=path, message="{} || {}")
    assert list(check.check(term_pair[choice])) == []


@given(
    TERM_PAIR_STRATEGY,
    st.text(),
    st.tuples(st.integers(1, 100), st.integers(1, 100)),
)
def test_consistency_both_in_text(
    term_pair: tuple[str, str], path: str, count: tuple[int, int]
) -> None:
    """Return correct matches when both elements are present."""
    check_type = types.Consistency(term_pairs=(term_pair,))
    check = Check(check_type=check_type, path=path, message="{} || {}")

    text = f"{term_pair[0]} " * count[0] + f"{term_pair[1]} " * count[1]
    results = list(check.check(text))
    assert len(results) == min(count)
    assert all(result.check_path == path for result in results)
    idx_minority = count[0] > count[1]
    assert all(
        result.message
        == f"{term_pair[not idx_minority]} || {term_pair[idx_minority]}"
        for result in results
    )


# PreferredForms
PREFERRED_ITEMS_STRATEGY: st.SearchStrategy[dict[str, str]] = st.builds(  # pyright: ignore[reportUnknownVariableType]
    dict,
    LOWER_STRATEGIES.term_pairs,
)

PREFERRED_ITEMS_CASED_STRATEGY: st.SearchStrategy[dict[str, str]] = st.builds(  # pyright: ignore[reportUnknownVariableType]
    dict,
    CASED_STRATEGIES.term_pairs,
)


@given(PREFERRED_ITEMS_STRATEGY, PADDING_STRATEGY, st.text(), st.text())
def test_preferred_smoke(
    items: dict[str, str], padding: Padding, path: str, noise: str
) -> None:
    """Return no matches when no elements are present."""
    assume(all(item not in noise.lower() for item in items))
    check_type = types.PreferredForms(items=items, padding=padding)
    check = Check(
        check_type=check_type,
        path=path,
        message="{} || {}",
        engine=engine_from(padding),
    )
    assert list(check.check(noise)) == []


@given(PREFERRED_ITEMS_STRATEGY, PADDING_STRATEGY, st.text(), st.data())
def test_preferred_values_smoke(
    items: dict[str, str], padding: Padding, path: str, data: st.DataObject
) -> None:
    """Return no matches when only replacements are present."""
    count = n_counts(data, len(items))
    check_type = types.PreferredForms(items=items, padding=padding)
    check = Check(
        check_type=check_type,
        path=path,
        message="{} || {}",
        engine=engine_from(padding),
    )
    content = " ".join(chain.from_iterable(map(repeat, items.values(), count)))
    assert list(check.check(content)) == []


@given(PREFERRED_ITEMS_STRATEGY, PADDING_STRATEGY, st.text(), st.data())
def test_preferred_in_text(
    items: dict[str, str], padding: Padding, path: str, data: st.DataObject
) -> None:
    """Return correct matches when elements are present."""
    count = n_counts(data, len(items))
    check_type = types.PreferredForms(items=items, padding=padding)
    check = Check(
        check_type=check_type,
        path=path,
        message="{} || {}",
        engine=engine_from(padding),
    )
    selected_matches = list(
        chain.from_iterable(
            repeat(xeger(padding.format(escape(a))), b)
            for a, b in zip(items.keys(), count, strict=True)
        )
    )

    # NOTE: rstr.xeger does not work for nonword boundaries, so this is
    # necessary. See leapfrogonline/rstr#45.
    if padding == Padding.NONWORDS_IN_TEXT:
        selected_matches = [f"_{x}_" for x in selected_matches]

    content = "  ".join(selected_matches)
    results = list(check.check(content))
    assert len(results) == sum(count)

    cum_count = list(accumulate(count))
    values = list(items.values())
    for idx in range(len(results)):
        replacement = values[bisect_right(cum_count, idx)]
        entry = selected_matches[idx].strip()
        if padding == Padding.NONWORDS_IN_TEXT:
            entry = entry[1:-1]

        assert results[idx].check_path == path
        assert results[idx].message == f"{replacement} || {entry}"
        assert results[idx].replacements == replacement


# PreferredFormsSimple
@given(PREFERRED_ITEMS_STRATEGY, PADDING_STRATEGY, st.text(), st.text())
def test_preferred_s_smoke(
    items: dict[str, str], padding: Padding, path: str, noise: str
) -> None:
    """Return no matches when no elements are present."""
    assume(all(item not in noise.lower() for item in items))
    check_type = types.PreferredFormsSimple(items=items, padding=padding)
    check = Check(
        check_type=check_type,
        path=path,
        message="{} || {}",
        engine=engine_from(padding),
    )
    assert list(check.check(noise)) == []


@given(PREFERRED_ITEMS_CASED_STRATEGY, PADDING_STRATEGY, st.text())
def test_preferred_s_case_sensitive(
    items: dict[str, str], padding: Padding, path: str
) -> None:
    """Return correct matches in case-sensitive mode with case variations."""
    check = Check(
        check_type=types.PreferredFormsSimple(items=items, padding=padding),
        path=path,
        message="{} || {}",
        engine=engine_from(
            padding, engine.RegexOptions(case_insensitive=False)
        ),
    )

    text = " ".join(items.keys())
    check_type = types.PreferredFormsSimple(items=items, padding=padding)
    results = list(check_type.check(text, check))

    for result, (original, replacement) in zip(
        results, items.items(), strict=False
    ):
        assert result.check_path == path
        assert result.message == f"{replacement} || {original}"
        assert result.replacements == replacement


@given(PREFERRED_ITEMS_CASED_STRATEGY, PADDING_STRATEGY, st.text())
def test_preferred_s_case_insensitive(
    items: dict[str, str], padding: Padding, path: str
) -> None:
    """Return correct matches in case-insensitive mode with case variations."""
    normalised = {k.lower(): v for k, v in items.items()}

    check_type = types.PreferredFormsSimple(items=normalised, padding=padding)
    check = Check(
        check_type=check_type,
        path=path,
        message="{} || {}",
        engine=engine_from(padding, engine.RegexOptions(case_insensitive=True)),
    )

    text_variations = [
        k.swapcase() if i % 2 == 0 else k.upper()
        for i, k in enumerate(items.keys())
    ]

    results = list(check_type.check(" ".join(text_variations), check))

    for result, text in zip(results, text_variations, strict=False):
        replacements = normalised[text.lower()]

        assert result.check_path == path
        assert result.message == f"{replacements} || {text}"
        assert result.replacements == replacements


@given(PREFERRED_ITEMS_STRATEGY, PADDING_STRATEGY, st.text(), st.data())
def test_preferred_s_values_smoke(
    items: dict[str, str], padding: Padding, path: str, data: st.DataObject
) -> None:
    """Return no matches when only replacements are present."""
    count = n_counts(data, len(items))
    check_type = types.PreferredFormsSimple(items=items, padding=padding)
    check = Check(
        check_type=check_type,
        path=path,
        message="{} || {}",
        engine=engine_from(padding),
    )
    content = " ".join(chain.from_iterable(map(repeat, items.values(), count)))
    assert list(check.check(content)) == []


@given(PREFERRED_ITEMS_STRATEGY, PADDING_STRATEGY, st.text(), st.data())
def test_preferred_s_in_text(
    items: dict[str, str], padding: Padding, path: str, data: st.DataObject
) -> None:
    """Return correct matches when elements are present."""
    count = n_counts(data, len(items))
    check_type = types.PreferredFormsSimple(items=items, padding=padding)
    check = Check(
        check_type=check_type,
        path=path,
        message="{} || {}",
        engine=engine_from(padding),
    )
    selected_matches = list(
        chain.from_iterable(
            repeat(xeger(padding.format(escape(a))), b)
            for a, b in zip(items.keys(), count, strict=True)
        )
    )

    # NOTE: rstr.xeger does not work for nonword boundaries, so this is
    # necessary. See leapfrogonline/rstr#45.
    if padding == Padding.NONWORDS_IN_TEXT:
        selected_matches = [f"_{x}_" for x in selected_matches]

    content = "  ".join(selected_matches)
    results = list(check.check(content))
    assert len(results) == sum(count)

    cum_count = list(accumulate(count))
    values = list(items.values())
    for idx in range(len(results)):
        replacement = values[bisect_right(cum_count, idx)]
        entry = selected_matches[idx].strip()
        if padding == Padding.NONWORDS_IN_TEXT:
            entry = entry[1:-1]

        assert results[idx].check_path == path
        assert results[idx].message == f"{replacement} || {entry}"
        assert results[idx].replacements == replacement


# Existence
EXISTENCE_ITEMS_STRATEGY: st.SearchStrategy[tuple[str, ...]] = st.builds(  # pyright: ignore[reportAssignmentType]
    tuple,
    st.lists(ITEM_TEXT_STRATEGY, min_size=1, max_size=BATCH_COUNT).filter(
        lambda x: all(
            item[0] not in item[1] and item[1] not in item[0]
            for item in combinations(x, 2)
        )
    ),
)


@st.composite
def items_split(draw: st.DrawFn) -> tuple[tuple[str, ...], tuple[str, ...]]:
    """Split existence items into items and exceptions."""
    items = draw(EXISTENCE_ITEMS_STRATEGY)
    split_idx = draw(st.integers(1, len(items)))
    return (items[:split_idx], items[split_idx:])


@given(items_split(), PADDING_STRATEGY, st.text(), st.text())
def test_existence_smoke(
    items_exceptions: tuple[tuple[str, ...], tuple[str, ...]],
    padding: Padding,
    path: str,
    noise: str,
) -> None:
    """Return no matches when no elements are present."""
    items, exceptions = items_exceptions
    assume(all(item not in noise.lower() for item in items))
    check_type = types.Existence(
        items=items, padding=padding, exceptions=exceptions
    )
    check = Check(
        check_type=check_type,
        path=path,
        message="{}",
        engine=engine_from(padding),
    )
    assert list(check.check(noise)) == []


@given(items_split(), PADDING_STRATEGY, st.text(), st.data())
def test_existence_exceptions_smoke(
    items_exceptions: tuple[tuple[str, ...], tuple[str, ...]],
    padding: Padding,
    path: str,
    data: st.DataObject,
) -> None:
    """Return no matches when only exceptions are present."""
    items, exceptions = items_exceptions
    count = n_counts(data, len(exceptions))
    check_type = types.Existence(
        items=items, padding=padding, exceptions=exceptions
    )
    check = Check(
        check_type=check_type,
        path=path,
        message="{}",
        engine=engine_from(padding),
    )
    content = " ".join(chain.from_iterable(map(repeat, exceptions, count)))
    assert list(check.check(content)) == []


@given(items_split(), PADDING_STRATEGY, st.text(), st.data())
def test_existence_in_text(
    items_exceptions: tuple[tuple[str, ...], tuple[str, ...]],
    padding: Padding,
    path: str,
    data: st.DataObject,
) -> None:
    """Return correct matches when elements are present."""
    items, exceptions = items_exceptions
    count = n_counts(data, len(items) + len(exceptions))
    check_type = types.Existence(
        items=items, padding=padding, exceptions=exceptions
    )
    check = Check(
        check_type=check_type,
        path=path,
        message="{}",
        engine=engine_from(padding),
    )
    selected_matches = list(
        chain.from_iterable(
            repeat(xeger(padding.format(escape(a))), b)
            for a, b in zip(chain(items, exceptions), count, strict=True)
        )
    )

    # NOTE: rstr.xeger does not work for nonword boundaries, so this is
    # necessary. See leapfrogonline/rstr#45.
    if padding == Padding.NONWORDS_IN_TEXT:
        selected_matches = [f"_{x}_" for x in selected_matches]

    content = "  ".join(selected_matches)
    results = list(check.check(content))
    cum_count = list(accumulate(count))
    assert len(results) == cum_count[len(count) - len(exceptions) - 1]

    for result, raw_entry in zip(results, selected_matches, strict=False):
        entry = raw_entry.strip()
        if padding == Padding.NONWORDS_IN_TEXT:
            entry = entry[1:-1]

        assert result.check_path == path
        assert result.message == entry
        assert result.replacements is None


# ExistenceSimple
@given(EXISTENCE_ITEMS_STRATEGY, st.text(), st.text())
def test_existence_s_smoke(
    items_exceptions: tuple[str, ...],
    path: str,
    noise: str,
) -> None:
    """Return no matches when no elements are present."""
    pattern, exceptions = items_exceptions[0], items_exceptions[1:]
    assume(pattern not in noise.lower())
    check_type = types.ExistenceSimple(pattern=pattern, exceptions=exceptions)
    check = Check(check_type=check_type, path=path, message="{}")
    assert list(check.check(noise)) == []


@given(EXISTENCE_ITEMS_STRATEGY, st.text(), st.data())
def test_existence_s_exceptions_smoke(
    items_exceptions: tuple[str, ...],
    path: str,
    data: st.DataObject,
) -> None:
    """Return no matches when only exceptions are present."""
    pattern, exceptions = items_exceptions[0], items_exceptions[1:]
    count = n_counts(data, len(exceptions))
    check_type = types.ExistenceSimple(pattern=pattern, exceptions=exceptions)
    check = Check(check_type=check_type, path=path, message="{}")
    content = " ".join(chain.from_iterable(map(repeat, exceptions, count)))
    assert list(check.check(content)) == []


@given(EXISTENCE_ITEMS_STRATEGY, st.text(), st.data())
def test_existence_s_in_text(
    items_exceptions: tuple[str, ...],
    path: str,
    data: st.DataObject,
) -> None:
    """Return correct matches when elements are present."""
    pattern, exceptions = items_exceptions[0], items_exceptions[1:]
    count = n_counts(data, len(items_exceptions))
    check_type = types.ExistenceSimple(pattern=pattern, exceptions=exceptions)
    check = Check(check_type=check_type, path=path, message="{}")
    selected_matches = list(
        chain.from_iterable(
            repeat(xeger(escape(a)), b)
            for a, b in zip(items_exceptions, count, strict=True)
        )
    )

    content = "  ".join(selected_matches)
    results = list(check.check(content))
    cum_count = list(accumulate(count))
    assert len(results) == cum_count[len(count) - len(exceptions) - 1]
    for result, entry in zip(results, selected_matches, strict=False):
        assert result.check_path == path
        assert result.message == entry.strip()
        assert result.replacements is None


# ReverseExistence
TOKEN_STRATEGY = st.from_regex(
    types._DEFAULT_TOKENIZER,  # pyright: ignore[reportPrivateUsage]
    alphabet=f"{ascii_letters}'-_",
)
TOKENS_STRATEGY = st.lists(TOKEN_STRATEGY, min_size=1, max_size=BATCH_COUNT)
NON_TOKEN_STRATEGY = st.one_of(st.just(r"\w\w?"), st.just(r"\w*\d+\w*"))
NON_TOKENS_STRATEGY = st.lists(
    NON_TOKEN_STRATEGY, min_size=1, max_size=BATCH_COUNT
)
REV_ALLOWED_STRATEGY: st.SearchStrategy[set[str]] = st.builds(  # pyright: ignore[reportUnknownVariableType]
    set, EXISTENCE_ITEMS_STRATEGY
)

# NOTE: traditional smoke is not applicable here, since any tokenizable noise
# beyond the allowed set would trigger a result.


@given(REV_ALLOWED_STRATEGY, st.text(), st.data())
def test_rev_existence_allowed_smoke(
    allowed: set[str], path: str, data: st.DataObject
) -> None:
    """Return no matches when only allowed items are present."""
    count = n_counts(data, len(allowed))
    check_type = types.ReverseExistence(allowed=allowed)
    check = Check(check_type=check_type, path=path, message="{}")
    content = " ".join(chain.from_iterable(map(repeat, allowed, count)))
    assert check.check(content)


@given(REV_ALLOWED_STRATEGY, st.text(), NON_TOKENS_STRATEGY)
def test_rev_existence_non_token_smoke(
    allowed: set[str], path: str, non_tokens: list[str]
) -> None:
    """Return no matches when only non-tokenizable items are present."""
    check_type = types.ReverseExistence(allowed=allowed)
    check = Check(check_type=check_type, path=path, message="{}")
    assert list(check.check(" ".join(map(xeger, non_tokens)))) == []


@given(REV_ALLOWED_STRATEGY, st.text(), TOKENS_STRATEGY)
def test_rev_existence_forbidden(
    allowed: set[str], path: str, tokens: list[str]
) -> None:
    """Return correct matches when items not in the allowed set are present."""
    assume(all(token not in allowed for token in tokens))
    check_type = types.ReverseExistence(allowed=allowed)
    check = Check(check_type=check_type, path=path, message="{}")
    results = list(check.check(" ".join(tokens)))

    assert len(results) == len(tokens)

    for result, token in zip(results, tokens, strict=True):
        assert result.check_path == path
        assert result.message == token.strip("'-")
        assert result.replacements is None
