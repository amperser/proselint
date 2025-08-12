"""Configuration paths for proselint."""

import os
from pathlib import Path

XDG_CONFIG_VAR = "XDG_CONFIG_HOME"
XDG_CACHE_VAR = "XDG_CACHE_HOME"

proselint_path = Path(__file__).parent.parent
demo_path = proselint_path / "demo.md"
home_path = Path.home()
cwd = Path.cwd()


def _get_xdg_path(env_var: str, default: Path) -> Path:
    """Get an XDG path from an environment variable, or a provided default."""
    return Path(xdg_path) if (xdg_path := os.environ.get(env_var)) else default


config_global_path = Path("/etc/proselintrc")
config_user_path = _get_xdg_path(XDG_CONFIG_VAR, home_path / ".config")

config_paths = [
    # NOTE: This is in reverse priority order - the order config gets merged in
    config_global_path,
    home_path / ".proselintrc.json",
    config_user_path / "proselint" / "config.json",
    cwd / ".proselintrc.json",
]
