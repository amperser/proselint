"""-er vs. -or."""

from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "She met with the invester.",
]


def check(text: str) -> list[ResultCheck]:
    """-er vs. -or."""
    err = "spelling.er_or"
    msg = "-er vs. -or. '{}' is the preferred spelling."

    items: dict[str, str] = {
        "abducter": "abductor",
        "abbeter": "abettor",
        "acquiror": "acquirer",
        "adaptor": "adapter",
        "collecter": "collector",
        "conjuror": "conjurer",
        "corruptor": "corrupter",
        "digestor": "digester",
        "dispensor": "dispenser",
        "distributer": "distributor",
        "endorsor": "endorser",
        "erasor": "eraser",
        "idolator": "idolater",
        "imposter": "impostor",
        "infiltrater": "infiltrator",
        "invester": "investor",
        "manipulater": "manipulator",
        "mortgager": "mortgagor",
        "persecuter": "persecutor",
        "promotor": "promoter",
        "purveyer": "purveyor",
        "requestor": "requester",
        "revisor": "reviser",
        "surveyer": "surveyor",
    }

    return preferred_forms_check_opti(text, items, err, msg)
