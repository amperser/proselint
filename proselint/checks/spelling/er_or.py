"""-er vs. -or."""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
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
    ),
    path="spelling.er_or",
    message="-er vs. -or. '{}' is the preferred spelling.",
)

__register__ = (check,)
