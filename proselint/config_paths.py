import os
from pathlib import Path

proselint_path = Path(__file__).parent
demo_file = proselint_path / "demo.md"

user_path = Path("~").expanduser()
cwd_path = Path.cwd()


def _get_xdg_path(variable_name: str, default_path: Path) -> Path:
    _value = os.environ.get(variable_name)
    if _value is None or not _value:
        return default_path
    return Path(_value)


config_global_path = Path("/etc/proselintrc")
config_xdg_path = _get_xdg_path("XDG_CONFIG_HOME", user_path / ".config")

config_user_paths = [
    # highest prio is user provided path then as followed
    cwd_path / ".proselintrc.json",
    config_xdg_path / "proselint/config.json",
    user_path / ".proselintrc.json",
]

cache_xdg_path = _get_xdg_path("XDG_CACHE_HOME", user_path / ".cache")
cache_user_path = cache_xdg_path / "proselint"
cache_user_path.mkdir(parents=True, exist_ok=True)
