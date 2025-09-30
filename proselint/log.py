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
    formatter: logging.Formatter | None = None,
) -> logging.StreamHandler[TextIO]:
    """Initialise a `StreamHandler` for logging with a level filter."""
    handler = logging.StreamHandler(stream)
    handler.setLevel(level)
    handler.setFormatter(formatter)
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
            logging.INFO.__eq__,
        )
        err_handler = _init_stream_handler(
            stderr,
            logging.DEBUG,
            logging.INFO.__ne__,
            logging.Formatter(
                (
                    "[%(asctime)s][proselint::%(module)s][%(levelname)s]"
                    " %(message)s"
                )
                if verbose
                else "%(message)s"
            ),
        )

        logging.basicConfig(handlers=[base_handler, err_handler])


logging.setLoggerClass(Logger)
log = cast("Logger", logging.getLogger("proselint"))
