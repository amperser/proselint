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
import logging.handlers

# TODO: maybe use with rich to allow links

log = logging.getLogger("proselint")
log.setLevel(logging.INFO)
# log.propagate = 0

logging.basicConfig(format="%(message)s")

# console_handler = logging.StreamHandler(sys.stderr)
# console_handler.setLevel(logging.INFO)
# log.addHandler(console_handler)


def set_verbosity(*, debug: bool = False) -> None:
    """Set the logger's verbose mode."""
    if debug:
        log.setLevel(logging.DEBUG)
        logging.basicConfig(format="%(name)s %(levelname)s: %(message)s")
    else:
        log.setLevel(logging.INFO)
        logging.basicConfig(format="%(message)s", force=True)
        # only needed in debug mode:
        # logging._srcfile = None
        # logging.logThreads = 0
        # logging.logProcesses = 0


def get_verbosity() -> bool:
    """Check if the logger is in verbose mode."""
    return log.level == logging.DEBUG
