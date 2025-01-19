"""Test the consistency_check function from the tools.py module."""

from proselint.checks import consistency_check


def test_consistency_check():
    """Basic smoke test for consistency_check."""
    items = [["colour", "color"]]
    err = "error message"
    msg = "inconsistent form of {} vs {}"
    assert consistency_check("Painting colour on color", items, err, msg) != []
    assert consistency_check("Painting colour on colour", items, err, msg) == []
    assert consistency_check("Painting color on color", items, err, msg) == []
