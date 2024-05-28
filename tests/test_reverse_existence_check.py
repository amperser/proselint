"""Test the reverse_existence_check function from proselint.checks."""
from proselint.checks import reverse_existence_check


def test_reverse_existence_check() -> None:
    """Basic smoke test to determine that reverse_existence_check is working."""
    allowed = ["abc", "cab"]
    err = "error message"
    msg = "something else exists"
    assert reverse_existence_check("abc cab abc abc", allowed, err, msg) == []
    assert reverse_existence_check("easy breezy", allowed, err, msg) != []
    assert err in reverse_existence_check("easy breezy", allowed, err, msg)[0]
    assert msg in reverse_existence_check("easy breezy", allowed, err, msg)[0]


def test_reverse_existence_check_multiple_matches() -> None:
    """Test that multiple matches are found correctly."""
    allowed = ["abc", "cab"]
    err = "error message"
    msg = "something exists"
    assert (
        len(
            reverse_existence_check(
                "abc and abc are easy like cab", allowed, err, msg
            )
        )
        == 4
    )
    assert (
        len(
            reverse_existence_check(
                "ABC and abc are easy like cab CAB",
                allowed,
                err,
                msg,
                ignore_case=True,
            )
        )
        == 4
    )
    assert (
        len(
            reverse_existence_check(
                "ABC and abc are easy like cab CAB",
                allowed,
                err,
                msg,
                ignore_case=False,
            )
        )
        == 6
    )
    assert reverse_existence_check("abc cab abc cab", allowed, err, msg) == []


def test_reverse_existence_check_special_chars() -> None:
    """Test that matches with ' and - are found correctly."""
    allowed = ["abc", "cab"]
    err = "error message"
    msg = "something exists"
    assert (
        len(reverse_existence_check("what's your go-to?", allowed, err, msg))
        == 3
    )
    allowed = ["what's"]
    assert (
        len(reverse_existence_check("what's your go-to?", allowed, err, msg))
        == 2
    )
    allowed = ["what's", "go-to"]
    assert (
        len(reverse_existence_check("what's your go-to?", allowed, err, msg))
        == 1
    )


def test_reverse_existence_check_no_digits() -> None:
    """Test that matches with digits are excluded correctly."""
    allowed = ["abc", "cab"]
    err = "error message"
    msg = "something exists"
    assert (
        len(
            reverse_existence_check(
                "abc cab 123 a5bc noway no7way", allowed, err, msg
            )
        )
        == 1
    )
    assert (
        reverse_existence_check("abc cab 123 a5bc no7way", allowed, err, msg)
        == []
    )


def test_reverse_existence_check_3_chars() -> None:
    """Test that matches are exclusively >=3 characters long."""
    allowed = ["abc", "cab"]
    err = "error message"
    msg = "something exists"
    assert len(reverse_existence_check("i am not me", allowed, err, msg)) == 1
    assert reverse_existence_check("i am me", allowed, err, msg) == []
