from __future__ import annotations

import importlib
import re
from typing import Optional

import pytest
import rstr

import proselint
from proselint.checks import CheckResult, CheckSpec, Pd
from tests.test_checks import get_module_names


def generate_examples(items: list[str]) -> list[CheckResult]:
    results: list[CheckResult] = []
    for item in items:
        example = rstr.xeger(item)
        results.append(
            CheckResult(
                start_pos=0,
                end_pos=100,
                check="mock",
                message=f"Smoke phrase with something {example} flagged.",
                replacements=None,
            )
        )
    return results


def verify_regex_padding(regex: list[str], padding: str) -> None:
    assert isinstance(regex, list)
    assert isinstance(padding, str)
    assert all(
        isinstance(_e, str) for _e in regex
    ), f"all elements in list must be strings ({regex[:5]})"

    examples = [rstr.xeger(_e) for _e in regex]
    if padding == Pd.sep_in_txt.value:
        # if all elements start&end with alpha/num we can optimize
        assert not all(
            _x[0].isalnum() and _x[-1].isalnum() for _x in examples
        ), f"Choose Pd.words_in_txt for {regex[:5]}[...] as optimization for check()"

    if padding == Pd.words_in_txt.value:
        # any element without num or alpha at start AND end should fail
        for _i, _x in enumerate(examples):
            assert (
                _x[0].isalnum() and _x[-1].isalnum()
            ), f"Choose Pd.sep_in_txt for '{regex[_i]}' to fix check()"


# ##### MOCK-Functions


def mock_preferred_forms_check_regex(
    text: str,
    items: dict[str, str],
    err: str,
    msg: str,
    ignore_case: bool = True,
    offset: tuple[int, int] = (0, 0),
    padding: str = Pd.words_in_txt,
) -> list[CheckResult]:
    item_list = list(items.keys())
    verify_regex_padding(item_list, padding)
    return generate_examples(item_list)


def mock_preferred_forms_check_opti(
    text: str,
    items: dict[str, str],
    err: str,
    msg: str,
    ignore_case: bool = True,
    offset: tuple[int, int] = (0, 0),
    padding: str = Pd.words_in_txt,
) -> list[CheckResult]:
    item_list = list(items.keys())
    # items can't contain any active regex - tested here:
    for item in item_list:
        _rev = rstr.xeger(item)
        assert _rev == item, (
            "items for preferred_forms_check_opti() "
            f"can't contain regex, here '{item}' for {err}"
        )
    return generate_examples(item_list)


def mock_existence_check(
    text: str,
    re_items: list,
    err: str,
    msg: str,
    ignore_case: bool = True,
    string: bool = False,
    offset: tuple[int, int] = (0, 0),
    padding: Pd = Pd.words_in_txt,
    dotall: bool = False,
    excluded_topics: Optional[list] = None,
    exceptions=(),
) -> list[CheckResult]:
    verify_regex_padding(re_items, padding)
    return generate_examples(re_items)


def mock_existence_check_simple(
    text: str,
    pattern: str,
    err: str,
    msg: str,
    ignore_case: bool = True,
    unicode: bool = True,
    exceptions=(),
) -> list[CheckResult]:
    items = [pattern]
    return generate_examples(items)


# ######### Unittests


@pytest.mark.parametrize("module_name", get_module_names())
def test_regex_in_checks(module_name: str, monkeypatch) -> None:
    # first: intercept regex-items, test them and get reverse-regex as example-data
    monkeypatch.setattr(
        proselint.checks,
        "preferred_forms_check_regex",
        mock_preferred_forms_check_regex,
    )
    monkeypatch.setattr(
        proselint.checks,
        "preferred_forms_check_opti",
        mock_preferred_forms_check_opti,
    )
    monkeypatch.setattr(
        proselint.checks, "existence_check", mock_existence_check
    )
    monkeypatch.setattr(
        proselint.checks, "existence_check_simple", mock_existence_check_simple
    )

    try:
        module = importlib.import_module("." + module_name, "proselint")
    except ModuleNotFoundError as _xpt:
        raise ImportError(f"Is {module_name} broken?") from _xpt

    checks: dict[str, CheckSpec] = {
        d: getattr(module, d) for d in dir(module) if re.match(r"^check", d)
    }

    examples: list[CheckResult] = []
    for check in checks.values():  # any-config
        # reverse regex-action happening here
        examples.extend(check.dispatch_with_flags("smokey"))

    monkeypatch.undo()

    # second: test checks with generated example data
    for example in examples:
        _xmp = example.message
        print(_xmp)
        errors: list = []
        for check in checks.values():
            errors.extend(check.dispatch_with_flags(_xmp))
        assert (
            len(errors) > 0
        ), f"False negative for {module_name} processing '{_xmp}'"
