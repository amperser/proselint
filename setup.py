"""Installation script for proselint."""

import io
import os
from setuptools import setup, find_packages

from proselint.version import __version__

DESCRIPTION = "A linter for prose."

base_url = 'http://github.com/amperser/proselint'

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name='proselint',
    version=__version__,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=base_url,
    download_url="{}/tarball/{}".format(base_url, __version__),
    author='Amperser Labs',
    author_email='hello@amperser.com',
    license='BSD',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={'': ['demo.md', '.proselintrc']},
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'proselint = proselint.command_line:proselint',
        ],
    },
    install_requires=[
        'click',
        'future',
        'six'
    ])
