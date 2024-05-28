"""
Use the right symbols.

source:     Butterick's Practical Typography
source_url: http://practicaltypography.com/
"""

from __future__ import annotations

from proselint.checks import (
    CheckResult,
    Pd,
    consistency_check,
    existence_check,
    existence_check_simple,
    limit_results,
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


@limit_results(3)
def check_ellipsis(text: str) -> list[CheckResult]:
    """Use an ellipsis instead of three dots."""
    err = "typography.symbols.ellipsis"
    msg = "'...' is an approximation, use the ellipsis symbol '…'."
    items = [r"\.\.\."]
    return existence_check(text, items, err, msg, padding=Pd.disabled)


@limit_results(1)
def check_copyright_symbol(text: str) -> list[CheckResult]:
    """Use the copyright symbol instead of (c)."""
    err = "typography.symbols.copyright"
    msg = "(c) is a goofy alphabetic approximation, use the symbol ©."
    regex = r"\([cC]\)\B"

    return existence_check(text, [regex], err, msg, padding=Pd.disabled)


@limit_results(3)
def check_trademark_symbol(text: str) -> list[CheckResult]:
    """Use the trademark symbol instead of (TM)."""
    err = "typography.symbols.trademark"
    msg = "(TM) is a goofy alphabetic approximation, use the symbol ™."
    regex = r"\(TM\)\B"

    return existence_check(text, [regex], err, msg, padding=Pd.disabled)


@limit_results(3)
def check_registered_trademark_symbol(text: str) -> list[CheckResult]:
    """Use the registered trademark symbol instead of (R)."""
    err = "typography.symbols.trademark"
    msg = "(R) is a goofy alphabetic approximation, use the symbol ®."
    regex = r"\([rR]\)\B"

    return existence_check(text, [regex], err, msg, padding=Pd.disabled)


@limit_results(3)
def check_sentence_spacing(text: str) -> list[CheckResult]:
    """Use no more than two spaces after a period."""
    err = "typography.symbols.sentence_spacing"
    msg = "More than two spaces after the period; use 1 or 2."
    regex = r"\. {3}"

    return existence_check(text, [regex], err, msg, padding=Pd.disabled)


@limit_results(3)
def check_multiplication_symbol(text: str) -> list[CheckResult]:
    """Use the multiplication symbol ×, not the lowercase letter x."""
    err = "typography.symbols.multiplication_symbol"
    msg = "Use the multiplication symbol ×, not the letter x."
    regex = r"[0-9]+ ?x ?[0-9]+"

    return existence_check(text, [regex], err, msg, padding=Pd.disabled)


@limit_results(3)
def check_curly_quotes(text: str) -> list[CheckResult]:
    """Use curly quotes, not straight quotes."""
    err = "typography.symbols.curly_quotes"
    msg = 'Use curly quotes “”, not straight quotes "".'
    regex = r"\"[\w\s\d]+\""

    return existence_check(text, [regex], err, msg, padding=Pd.disabled)


def disabled_check_en_dash_separated_names(_text: str) -> list[CheckResult]:
    """Use an en-dash to separate names."""
    # [u"[A-Z][a-z]{1,10}[-\u2014][A-Z][a-z]{1,10}",
    #     u"Use an en dash (–) to separate names."],
    return []  # TODO


def check_apostrophes(text: str) -> list[CheckResult]:
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
