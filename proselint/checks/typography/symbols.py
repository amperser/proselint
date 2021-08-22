"""Use the right symbols.

source:     Butterick's Practical Typography
source_url: http://practicaltypography.com/
"""

from proselint.tools import existence_check, max_errors, memoize


@max_errors(3)
@memoize
def check_ellipsis(text):
    """Use an ellipsis instead of three dots."""
    err = "typography.symbols.ellipsis"
    msg = "'...' is an approximation, use the ellipsis symbol '…'."
    regex = r"\.\.\."

    return existence_check(text, [regex], err, msg, require_padding=False,
                           offset=0)


@max_errors(1)
@memoize
def check_copyright_symbol(text):
    """Use the copyright symbol instead of (c)."""
    err = "typography.symbols.copyright"
    msg = "(c) is a goofy alphabetic approximation, use the symbol ©."
    regex = r"\([cC]\)"

    return existence_check(text, [regex], err, msg, require_padding=False)


@max_errors(3)
@memoize
def check_trademark_symbol(text):
    """Use the trademark symbol instead of (TM)."""
    err = "typography.symbols.trademark"
    msg = "(TM) is a goofy alphabetic approximation, use the symbol ™."
    regex = r"\(TM\)"

    return existence_check(text, [regex], err, msg, require_padding=False)


@max_errors(3)
@memoize
def check_registered_trademark_symbol(text):
    """Use the registered trademark symbol instead of (R)."""
    err = "typography.symbols.trademark"
    msg = "(R) is a goofy alphabetic approximation, use the symbol ®."
    regex = r"\([rR]\)"

    return existence_check(text, [regex], err, msg, require_padding=False)


@max_errors(3)
@memoize
def check_sentence_spacing(text):
    """Use no more than two spaces after a period."""
    err = "typography.symbols.sentence_spacing"
    msg = "More than two spaces after the period; use 1 or 2."
    regex = r"\. {3}"

    return existence_check(text, [regex], err, msg, require_padding=False)


@max_errors(3)
@memoize
def check_multiplication_symbol(text):
    """Use the multiplication symbol ×, not the lowercase letter x."""
    err = "typography.symbols.multiplication_symbol"
    msg = "Use the multiplication symbol ×, not the letter x."
    regex = r"[0-9]+ ?x ?[0-9]+"

    return existence_check(text, [regex], err, msg, require_padding=False)


@max_errors(3)
@memoize
def check_curly_quotes(text):
    """Use curly quotes, not straight quotes."""
    err = "typography.symbols.curly_quotes"
    msg = 'Use curly quotes “”, not straight quotes "".'
    regex = r"\"[\w\s\d]+\""

    return existence_check(text, [regex], err, msg, require_padding=False)

# @memoize
# def check_en_dash_separated_names(text):
#     """Use an en-dash to separate names."""
#     # [u"[A-Z][a-z]{1,10}[-\u2014][A-Z][a-z]{1,10}",
#     #     u"Use an en dash (–) to separate names."],
