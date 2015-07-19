Work on proselint happens over at http://github.com/amperser/proselint. To contribute, create a new branch off of master and then open a pull request. You code should run cleanly through pep8 and pep257 linters. Comments, bug reports, and other feedback can be provided through GitHub issues.

To create a new check:
0. Pick a name for your check, e.g., `misc.abc_checkname`.
1. Create a copy of `checks/inprogress/example_check.py`, renaming it to `abc_checkname.py` and placing it in `checks/misc/`.
2. Edit your check.
3. Create a new test file `test_abc_checkname.py` and place it in `tests`.
4. Run the test suite using `nosetests`.
5. Submit a pull request to amperser/proselint.
