"""Cliches are cliché."""

from importlib.resources import files

from proselint.backports import batched
from proselint.checks import cliches
from proselint.registry.checks import BATCH_COUNT, Check, types

GARNER_CLICHES = (files(cliches) / "garner").read_text().splitlines()
WRITE_GOOD_CLICHES = (files(cliches) / "write-good").read_text().splitlines()
DICTION_CLICHES = (files(cliches) / "diction").read_text().splitlines()

CHECK_MESSAGE = "'{}' is a cliché"

"""
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
"""
check_garner = Check(
    check_type=types.Existence(items=tuple(GARNER_CLICHES)),
    path="cliches.misc.garner",
    message=CHECK_MESSAGE,
)

"""
source:     write-good
source_url: https://github.com/btford/write-good
"""
checks_write_good = tuple(
    Check(
        check_type=types.Existence(items=items),
        path="cliches.misc.write_good",
        message=CHECK_MESSAGE,
    )
    for items in batched(WRITE_GOOD_CLICHES, BATCH_COUNT)
)

"""
source:     GNU diction
source_url: https://directory.fsf.org/wiki/Diction
"""
check_diction = Check(
    check_type=types.Existence(items=tuple(DICTION_CLICHES)),
    path="cliches.misc.gnu_diction",
    message=CHECK_MESSAGE,
)

__register__ = (check_garner, *checks_write_good, check_diction)
