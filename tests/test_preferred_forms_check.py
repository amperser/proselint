"""Test the preferred_forms_check function from the tools.py module."""

from proselint.checks import preferred_forms_check


def test_preferred_forms_check():
    """Basic smoke test for preferred_forms_check."""
    items = [["use", ["utilize"]]]
    err = "error message"
    msg = "use the preferred form"
    assert preferred_forms_check("We utilize this tech", items, err, msg) != []
    assert preferred_forms_check("We use this tech", items, err, msg) == []


def test_preferred_forms_check_capitalization():
    """Test for preferred forms involving capitalization."""
    items = [["Stone Age", ["stone age"]]]
    err = "error message"
    msg = "use the preferred form"
    assert not preferred_forms_check(
        "In the stone age",
        items,
        err,
        msg,
        ignore_case=False,
    )
    assert (
        preferred_forms_check(
            "In the Stone Age", items, err, msg, ignore_case=False
        )
        == []
    )
