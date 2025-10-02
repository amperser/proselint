"""Test user option overrides using --config and load_options."""

import json
from pathlib import Path

from pytest import LogCaptureFixture, raises

from proselint.command_line import get_parser, proselint
from proselint.config import (
    DEFAULT,
    _deepmerge_dicts,  # pyright: ignore[reportPrivateUsage]
    load_from,
)
from proselint.registry import CheckRegistry

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


def test_specific_overrides_general() -> None:
    """Test that specific config keys override general ones."""
    checks = {
            "typography": True,
            "typography.symbols": False,
            "typography.symbols.curly_quotes": True,
            "typography.punctuation.hyperbole": False,
    }

    registry = CheckRegistry()
    enabled = registry.get_all_enabled(checks)

    paths = {check.path for check in enabled}

    assert any(
        "typography.symbols.curly_quotes" in path
        for path in paths
    )

    assert len(
            [path for path in paths
            if path.startswith("typography.symbols.")
            and "curly_quotes" not in path]
            ) == 0

    assert not any(
        "typography.punctuation.hyperbole" in path
        for path in paths
    )

    assert any(
        path.startswith("typography.")
        and not path.startswith("typography.symbols.")
        and "hyperbole" not in path
        for path in paths
    )


def test_load_from() -> None:
    """Test load_options by specifying a user options path."""
    overrides = load_from(CONFIG_FILE)
    assert load_from()["checks"]["uncomparables"]
    assert not overrides["checks"]["uncomparables"]


def test_config_flag(caplog: LogCaptureFixture) -> None:
    """Test the --config CLI argument."""
    with caplog.at_level("WARNING", "proselint"):
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
