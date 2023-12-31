import os
from pathlib import Path

proselint_path = Path(__file__).parent
demo_file = proselint_path / "demo.md"

user_path = Path("~").expanduser()
cwd_path = Path.cwd()


def _get_xdg_path(variable_name: str, default_path: Path) -> Path:
    _value = os.environ.get(variable_name)
    if _value is None or _value == "":
        return default_path
    return Path(_value)


xdg_config_path = _get_xdg_path("XDG_CONFIG_HOME", user_path / ".config")
xdg_cache_path = _get_xdg_path("XDG_CACHE_HOME", user_path / ".cache")


user_config_paths = [
    cwd_path / ".proselintrc.json",
    xdg_config_path / "proselint/config.json",
    user_path / ".proselintrc.json",
]

user_cache_path = xdg_cache_path / "proselint"
