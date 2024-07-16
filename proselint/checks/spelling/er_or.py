"""-er vs. -or."""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "She met with the invester.",
]

check = CheckSpec(
    PreferredFormsSimple({
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
    }),
    "spelling.er_or",
    "-er vs. -or. '{}' is the preferred spelling.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
