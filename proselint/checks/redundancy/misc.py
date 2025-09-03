"""Redundancy."""

from importlib.resources import files

from proselint.backports import batched
from proselint.checks import redundancy
from proselint.registry.checks import BATCH_COUNT, Check, types

CHECK_MESSAGE = "Redundancy. Use '{}' instead of '{}'."

GARNER_RAW = (files(redundancy) / "garner").read_text().splitlines()
AFTER_THE_DEADLINE_RAW = (
    (files(redundancy) / "after-the-deadline").read_text("utf8").splitlines()
)

check_wallace = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "rectangular in shape": "rectangular",
            "audible to the ear": "audible",
        }
    ),
    path="redundancy.misc.wallace",
    message="Redundancy. Use '{}' instead of '{}'.",
)

"""
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
"""
check_garner_regex = Check(
    check_type=types.PreferredForms(
        items={
            "(?:general )?consensus of opinion": "consensus",
            "associate together(?: in groups)?": "associate",
        }
    ),
    path="redundancy.misc.garner",
    message=CHECK_MESSAGE,
)

"""
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
"""
check_garner = Check(
    check_type=types.PreferredFormsSimple(
        items=dict(line.split(",", maxsplit=1) for line in GARNER_RAW)
    ),
    path="redundancy.misc.garner",
    message="Redundancy. Use '{}' instead of '{}'.",
)


"""
source:     Richard Nordquist
source_url: http://grammar.about.com/bio/Richard-Nordquist-22176.htm
"""
check_nordquist = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "absolutely essential": "essential",
            "absolutely necessary": "necessary",
            r"a\.m\. in the morning": r"a\.m\.",
            r"p\.m\. at night": r"p\.m\.",
        }
    ),
    path="redundancy.misc.nordquist",
    message="Redundancy. Use '{}' instead of '{}'.",
)

# TODO: review commented entries
# "first and foremost": "foremost",
# "former graduate": "graduate",
# "has got": "has",
# "have got": "have",
# "he himself": "he",
# "indicted on a charge": "indicted",
# "input into": "input",
# "last of all": "last",
# "later time": "later",
# "bare naked": "naked",
# "protrude out": "protrude",
# "close proximity": "proximity",
# "raise up": "raise",
# "highly relevant": "relevant",
# "necessary requirements": "requirements",
# "slow speed": "slow",
# "small size": "small",
# "they themselves": "they",
# "undeniable truth": "undeniable",
# "unintentional mistake": "unintentional",
checks_after_the_deadline = tuple(
    Check(
        check_type=types.PreferredFormsSimple(
            items=dict(line.split(",", maxsplit=1) for line in lines)
        ),
        path="redundancy.misc.after_the_deadline",
        message="Redundancy. Use '{}' instead of '{}'.",
    )
    for lines in batched(AFTER_THE_DEADLINE_RAW, BATCH_COUNT)
)

__register__ = (
    check_wallace,
    check_garner,
    check_garner_regex,
    check_nordquist,
    *checks_after_the_deadline,
)
