"""
Use the right symbols.

source:     Butterick's Practical Typography
source_url: http://practicaltypography.com/
"""

from __future__ import annotations

from proselint.checks import (
    CheckFlags,
    CheckRegistry,
    CheckResult,
    CheckSpec,
    Existence,
    Pd,
    consistency_check,
    existence_check_simple,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
    # quotes
    """This is “a sentence”. Look at it.""",
    """“This should produce no error”, he said.""",
    """A 'singular' should not, though.""",
    # apo
    "jim's is preferred",
    "amanda´s is ok",
]

examples_fail = [
    "The long and winding road...",
    "Show me the money! (C)",
    "Show me the money! (c)",
    "The Fresh Maker (TM)",
    "The Fresh Maker (tm)",
    "Just Do It (R)",
    "Just Do It (r)",
    # spacing
    "This is a sentence.   This is another.",
    # mult
    "It is obvious that 2 x 2 = 4.",
    # quotes
    """This is "another sentence". How faulty.""",
    """"This should produce an error", he said.""",
    """Alas, "it should here too".""",
    # apo
    "jim's is preferred - amanda´s is ok, but not mixed",
    "pauls`s is not fine",
]

# TODO: reimplement limit_results

check_ellipsis = CheckSpec(
    Existence(
        [r"\.\.\."],
        padding=Pd.disabled,
    ),
    "typography.symbols.ellipsis",
    "'...' is an approximation, use the ellipsis symbol '…'.",
    flags=CheckFlags(limit_results=3),
)

check_copyright_symbol = CheckSpec(
    Existence(
        [r"\([cC]\)\B"],
        padding=Pd.disabled,
    ),
    "typography.symbols.copyright",
    "(c) is a goofy alphabetic approximation, use the symbol ©.",
    flags=CheckFlags(limit_results=1),
)

check_trademark_symbol = CheckSpec(
    Existence(
        [r"\(TM\)\B"],
        padding=Pd.disabled,
    ),
    "typography.symbols.trademark",
    "(TM) is a goofy alphabetic approximation, use the symbol ™.",
    flags=CheckFlags(limit_results=3),
)

check_registered_trademark_symbol = CheckSpec(
    Existence(
        [r"\([rR]\)\B"],
        padding=Pd.disabled,
    ),
    "typography.symbols.registered",
    "(R) is a goofy alphabetic approximation, use the symbol ®.",
    flags=CheckFlags(limit_results=3),
)

# FIXME: this check is repeated elsewhere
check_sentence_spacing = CheckSpec(
    Existence(
        [r"\. {3}"],
        padding=Pd.disabled,
    ),
    "typography.symbols.sentence_spacing",
    "More than two spaces after the period; use 1 or 2.",
    flags=CheckFlags(limit_results=3),
)

check_multiplication_symbol = CheckSpec(
    Existence(
        [r"[0-9]+ ?x ?[0-9]+"],
        padding=Pd.disabled,
    ),
    "typography.symbols.multiplication_symbol",
    "Use the multiplication symbol ×, not the letter x.",
    flags=CheckFlags(limit_results=3),
)

check_curly_quotes = CheckSpec(
    Existence(
        [r"\"[\w\s\d]+\""],
        padding=Pd.disabled,
    ),
    "typography.symbols.curly_quotes",
    'Use curly quotes “”, not straight quotes "".',
    flags=CheckFlags(limit_results=3),
)

deactivated_check_en_dash_separated_names = CheckSpec(
    Existence(["[A-Z][a-z]{1,10}[-\u2014][A-Z][a-z]{1,10}"]),
    "",
    "Use an en dash (–) to separate names.",
)


def _check_apostrophes(text: str) -> list[CheckResult]:
    """Enforce use of correct typographical apostrophes."""
    # src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L834
    err = "typography.symbols.apostrophes"
    msg = "Use the correct apostrophe - 's is preferred - ´s is ok"
    regex = r"\w+`s"  # unwanted form
    results = existence_check_simple(text, regex, err, msg)

    msg = "Use the same apostrophe consistently - {} vs {}"
    results.extend(
        consistency_check(
            text, [[r"\w+'s", r"\w+´s"]], err, msg, ignore_case=False
        )
    )
    return results


check_apostrophes = CheckSpec(
    _check_apostrophes,
    "typography.symbols.apostrophes",
    "Use the correct apostrophe - 's is preferred - ´s is ok",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    registry.register_many((
        check_ellipsis,
        check_copyright_symbol,
        check_trademark_symbol,
        check_registered_trademark_symbol,
        check_sentence_spacing,
        check_multiplication_symbol,
        check_curly_quotes,
        check_apostrophes,
    ))
