"""
Use the right symbols.

source:     Butterick's Practical Typography
source_url: http://practicaltypography.com/
"""

from proselint.registry.checks import Check, CheckFlags, types

check_ellipsis = Check(
    check_type=types.ExistenceSimple(pattern=r"\.\.\."),
    path="typography.symbols.ellipsis",
    message="'...' is an approximation, use the ellipsis symbol '…'.",
)

check_copyright_symbol = Check(
    check_type=types.ExistenceSimple(pattern=r"\(c\)"),
    path="typography.symbols.copyright",
    message="(c) is a goofy alphabetic approximation, use the symbol ©.",
)

check_trademark_symbol = Check(
    check_type=types.ExistenceSimple(pattern=r"\(tm\)"),
    path="typography.symbols.trademark",
    message="(TM) is a goofy alphabetic approximation, use the symbol ™.",
)


check_registered_trademark_symbol = Check(
    check_type=types.ExistenceSimple(pattern=r"\(r\)"),
    path="typography.symbols.trademark",
    message="(R) is a goofy alphabetic approximation, use the symbol ®.",
)


check_sentence_spacing = Check(
    check_type=types.ExistenceSimple(pattern=r"\. {3}"),
    path="typography.symbols.sentence_spacing",
    message="More than two spaces after the period; use 1 or 2.",
)


check_multiplication_symbol = Check(
    check_type=types.ExistenceSimple(pattern=r"\d+ ?x ?\d+"),
    path="typography.symbols.multiplication",
    message="Use the multiplication symbol ×, not the letter x.",
)


check_curly_quotes = Check(
    check_type=types.ExistenceSimple(pattern=r"\"[\w\s\d]+\""),
    path="typography.symbols.curly_quotes",
    message='Use curly quotes “”, not straight quotes "".',
    flags=CheckFlags(allow_quotes=True),
)


# TODO: fix this or remove it
"""
check_en_dash_separated_names
    # [u"[A-Z][a-z]{1,10}[-\u2014][A-Z][a-z]{1,10}",
    #     u"Use an en dash (–) to separate names."],
"""

__register__ = (
    check_ellipsis,
    check_copyright_symbol,
    check_trademark_symbol,
    check_registered_trademark_symbol,
    check_sentence_spacing,
    check_multiplication_symbol,
    check_curly_quotes,
)
