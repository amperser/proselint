"""Tests for the clear cache operation from proselint.command_line."""

import unittest
from unittest import mock

import proselint.lint_cache
from proselint.config_paths import cache_user_path


class Test__delete_cache(unittest.TestCase):
    """proselint.command_line.__delete_cache()."""

    def setUp(self):
        """Init common data."""
        self.cache_path = cache_user_path

    @mock.patch("shutil.rmtree")
    def test_rm_cache(self, mock_rmtree):
        """Correct directory is removed."""
        proselint.lint_cache.cache.clear()
        mock_rmtree.assert_called_with(self.cache_path)

    @mock.patch("shutil.rmtree", side_effect=PermissionError)
    def test_no_permission(self, mock_rmtree):
        """Ignore if unable to delete."""
        proselint.lint_cache.cache.clear()

    @mock.patch("shutil.rmtree", side_effect=OSError)
    def test_on_oserror(self, mock_rmtree):
        """Ignore if general OSError."""
        proselint.lint_cache.cache.clear()
