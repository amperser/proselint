"""Proselint applies advice from great writers to your writing."""

from . import checks
from . import tools
from .config_base import proselint_base as config_default
from .config_paths import proselint_path as path
from .logger import log

__all__ = ["checks", "config_default", "log", "path", "tools"]
