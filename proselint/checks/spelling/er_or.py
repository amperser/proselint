"""-er vs. -or."""

from __future__ import annotations

from proselint.tools import ResultCheck, memoize, preferred_forms_check


@memoize
def check(text: str) -> list[ResultCheck]:
    """-er vs. -or."""
    err = "spelling.er_or"
    msg = "-er vs. -or. '{}' is the preferred spelling."

    preferences = [

        ["abductor",            ["abducter"]],
        ["abettor",             ["abbeter"]],
        ["acquirer",            ["acquiror"]],
        ["adapter",             ["adaptor"]],
        ["collector",           ["collecter"]],
        ["conjurer",            ["conjuror"]],
        ["corrupter",           ["corruptor"]],
        ["digester",            ["digestor"]],
        ["dispenser",           ["dispensor"]],
        ["distributor",         ["distributer"]],
        ["endorser",            ["endorsor"]],
        ["eraser",              ["erasor"]],
        ["idolater",            ["idolator"]],
        ["impostor",            ["imposter"]],
        ["infiltrator",         ["infiltrater"]],
        ["investor",            ["invester"]],
        ["manipulator",         ["manipulater"]],
        ["mortgagor",           ["mortgager"]],
        ["persecutor",          ["persecuter"]],
        ["promoter",            ["promotor"]],
        ["promoter",            ["promotor"]],
        ["purveyor",            ["purveyer"]],
        ["requester",           ["requestor"]],
        ["reviser",             ["revisor"]],
        ["surveyor",            ["surveyer"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
