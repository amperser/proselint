"""Handle logging for proselint."""

from __future__ import annotations

import logging
from sys import stderr, stdout
from typing import TYPE_CHECKING, TextIO

if TYPE_CHECKING:
    from collections.abc import Callable


def _level_clamp_filter(
    *,
    min_level: int = logging.NOTSET,
    max_level: int = logging.CRITICAL,
) -> Callable[[logging.LogRecord], bool]:
    """Create a filter that allows log levels in the given closed interval."""

    def _filter(record: logging.LogRecord) -> bool:
        return min_level <= record.levelno <= max_level

    return _filter


def _init_stream_handler(
    stream: TextIO,
    level: int,
    log_filter: Callable[[logging.LogRecord], bool],
) -> logging.StreamHandler[TextIO]:
    """Initialise a `StreamHandler` for logging with a level filter."""
    handler = logging.StreamHandler(stream)
    handler.setLevel(level)
    handler.addFilter(log_filter)
    return handler


class Logger(logging.Logger):
    """Handle logging for proselint."""

    @staticmethod
    def setup(*, verbose: bool = False) -> None:
        """Initialise the logger."""
        base_handler = _init_stream_handler(
            stdout,
            logging.DEBUG if verbose else logging.INFO,
            _level_clamp_filter(max_level=logging.INFO),
        )
        err_handler = _init_stream_handler(
            stderr,
            logging.WARNING,
            _level_clamp_filter(min_level=logging.WARNING),
        )

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
