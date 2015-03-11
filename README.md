# proselint

`proselint` places the world's greatest writers and editors by your side, where they whisper suggestions on how to improve your prose.

To get this up and running as a command line utility, run `python setup.py develop` from inside the root directory.

## Creating a new check
0. Pick a name for your check, e.g., `abc_checkname`.
1. Create a copy of `checks/inprogress/example_check.py`, renaming it `abc_checkname.py` and placing it in `checks/inprogress/`.
2. Edit your check.
3. Create a new test file `test_abc_checkname.py` and place it in `tests`.
4. Run the test suite using `nosetests`.
5. Submit a pull request to suchow/proselint.
