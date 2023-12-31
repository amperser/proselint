# flake8: noqa

"""Proselint applies advice from great writers to your writing."""
from . import tools
from .version import __version__
from .logger import log

__all__ = ["tools", "log"]
