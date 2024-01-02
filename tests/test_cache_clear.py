"""Tests for the clear cache operation from proselint.command_line."""

from unittest import mock

import proselint.lint_cache
from proselint.config_paths import cache_user_path


@mock.patch("shutil.rmtree")
def test_rm_cache(mock_rmtree):
    """Correct directory is removed."""
    proselint.lint_cache.cache.clear()
    mock_rmtree.assert_called_with(cache_user_path)


@mock.patch("shutil.rmtree", side_effect=PermissionError)
def test_no_permission(mock_rmtree):
    """Ignore if unable to delete."""
    proselint.lint_cache.cache.clear()


@mock.patch("shutil.rmtree", side_effect=OSError)
def test_on_oserror(mock_rmtree):
    """Ignore if general OSError."""
    proselint.lint_cache.cache.clear()
