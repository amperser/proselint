"""
Advanced substitute for print().

short reminder for format-strings:
%s    string
%d    decimal
%f    float
%o    decimal as octal
%x    decimal as hex

%05d  pad right (aligned with 5chars)
%-05d pad left (left aligned)
%06.2f    6chars float, including dec point, with 2 chars after
%.5s  truncate to 5 chars

%% for a percent character

"""

import logging
from sys import stdout
from typing import Union

try:
    from rich.logging import RichHandler

    _has_rich = True
except ImportError:
    _has_rich = False


class Logger(logging.Logger):
    def __init__(self, name: str, level: Union[int, str] = 0) -> None:
        super().__init__(name, level)
        self.rich = _has_rich
        self.fancy = False
        # TODO: implement a way to switch to stderr for lint warnings

    def setup(
        self,
        *,
        debug: bool = False,
        fancy: bool = False,
    ) -> None:
        self.fancy = fancy = self.rich and fancy
        if fancy:
            handler = RichHandler(
                markup=True,
                rich_tracebacks=True,
                show_path=False,
                show_time=False,
            )
        else:
            handler = logging.StreamHandler(stdout)

        handler.setLevel(logging.DEBUG if debug else logging.INFO)
        logging.basicConfig(
            level=logging.NOTSET,
            format="[%(levelname)08s] %(name)s: %(message)s"
            if debug and not fancy
            else "%(message)s",
            handlers=[handler],
        )

    def is_verbose(self) -> bool:
        return self.level == logging.DEBUG


logging.setLoggerClass(Logger)
log: Logger = logging.getLogger("proselint")
