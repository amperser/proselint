from __future__ import annotations

from typing import Optional

import pytest
import rstr

import proselint
from proselint.checks import CheckResult, Pd
from tests.test_checks import extract_checks, get_module_names, verify_module


def generate_examples(items: list[str]) -> list[CheckResult]:
    return [
        CheckResult(
            start_pos=0,
            end_pos=100,
            check="mock",
            message=rstr.xeger(item),
            replacements=None,
        )
        for item in items
    ]


def verify_regex_padding(regex: list[str], padding: str) -> None:
    assert isinstance(regex, list)
    assert isinstance(padding, str)
    assert all(
        isinstance(_e, str) for _e in regex
    ), f"all elements in list must be strings ({regex[:5]})"

    examples = [rstr.xeger(_e) for _e in regex]
    if padding == Pd.sep_in_txt:
        # if all elements start&end with alpha/num we can optimize
        assert not all(
            _x[0].isalnum() and _x[-1].isalnum() for _x in examples
        ), f"Choose Pd.words_in_txt for {regex[:5]}[...] as optimization for check()"

    if padding == Pd.words_in_txt:
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
    offset: tuple[int, int] = (0, 0),
    padding: str = Pd.words_in_txt,
    *,
    ignore_case: bool = True,
) -> list[CheckResult]:
    item_list = list(items.keys())
    verify_regex_padding(item_list, padding)
    return generate_examples(item_list)


def mock_preferred_forms_check_opti(
    text: str,
    items: dict[str, str],
    err: str,
    msg: str,
    offset: tuple[int, int] = (0, 0),
    padding: str = Pd.words_in_txt,
    *,
    ignore_case: bool = True,
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
    offset: tuple[int, int] = (0, 0),
    padding: Pd = Pd.words_in_txt,
    exceptions: tuple = (),
    *,
    ignore_case: bool = True,
    unicode: bool = True,
    dotall: bool = False,
) -> list[CheckResult]:
    verify_regex_padding(re_items, padding)
    return generate_examples(re_items)


def mock_existence_check_simple(
    text: str,
    pattern: str,
    err: str,
    msg: str,
    exceptions=(),
    *,
    ignore_case: bool = True,
    unicode: bool = True,
) -> list[CheckResult]:
    return generate_examples([pattern])


# ######### Unittests


@pytest.mark.parametrize("module_name", get_module_names())
def test_regex_in_checks(
    module_name: str,
    monkeypatch: pytest.MonkeyPatch
) -> None:
    # first: intercept regex-items, test them and get reverse-regex as example data
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

    checks = extract_checks(verify_module(module_name))

    examples: list[CheckResult] = []
    for check in checks:  # any config
        # reverse regex-action happening here
        examples.extend(check.dispatch("smokey"))

    monkeypatch.undo()

    # second: test checks with generated example data
    for example in examples:
        _xmp = example.message
        print(_xmp)
        errors: list = []
        for check in checks:
            errors.extend(check.dispatch(_xmp))
        assert (
            len(errors) > 0
        ), f"False negative for {module_name} processing '{_xmp}'"
