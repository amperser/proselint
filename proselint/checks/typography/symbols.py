"""Use the right symbols.

source:     Butterick's Practical Typography
source_url: http://practicaltypography.com/
"""

from __future__ import annotations

from proselint.checks import Pd
from proselint.checks import ResultCheck
from proselint.checks import existence_check
from proselint.checks import limit_results


def check(text: str) -> list[ResultCheck]:
    # NOTE: these tests are pretty fast, so they are combined for a more even
    # load

    @limit_results(3)
    def check_ellipsis(_text: str) -> list[ResultCheck]:
        """Use an ellipsis instead of three dots."""
        err = "typography.symbols.ellipsis"
        msg = "'...' is an approximation, use the ellipsis symbol '…'."
        items = [r"\.\.\."]

        return existence_check(_text, items, err, msg, padding=Pd.disabled)

    @limit_results(1)
    def check_copyright_symbol(_text: str) -> list[ResultCheck]:
        """Use the copyright symbol instead of (c)."""
        err = "typography.symbols.copyright"
        msg = "(c) is a goofy alphabetic approximation, use the symbol ©."
        regex = r"\([cC]\)"

        return existence_check(_text, [regex], err, msg, padding=Pd.disabled)

    @limit_results(3)
    def check_trademark_symbol(_text: str) -> list[ResultCheck]:
        """Use the trademark symbol instead of (TM)."""
        err = "typography.symbols.trademark"
        msg = "(TM) is a goofy alphabetic approximation, use the symbol ™."
        regex = r"\(TM\)"

        return existence_check(_text, [regex], err, msg, padding=Pd.disabled)

    @limit_results(3)
    def check_registered_trademark_symbol(_text: str) -> list[ResultCheck]:
        """Use the registered trademark symbol instead of (R)."""
        err = "typography.symbols.trademark"
        msg = "(R) is a goofy alphabetic approximation, use the symbol ®."
        regex = r"\([rR]\)"

        return existence_check(_text, [regex], err, msg, padding=Pd.disabled)

    @limit_results(3)
    def check_sentence_spacing(_text: str) -> list[ResultCheck]:
        """Use no more than two spaces after a period."""
        err = "typography.symbols.sentence_spacing"
        msg = "More than two spaces after the period; use 1 or 2."
        regex = r"\. {3}"

        return existence_check(_text, [regex], err, msg, padding=Pd.disabled)

    @limit_results(3)
    def check_multiplication_symbol(_text: str) -> list[ResultCheck]:
        """Use the multiplication symbol ×, not the lowercase letter x."""
        err = "typography.symbols.multiplication_symbol"
        msg = "Use the multiplication symbol ×, not the letter x."
        regex = r"[0-9]+ ?x ?[0-9]+"

        return existence_check(_text, [regex], err, msg, padding=Pd.disabled)

    @limit_results(3)
    def check_curly_quotes(_text: str) -> list[ResultCheck]:
        """Use curly quotes, not straight quotes."""
        err = "typography.symbols.curly_quotes"
        msg = 'Use curly quotes “”, not straight quotes "".'
        regex = r"\"[\w\s\d]+\""

        return existence_check(_text, [regex], err, msg, padding=Pd.disabled)

    def disabled_check_en_dash_separated_names(text: str) -> list[ResultCheck]:
        """Use an en-dash to separate names."""
        # [u"[A-Z][a-z]{1,10}[-\u2014][A-Z][a-z]{1,10}",
        #     u"Use an en dash (–) to separate names."],
        return []  # TODO

    result = check_ellipsis(text)
    result.extend(check_copyright_symbol(text))
    result.extend(check_trademark_symbol(text))
    result.extend(check_registered_trademark_symbol(text))
    result.extend(check_sentence_spacing(text))
    result.extend(check_multiplication_symbol(text))
    result.extend(check_curly_quotes(text))
    return result
