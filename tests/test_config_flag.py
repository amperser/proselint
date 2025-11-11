"""Test user option overrides using --config and load_options."""

import json
from pathlib import Path

from pytest import LogCaptureFixture, raises

from proselint.command_line import get_parser, proselint
from proselint.config import (
    DEFAULT,
    _deepmerge_dicts,  # pyright: ignore[reportPrivateUsage]
    _flatten_checks,  # pyright: ignore[reportPrivateUsage]
    _sort_by_specificity,  # pyright: ignore[reportPrivateUsage]
    load_from,
)

CONFIG_FILE = Path(__file__).parent / "test-proselintrc.json"
PARSER = get_parser()


def test_deepmerge_dicts() -> None:
    """Test deepmerge_dicts."""
    d1 = {"a": 1, "b": {"c": 2, "d": 3}, "f": 4, "g": 5}
    d2 = {"a": 2, "b": {"c": 3, "e": 4}, "g": {"h": 5}, "i": 6}
    assert _deepmerge_dicts(d1, d2) == {
        "a": 2,
        "b": {"c": 3, "d": 3, "e": 4},
        "f": 4,
        "g": {"h": 5},
        "i": 6,
    }


def test_sort_by_specificity() -> None:
    """Test sort_by_specificity sorts by dot count descending."""
    unsorted = {
        "a": True,
        "a.b.c": False,
        "x.y": True,
        "a.b": True,
    }

    sorted_checks = _sort_by_specificity(unsorted)
    keys = list(sorted_checks.keys())

    dots = [key.count(".") for key in keys]

    assert dots == sorted(dots, reverse=True)
    assert keys[0] == "a.b.c"
    assert keys[-1] == "a"

    assert sorted_checks["a.b.c"] is False
    assert sorted_checks["a"] is True


def test_flatten_checks() -> None:
    """Test flatten_checks."""
    assert _flatten_checks({"a": True, "b": False}) == {
        "a": True,
        "b": False,
    }

    assert _flatten_checks({"x": {"y": True, "z": False}, "w": True}) == {
        "x.y": True,
        "x.z": False,
        "w": True,
    }

    assert _flatten_checks({"a": {"b": {"c": True}}}) == {"a.b.c": True}


def test_load_from() -> None:
    """Test load_options by specifying a user options path."""
    overrides = load_from(CONFIG_FILE)
    assert load_from()["checks"]["uncomparables"]
    assert not overrides["checks"]["uncomparables"]


def test_config_flag(caplog: LogCaptureFixture) -> None:
    """Test the --config CLI argument."""
    with caplog.at_level("INFO", "proselint"):
        _ = proselint(
            PARSER.parse_args(
                (
                    "check",
                    "--demo",
                )
            ),
            PARSER,
        )
        assert "uncomparables" in caplog.text
        caplog.clear()
        _ = proselint(
            PARSER.parse_args(
                ("check", "--demo", "--config", CONFIG_FILE.as_posix())
            ),
            PARSER,
        )
        assert "uncomparables" not in caplog.text

    with raises(FileNotFoundError):
        _ = proselint(
            PARSER.parse_args(
                ("check", "--demo", "--config", "non_existent_file")
            ),
            PARSER,
        )


def test_dump_config(caplog: LogCaptureFixture) -> None:
    """Test dump-config."""
    with caplog.at_level("INFO", "proselint"):
        _ = proselint(PARSER.parse_args(("dump-config", "--default")), PARSER)
        assert json.loads(caplog.records[0].message) == DEFAULT
        _ = proselint(
            PARSER.parse_args(
                ("dump-config", "--config", CONFIG_FILE.as_posix())
            ),
            PARSER,
        )
        assert json.loads(caplog.records[1].message) == json.loads(
            CONFIG_FILE.read_text()
        )
