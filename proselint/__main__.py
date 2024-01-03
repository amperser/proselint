"""
__main__.py.

This lets you run python -m proselint.
"""
from multiprocessing import freeze_support

from .command_line import proselint

if __name__ == "__main__":
    freeze_support()  # todo: really needed?
    proselint()
