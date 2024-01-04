"""Test the existence_check function from the tools.py module."""
from proselint.checks import Pd, existence_check


def test_existence_check():
    """Basic smoke test to determine that existence_check is working."""
    items = ["abc"]
    err = "error message"
    msg = "it exists"
    assert existence_check("abc is as easy as 123", items, err, msg) != []
    assert existence_check("easy breezy", items, err, msg) == []
    assert err in existence_check("abc is as easy as 123", items, err, msg)[0]
    assert msg in existence_check("abc is as easy as 123", items, err, msg)[0]


def test_existence_check_multiple_matches():
    """Test that multiple matches are found correctly."""
    items = ["abc"]
    err = "error message"
    msg = "it exists"
    assert len(existence_check("abc and abc are as easy as 123", items, err, msg)) == 2
    assert (
        len(
            existence_check(
                "ABC and abc are as easy as 123",
                items,
                err,
                msg,
                ignore_case=True,
            ),
        )
        == 2
    )
    assert (
        len(
            existence_check(
                "ABC and abc are as easy as 123",
                items,
                err,
                msg,
                ignore_case=False,
            ),
        )
        == 1
    )
    assert existence_check("abcabc are easy as 123", items, err, msg) == []


def test_existence_check_exceptions():
    """Test that existence_check does not report excluded phrases"""
    regex = [r"\b(\w+)\b\s\1"]
    no = ["should should"]
    errs = existence_check(
        "should should flag flag.",
        regex,
        "",
        "",
        padding=Pd.disabled,
    )
    assert len(errs) == 2
    errs = existence_check(
        "should should flag flag.",
        regex,
        "",
        "",
        exceptions=no,
        padding=Pd.disabled,
    )
    assert len(errs) == 1
