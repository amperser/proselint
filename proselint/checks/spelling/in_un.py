"""in- vs. un-."""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "unadvisable": "inadvisable",
            "unalienable": "inalienable",
            "unexpressive": "inexpressive",
            "unfeasible": "infeasible",
        }
    ),
    path="spelling.in_un",
    message="in- vs. un-. '{}' is the preferred spelling.",
)

__register__ = (check,)
