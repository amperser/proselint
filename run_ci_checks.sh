#!/usr/bin/env bash

# This script runs the same commands that are run for each pull request
# before it can be merged. Run this script before you open a pull request
# to make sure your changes are good.

if ! which poetry >/dev/null; then
    echo -e "
poetry is not set up. It is required as our dependency sandbox for proselint.
Please install it from python-poetry.org."
    exit 1
fi

if ! poetry run flake8 proselint || ! poetry run pydocstyle proselint; then
    echo -e "\n\n=== LINT ISSUES FOUND! SEE ABOVE. ==="
    exit 1
fi

if ! poetry run pytest --continue-on-collection-errors; then
    echo -e "\n\n=== TESTS FAILED! SEE ABOVE. ==="
    exit 1
fi

echo -e "\n\nSuccess! Your pull request is ready to submit."
