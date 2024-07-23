from __future__ import annotations

from copy import deepcopy
from importlib import import_module
from typing import TYPE_CHECKING
from unittest import mock

import pytest

from proselint.checks import CheckRegistry, CheckSpec
from tests.test_checks import extract_checks, get_module_names, verify_module

if TYPE_CHECKING:
    from types import ModuleType


def test_singleton() -> None:
    """Ensure that the check registry has one global instance."""
    pass


original_import = deepcopy(import_module)


def import_proxy(name: str, package: str) -> ModuleType:
    """Proxy for mocking importlib.import_module without breaking things."""
    return original_import(name, package)


def register_proxy(self: CheckRegistry, checks: tuple[CheckSpec, ...]) -> None:
    """Proxy for mocking CheckRegistry.register_many without breaking things."""
    self._checks.extend(checks)


@mock.patch(
    "proselint.checks.CheckRegistry.register_many",
    autospec=True,
    side_effect=register_proxy,
)
def test_discover_once(mock_register_many: mock.Mock) -> None:
    """Ensure that discovery happens exactly once."""
    registry = CheckRegistry()
    registry.discover()
    assert mock_register_many.call_count > 0, "Registry did not occur."
    assert len(registry._checks) > 0, "Nothing was registered."
    call_count = mock_register_many.call_count
    check_count = len(registry._checks)
    for _ in range(3):
        registry.discover()
    assert (
        mock_register_many.call_count == call_count
    ), "Discovery and registry process occurred more than once."
    assert (
        len(registry._checks) == check_count
    ), "Repeated discovery calls altered the check count."


@mock.patch("importlib.import_module", side_effect=import_proxy)
@mock.patch(
    "proselint.checks.CheckRegistry.register_many",
    autospec=True,
    side_effect=register_proxy,
)
def test_discover_all(
    mock_register_many: mock.Mock, mock_import_module: mock.Mock
) -> None:
    """Ensure that discovery imports and registers all modules."""
    category_names = {module.split(".")[0] for module in get_module_names()}
    registry = CheckRegistry()
    registry.discover()
    assert mock_register_many.call_count == len(
        category_names
    ), "Registry call count is incongruent with check categories."
    assert mock_import_module.call_count == len(
        category_names
    ), "Import count is incongruent with check categories."
    for category_name in category_names:
        mock_import_module.assert_any_call(
            f".{category_name}", "proselint.checks"
        )
        print([check.path for check in registry._checks])
        assert any(
            check.path.split(".")[0] == category_name
            for check in registry._checks
        ), f"{category_name} was not registered."


@pytest.mark.parametrize("module_name", get_module_names())
def test_register_all(module_name: str) -> None:
    """Ensure that all checks in all modules are exported and registered."""
    module = verify_module(module_name)

    assert hasattr(
        module, "__register__"
    ), f"{module_name} has no __register__."
    checks = extract_checks(module)

    index_name = module_name.split(".")[0]
    if module_name != index_name:
        index = verify_module(index_name)
        assert all(
            check in index.__register__ for check in module.__register__
        ), f"{module_name} is not re-exported in {index}"

    registry = CheckRegistry()
    registry.discover()
    for check in checks:
        assert check in module.__register__, f"{check.path} is not exported."
        assert (
            module.__register__.count(check) == 1
        ), f"{check.path} is exported more than once."
        assert check in registry._checks, f"{check.path} was not registered."
        assert (
            registry._checks.count(check) == 1
        ), f"{check.path} was registered more than once."


def test_get_enabled() -> None:
    """Ensure exclusively enabled checks are retrieved."""
    raise NotImplementedError()


def test_granular_selection() -> None:
    """Ensure submodule and check overrides with False are not retrieved."""
    raise NotImplementedError()
