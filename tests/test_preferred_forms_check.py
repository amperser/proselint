"""Test the preferred_forms_check function from the tools.py module."""
from __future__ import annotations

from proselint.checks import preferred_forms_check_regex


def test_preferred_forms_check():
    """Basic smoke test for preferred_forms_check."""
    items: dict[str, str] = {r"utilize": "use"}
    err = "error message"
    msg = "use the preferred form"
    assert (
        preferred_forms_check_regex("We utilize this tech", items, err, msg)
        != []
    )
    assert (
        preferred_forms_check_regex("We use this tech", items, err, msg) == []
    )


def test_preferred_forms_check_capitalization():
    """Test for preferred forms involving capitalization."""
    items: dict[str, str] = {r"stone age": "Stone Age"}
    err = "error message"
    msg = "use the preferred form"

    assert (
        preferred_forms_check_regex(
            "In the stone age",
            items,
            err,
            msg,
            ignore_case=False,
        )
        != []
    )
    assert (
        preferred_forms_check_regex(
            "In the Stone Age", items, err, msg, ignore_case=False
        )
        == []
    )
