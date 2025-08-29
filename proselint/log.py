"""Handle logging for proselint."""

from __future__ import annotations

import logging
from sys import stderr, stdout
from typing import Callable, TextIO


def _get_level_filter(
    level: int, *, invert: bool = False,
) -> Callable[[logging.LogRecord], bool]:
    """Create a filter function that allows log records of a given `level`."""
    def _filter(record: logging.LogRecord) -> bool:
        return record.levelno >= level if invert else record.levelno <= level
    return _filter


def _init_stream_handler(
    stream: TextIO, level: int, *, invert: bool = False
) -> logging.StreamHandler[TextIO]:
    """Test."""
    handler = logging.StreamHandler(stream)
    handler.setLevel(level)
    handler.addFilter(_get_level_filter(level, invert=invert))
    return handler


class Logger(logging.Logger):
    """Handle logging for proselint."""

    @staticmethod
    def setup(*, verbose: bool = False) -> None:
        """Initialise the logger."""
        base_handler = _init_stream_handler(
            stdout, logging.DEBUG if verbose else logging.INFO
        )
        err_handler = _init_stream_handler(stderr, logging.WARNING, invert=True)

        logging.basicConfig(
            level=logging.NOTSET,
            format="[%(levelname)08s] %(name)s: %(message)s"
            if verbose
            else "%(message)s",
            handlers=[base_handler, err_handler],
        )

    @property
    def verbose(self) -> bool:
        """Whether or not the logger is in verbose mode."""
        return self.level == logging.DEBUG


logging.setLoggerClass(Logger)
log: Logger = logging.getLogger("proselint")  # pyright: ignore[reportAssignmentType]
