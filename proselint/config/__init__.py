"""Configuration for proselint."""

import copy
import json
from importlib.resources import files
from pathlib import Path
from typing import Optional, TypedDict
from warnings import showwarning as warn

from proselint import config
from proselint.config import paths


class Config(TypedDict):
    """
    Configuration for proselint.

    Keys:
    - `max_errors`: the maximum allowable number of errors proselint can output
    - `checks`: a dictionary of check modules to enable or disable
    """

    max_errors: int
    checks: dict[str, bool]


DEFAULT: Config = json.loads((files(config) / "default.json").read_text())


def _deepmerge_dicts(base: dict, overrides: dict) -> dict:
    return base | overrides | {
        key: (
            _deepmerge_dicts(b_value, o_value)
            if isinstance(b_value := base[key], dict)
            else o_value
        )
        for key in set(base) & set(overrides)
        if isinstance(o_value := overrides[key], dict)
    }


def validate_config(config: dict) -> bool:
    """Validate a configuration dictionary."""
    if not isinstance(config, dict):
        return False
    
    # Check required keys
    if 'max_errors' not in config or 'checks' not in config:
        return False
    
    # Validate max_errors
    if not isinstance(config['max_errors'], int) or config['max_errors'] < 0:
        return False
    
    # Validate checks
    if not isinstance(config['checks'], dict):
        return False
    
    # All check values should be booleans
    for key, value in config['checks'].items():
        if not isinstance(key, str) or not isinstance(value, bool):
            return False
    
    return True


def load_from(config_path: Optional[Path] = None) -> Config:
    """
    Read various config paths, allowing user overrides.

    NOTE: This assumes that a `config_path` is valid if one is provided.
    """
    result = copy.deepcopy(DEFAULT)
    config_paths = paths.config_paths + ([config_path] if config_path else [])

    for path in config_paths:
        if path.is_file():
            try:
                config_data = json.loads(path.read_text())
                if validate_config(config_data):
                    result: Config = _deepmerge_dicts(result, config_data)
                else:
                    warn(
                        f"Invalid configuration in {path}, skipping.",
                        UserWarning,
                        "",
                        0,
                    )
            except (json.JSONDecodeError, UnicodeDecodeError) as e:
                warn(
                    f"Error reading configuration from {path}: {e}",
                    UserWarning,
                    "",
                    0,
                )
        if path.suffix == ".json" and (old := path.with_suffix("")).is_file():
            warn(
                f"{old} was found instead of a JSON file. Rename to {path}.",
                DeprecationWarning,
                "",
                0,
            )

    return result
