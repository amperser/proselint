#!/bin/bash

# This script runs the same commands that are run for each pull request before it
# can be merged.
#
# Run this script before you open a pull request to make sure your changes are good.

if ! which pep257 >/dev/null; then
    echo -e "pep257 is not installed. Please install it with 'pip install pep257'."
    exit 1
fi

if ! pep257 . --match='.*\.py'; then
    echo -e "\n\nPEP-257 issues found. Please fix them and re-run this script."
    exit 1
fi

if ! which nosetests >/dev/null; then
    echo -e "nose is not installed. Please install it with 'pip install nose'."
    exit 1
fi

if ! nosetests --with-coverage --cover-package proselint; then
    echo -e "\n\nSome tests failed. Please fix them and re-run this script."
    exit 1
fi

echo -e "\n\nSuccess! Your pull request looks good to submit."