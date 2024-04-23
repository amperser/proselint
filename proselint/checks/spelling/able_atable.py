"""-able vs. -atable."""

from __future__ import annotations

from proselint.checks import CheckResult
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "There was a demonstratable difference.",
]


def check(text: str) -> list[CheckResult]:
    """-able vs. -atable."""
    err = "spelling.able_atable"
    msg = "-able vs. -atable. '{}' is the preferred spelling."

    items: dict[str, str] = {
        "abbreviatable": "abbreviable",
        "abdicatable": "abdicable",
        "abrogatable": "abrogable",
        "accommodatable": "accommodable",
        "accumulatable": "accumulable",
        "activatable": "activable",
        "administratable": "administrable",
        "adulteratable": "adulterable",
        "affiliatable": "affiliable",
        "aggregatable": "aggregable",
        "agitatable": "agitable",
        "alienatable": "alienable",
        "alleviatable": "alleviable",
        "allocatable": "allocable",
        "amelioratable": "ameliorable",
        "annihilatable": "annihilable",
        "appreciatable": "appreciable",
        "appropriatable": "appropriable",
        "arbitratable": "arbitrable",
        "articulatable": "articulable",
        "calculatable": "calculable",
        "communicatable": "communicable",
        "compensatable": "compensable",
        "confiscatable": "confiscable",
        "corroboratable": "corroborable",
        "cultivatable": "cultivable",
        "delegatable": "delegable",
        "delineatable": "delineable",
        "demonstratable": "demonstrable",
        "detonatable": "detonable",
        "differentiatable": "differentiable",
        "eradicatable": "eradicable",
        "evacuatable": "evacuable",
        "evaluatable": "evaluable",
        "expropriatable": "expropriable",
        "generatable": "generable",
        "indicatable": "indicable",
        "inebriatable": "inebriable",
        "inextirpatable": "inextirpable",
        "inextricatable": "inextricable",
        "infatuatable": "infatuable",
        "infuriatable": "infuriable",
        "invalidatable": "invalidable",
        "investigatable": "investigable",
        "isolatable": "isolable",
        "litigatable": "litigable",
        "manipulatable": "manipulable",
        "medicatable": "medicable",
        "navigatable": "navigable",
        "obligatable": "obligable",
        "obviatable": "obviable",
        "operatable": "operable",
        "originatable": "originable",
        "participatable": "participable",
        "penetratable": "penetrable",
        "perpetratable": "perpetrable",
        "perpetuatable": "perpetuable",
        "predicatable": "predicable",
        "propagatable": "propagable",
        "regulatable": "regulable",
        "replicatable": "replicable",
        "repudiatable": "repudiable",
        "segregatable": "segregable",
        "separatable": "separable",
        "subjugatable": "subjugable",
        "vindicatable": "vindicable",
        "violatable": "violable",
        "vitiatable": "vitiable",
    }

    return preferred_forms_check_opti(text, items, err, msg)
