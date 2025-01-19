"""Tests for the clear cache operation from proselint.command_line."""

from unittest import mock

from proselint import memoizer
from proselint.config_paths import cache_user_path


@mock.patch("shutil.rmtree")
def test_rm_cache(mock_rmtree):
    """Correct directory is removed."""
    memoizer.cache.clear()
    mock_rmtree.assert_called_with(cache_user_path)


@mock.patch("shutil.rmtree", side_effect=PermissionError)
def test_no_permission(mock_rmtree):
    """Ignore if unable to delete."""
    memoizer.cache.clear()


@mock.patch("shutil.rmtree", side_effect=OSError)
def test_on_oserror(mock_rmtree):
    """Ignore if general OSError."""
    memoizer.cache.clear()
