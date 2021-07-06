A guide to how you can contribute to proselint can be found on [our website].

Work on proselint happens over at [our GitHub]. To contribute, create a new
branch off master and then open a pull request. Your code should run cleanly
through `pycodestyle` and `pydocstyle` linters (pro tip \- outside of CI,
use `pycodestyle --config=pyproject.toml && pydocstyle -se` for more
descriptive information on what's causing your lint failures). Comments,
bug reports, and other feedback can be provided through GitHub issues.

[our website]: http://proselint.com/contributing
[our GitHub]: http://github.com/amperser/proselint
