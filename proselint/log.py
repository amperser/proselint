"""Handle logging for proselint."""

from __future__ import annotations

import logging
from enum import Enum
from sys import stderr, stdout
from typing import TYPE_CHECKING, TextIO, cast

if TYPE_CHECKING:
    from collections.abc import Callable


class OutputFormat(str, Enum):
    """The format to output results in."""

    FULL = "full"
    JSON = "json"
    COMPACT = "compact"


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
            logging.INFO,
            lambda record: record.levelno == logging.INFO,
        )
        err_handler = _init_stream_handler(
            stderr,
            logging.DEBUG,
            lambda record: record.levelno != logging.INFO,
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
log = cast("Logger", logging.getLogger("proselint"))
