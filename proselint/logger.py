import logging
import logging.handlers

try:
    import chromalog

    chromalog.basicConfig(format="%(message)s")
except ImportError:
    chromalog = None

logger = logging.getLogger("proselint")
logger.addHandler(logging.NullHandler())
logger.setLevel(logging.INFO)


def set_verbosity(debug: bool = False) -> None:
    if debug:
        logger.setLevel(logging.DEBUG)
        if chromalog:
            chromalog.basicConfig(format="%(name)s %(levelname)s: %(message)s")
    else:
        logger.setLevel(logging.INFO)
        if chromalog:
            chromalog.basicConfig(format="%(message)s")
        # only needed in debug mode:
        logging._srcfile = None  # noqa: SLF001
        logging.logThreads = 0
        logging.logProcesses = 0



def get_verbosity() -> int:
    return logger.level == "DEBUG"


# short reminder for format-strings:
# %s    string
# %d    decimal
# %f    float
# %o    decimal as octal
# %x    decimal as hex
#
# %05d  pad right (aligned with 5chars)
# %-05d pad left (left aligned)
# %06.2f    6chars float, including dec point, with 2 chars after
# %.5s  truncate to 5 chars
#
# %% for a percent character
