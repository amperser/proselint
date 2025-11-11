"""Handle logging for proselint."""

from __future__ import annotations

import logging
from enum import Enum, IntEnum
from json import dump
from sys import stderr, stdout
from typing import TYPE_CHECKING, NamedTuple, TextIO, cast

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    from proselint.tools import LintResult


class OutputFormat(str, Enum):
    """The format to output results in."""

    FULL = "full"
    JSON = "json"
    COMPACT = "compact"


class LogLevel(IntEnum):
    """Log levels as in `logging`."""

    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


class ErrorCode(IntEnum):
    """Error codes for Proselint, adherent to the LSP specification."""

    Unknown = -31999
    FileError = -31998
    LintError = -31997


class ResponseError(NamedTuple):
    """An LSP error object."""

    code: int
    message: str
    data: object | None = None

    @staticmethod
    def from_exception(err: Exception) -> ResponseError:
        """Create a `ResponseError` from an `Exception`."""
        data = None
        match err:
            case FileNotFoundError() | PermissionError():
                err_code = ErrorCode.FileError
            case _:
                err_code = ErrorCode.Unknown
                data = type(err).__name__
        return ResponseError(code=err_code, message=str(err), data=data)

    def into_dict(self) -> dict[str, object]:
        """Convert `self` into a dictionary, omitting `data` if it is `None`."""
        result = self._asdict()
        if self.data is None:
            del result["data"]
        return result


def _init_stream_handler(
    stream: TextIO,
    level: int,
    log_filter: Callable[[logging.LogRecord], bool],
    formatter: logging.Formatter,
) -> logging.StreamHandler[TextIO]:
    """Initialise a `StreamHandler` for logging with a level filter."""
    handler = logging.StreamHandler(stream)
    handler.setLevel(level)
    handler.setFormatter(formatter)
    handler.addFilter(log_filter)
    return handler


BASE_HANDLER = _init_stream_handler(
    stdout,
    logging.INFO,
    lambda record: record.levelno == logging.INFO,
    logging.Formatter("%(message)s"),
)


class Logger(logging.Logger):
    """Handle logging for proselint."""

    fmt: OutputFormat
    verbose: bool
    collector: dict[str, dict[str, object]]

    def __init__(self, name: str, level: LogLevel = LogLevel.NOTSET) -> None:
        """Initialise the logger."""
        super().__init__(name, level)
        self.fmt = OutputFormat.FULL
        self.verbose = False
        self.collector = {}

    def setup(self, *, fmt: OutputFormat, verbose: bool) -> None:
        """Configure the logger."""
        self.fmt = fmt
        self.verbose = verbose

        err_handler = _init_stream_handler(
            stderr,
            logging.DEBUG,
            lambda record: record.levelno != logging.INFO
            and fmt != OutputFormat.JSON,
            logging.Formatter(
                (
                    "[%(asctime)s][proselint::%(module)s][%(levelname)s]"
                    " %(message)s"
                )
                if verbose
                else "%(message)s",
                "%Y-%m-%d %H:%M:%S",
            ),
        )
        self.setLevel(logging.DEBUG if verbose else logging.INFO)
        self.handlers.clear()
        self.addHandler(BASE_HANDLER)
        self.addHandler(err_handler)

    def format_source(self, source: Path | str) -> str:
        """Format the source name dependent on the output format."""
        if isinstance(source, str):
            return source
        match self.fmt:
            case OutputFormat.JSON:
                return source.resolve().as_uri()
            case OutputFormat.FULL:
                return source.resolve().as_posix()
            case _:
                return source.name

    @staticmethod
    def write_dict(data: dict[str, object]) -> None:
        """Write a dictionary to standard output, serialized as JSON."""
        dump(data, stdout, indent=2, sort_keys=True)

    def write_results(self, source: str, results: list[LintResult]) -> None:
        """Print or store results from a `LintFile`."""
        if self.fmt == OutputFormat.JSON:
            self.collector[source] = {
                "diagnostics": [result.into_dict() for result in results]
            }
            return

        for result in results:
            self.info(
                "%s:%s:%s: %s: %s",
                source,
                result.pos[0],
                result.pos[1],
                result.check_result.check_path,
                result.check_result.message,
            )

    def write_lint_exception(self, source: str, err: ResponseError) -> None:
        """Print an error encountered while linting a file."""
        if self.fmt == OutputFormat.JSON:
            self.collector[source] = {"error": err.into_dict()}
            return

        self.error(
            "Error encountered while linting %s: %s", source, err.message
        )

    def write_error(self, err: ResponseError) -> None:
        """Print an unrecoverable error."""
        if self.fmt == OutputFormat.JSON:
            Logger.write_dict({"error": err.into_dict()})
            return

        self.error(
            "Unrecoverable error encountered while running proselint: %s",
            err.message,
        )

    def flush(self) -> None:
        """Ensure logs are written."""
        if self.fmt == OutputFormat.JSON:
            Logger.write_dict({"result": self.collector})


logging.setLoggerClass(Logger)
log = cast("Logger", logging.getLogger("proselint"))
