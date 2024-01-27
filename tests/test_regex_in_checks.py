from __future__ import annotations

import importlib
import re
from typing import Optional

import pytest

import proselint
from proselint.checks import Pd
from proselint.checks import ResultCheck
from tests.test_checks import get_module_names

# ##### MOCK-Functions


def verify_regex_padding(regex: list[str], padding: str) -> None:
    assert isinstance(regex, list)
    assert isinstance(padding, str)
    assert all(
        isinstance(_e, str) for _e in regex
    ), f"all elements in list must be strings ({regex[:5]})"

    if padding == Pd.sep_in_txt.value:
        # if all elements start&end with alpha/num we can optimize
        assert not all(
            _e[0].isalnum() and _e[-1].isalnum() for _e in regex
        ), f"Choose Pd.words_in_txt for {regex[:5]}[...] as optimization for check()"

    if padding == Pd.words_in_txt.value:
        # any element without num or alpha at start AND end should fail
        for _e in regex:
            assert (
                _e[0].isalnum() and _e[-1].isalnum()
            ), f"Choose Pd.sep_in_txt for '{_e}' to fix check()"


def mock_preferred_forms_check_regex(
    text: str,
    items: list,
    err: str,
    msg: str,
    ignore_case: bool = True,
    offset: tuple[int, int] = (0, 0),
    padding: str = Pd.words_in_txt,
) -> list[ResultCheck]:
    _ilist = []
    for item in items:
        _ilist.extend(item[1])
    verify_regex_padding(_ilist, padding)
    return []


# TODO: update with new one
def mock_preferred_forms_check_opti(
    text: str,
    items: dict[str, str],
    err: str,
    msg: str,
    ignore_case: bool = True,
    offset: tuple[int, int] = (0, 0),
    padding: str = Pd.words_in_txt,
) -> list:
    _ilist = list(items.keys())
    verify_regex_padding(_ilist, padding)
    return []


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
) -> list[ResultCheck]:
    verify_regex_padding(re_items, padding)
    return []


# ######### Unittests


@pytest.mark.parametrize("module_name", get_module_names())
def test_regex_in_checks(module_name: str, monkeypatch) -> None:
    monkeypatch.setattr(
        proselint.checks,
        "preferred_forms_check_regex",
        mock_preferred_forms_check_regex,
    )
    monkeypatch.setattr(
        proselint.checks, "preferred_forms_check_opti", mock_preferred_forms_check_opti
    )
    monkeypatch.setattr(proselint.checks, "existence_check", mock_existence_check)

    try:
        module = importlib.import_module("." + module_name, "proselint")
    except ModuleNotFoundError as _xpt:
        raise ImportError(f"Is {module_name} broken?") from _xpt

    checks = {d: getattr(module, d) for d in dir(module) if re.match(r"^check", d)}

    for check in checks.values():  # any-config
        check("smokey")

    monkeypatch.undo()

    # TODO: assemble list with xeger, and test here again
    # https://github.com/leapfrogonline/rstr
