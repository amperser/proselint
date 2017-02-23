# -*- coding: utf-8 -*-
"""Tests for the clear cache operation from proselint.command_line."""

import os
import unittest

from proselint import command_line as cl


try:
    from unittest import mock
except ImportError:
    # Py2.x
    import mock

try:
    from builtins import PermissionError
except ImportError:

    class PermissionError(OSError):
        """Introduced in Py3.3, emulate for earlier versions."""

        def __init__(self, *args, **kwargs):
            """Constructor."""
            OSError.__init__(self, *args, **kwargs)

try:
    from builtins import FileNotFoundError
except ImportError:

    class FileNotFoundError(OSError):
        """Introduced in Py3.3, emulate for earlier versions."""

        def __init__(self, *args, **kwargs):
            """Constructor."""
            OSError.__init__(self, *args, **kwargs)

try:
    from builtins import IsADirectoryError
except ImportError:

    class IsADirectoryError(OSError):
        """Introduced in Py3.3, emulate for earlier versions."""

        def __init__(self, *args, **kwargs):
            """Constructor."""
            OSError.__init__(self, *args, **kwargs)


class Test__delete_compiled_python_files(unittest.TestCase):
    """proselint.command_line._delete_compiled_python_files()."""

    def setUp(self):
        """init common data."""
        self.base_dir = '.'
        self.python_file = 'a.py'
        self.pyc_file = 'a.pyc'
        self.dot_pyc = '.pyc'

        self.files = [
            (self.base_dir, ('dummy',), (self.pyc_file,
                                         self.python_file,
                                         self.dot_pyc))
        ]

        self.pyc_file_path = os.path.join(self.base_dir, self.pyc_file)
        self.python_file_path = os.path.join(self.base_dir, self.python_file)
        self.dot_pyc_path = os.path.join(self.base_dir, self.python_file)

    @mock.patch('os.walk')
    @mock.patch('os.remove')
    def test_delete_pyc_file(self, mock_remove, mock_walk):
        """Ensure 'pyc' files are removed."""
        mock_walk.return_value = self.files

        cl._delete_compiled_python_files()
        mock_remove.assert_called_with(self.pyc_file_path)

    @mock.patch('os.walk')
    @mock.patch('os.remove')
    def test_files_not_deleted(self, mock_remove, mock_walk):
        """Ensure non 'pyc' files are not removed."""
        mock_walk.return_value = self.files
        cl._delete_compiled_python_files()

        with self.assertRaises(AssertionError):
            mock_remove.assert_called_with(self.python_file_path)

        with self.assertRaises(AssertionError):
            mock_remove.assert_called_with(self.dot_pyc_path)

    @mock.patch('os.walk')
    @mock.patch('os.remove', side_effect=PermissionError)
    def test_no_permission(self, mock_remove, mock_walk):
        """Ignore if unable to delete files."""
        mock_walk.return_value = self.files
        cl._delete_compiled_python_files()

    @mock.patch('os.walk')
    @mock.patch('os.remove', side_effect=OSError)
    def test_on_oserror(self, mock_remove, mock_walk):
        """Ignore if OSError."""
        mock_walk.return_value = self.files
        cl._delete_compiled_python_files()

    @mock.patch('os.walk')
    @mock.patch('os.remove', side_effect=FileNotFoundError)
    def test_files_not_found(self, mock_remove, mock_walk):
        """Ignore if file not found."""
        mock_walk.return_value = self.files
        cl._delete_compiled_python_files()

    @mock.patch('os.walk')
    @mock.patch('os.remove', side_effect=IsADirectoryError)
    def test__remove_dir(self, mock_remove, mock_walk):
        """Ignore if attempt to delete a directory."""
        mock_walk.return_value = self.files
        cl._delete_compiled_python_files()


class Test__delete_cache(unittest.TestCase):
    """proselint.command_line.__delete_cache()."""

    def setUp(self):
        """Init common data."""
        self.cache_path = os.path.join("proselint", "cache")

    @mock.patch('shutil.rmtree')
    def test_rm_cache(self, mock_rmtree):
        """Correct directory is removed."""
        cl._delete_cache()
        mock_rmtree.assert_called_with(self.cache_path)

    @mock.patch('shutil.rmtree', side_effect=PermissionError)
    def test_no_permission(self, mock_rmtree):
        """Ignore if unable to delete."""
        cl._delete_cache()

    @mock.patch('shutil.rmtree', side_effect=OSError)
    def test_on_oserror(self, mock_rmtree):
        """Ignore if general OSError."""
        cl._delete_cache()


class Test_create_home_cache(unittest.TestCase):
    """proselint.command_line._create_home_cache()."""

    def setUp(self):
        """Init common data."""
        self.cache_path = os.path.join(os.path.expanduser("~"), ".proselint")

    @mock.patch('os.makedirs')
    def test_makedir(self, mock_makedir):
        """correct directory is used."""
        cl._create_home_cache()
        mock_makedir.assert_called_with(self.cache_path)

    @mock.patch('os.makedirs', side_effect=OSError)
    def test_on_oserror(self, mock_rmtree):
        """Ignore if general OSError."""
        cl._create_home_cache()

    @mock.patch('os.makedirs', side_effect=PermissionError)
    def test__no_permission(self, mock_rmtree):
        """Ignore if unable to delete."""
        cl._create_home_cache()
