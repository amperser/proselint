"""Handle logging for proselint."""

import logging
from sys import stderr, stdout


class Logger(logging.Logger):
    """Handle logging for proselint."""

    @staticmethod
    def setup(*, verbose: bool = False) -> None:
        """Initialise the logger."""
        base_handler = logging.StreamHandler(stdout)
        err_handler = logging.StreamHandler(stderr)

        base_handler.setLevel(logging.DEBUG if verbose else logging.INFO)
        err_handler.setLevel(logging.WARNING)
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
