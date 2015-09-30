"""Installation script for proselint."""

from setuptools import setup
from proselint.version import __version__

base_url = 'http://github.com/amperser/proselint'

setup(
    name='proselint',
    version=__version__,
    description='A linter for prose',
    url=base_url,
    download_url="{}/tarball/{}".format(base_url, __version__),
    author='Amperser Labs',
    author_email='hello@amperser.com',
    license='BSD',
    packages=[
        'proselint',
        'proselint.checks',
        'proselint.checks.misc',
        'proselint.checks.consistency',
        'proselint.checks.pinker',
        'proselint.checks.strunk_white',
        'proselint.checks.garner',
        'proselint.checks.write_good',
        'proselint.checks.wallace',
        'proselint.checks.wsj',
        'proselint.checks.butterick'],
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
