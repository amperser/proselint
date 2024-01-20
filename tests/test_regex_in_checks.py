from __future__ import annotations

import importlib
import os
import re
from pathlib import Path
from typing import Optional

import pytest

import proselint
from proselint.checks import Pd, ResultCheck
from tests.test_checks import get_module_names

# ##### MOCK-Functions


def verify_regex_padding(regex: list[str], padding: str) -> None:
    if padding is Pd.sep_in_txt.value:
        # if all elements start&end with alpha/num we can optimize
        assert not all(_e[0].isalnum() and _e[-1].isalnum() for _e in regex), f"Choose Pd.sep_in_txt for {regex[:5]}[...]"

    if padding is Pd.words_in_txt.value:
        # any element without num or alpha at start AND end should fail
        for _e in regex:
            assert _e[0].isalnum() and _e[-1].isalnum(), f"Choose Pd.sep_in_txt for {_e}"



def mock_preferred_forms_check(
    text: str,
    items: list,
    err: str,
    msg: str,
    ignore_case: bool = True,
    offset: tuple[int, int] = (0, 0),
    padding: str = Pd.words_in_txt,
) -> list[ResultCheck]:
    verify_regex_padding(items, padding)
    return []

def mock_preferred_forms_check2_pre(
    items: list, ignore_case: bool = True, padding: str = Pd.words_in_txt
) -> list:
    verify_regex_padding(items, padding)
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
    monkeypatch.setattr(proselint.checks, "preferred_forms_check", mock_preferred_forms_check)
    monkeypatch.setattr(proselint.checks, "preferred_forms_check2_pre", mock_preferred_forms_check2_pre)
    monkeypatch.setattr(proselint.checks, "existence_check", mock_existence_check)

    try:
        module = importlib.import_module("." + module_name, "proselint")
    except ModuleNotFoundError as _xpt:
        raise ImportError(f"Is {module_name} broken?") from _xpt

    checks = {d: getattr(module, d) for d in dir(module) if re.match(r"^check", d)}

    for check in checks.values():  # any-config
        check("smokey")
