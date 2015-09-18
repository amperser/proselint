"""Installation script for proselint."""

from setuptools import setup
from proselint.version import __version__

setup(
    name='proselint',
    version=__version__,
    description='Making your writing better',
    url='http://github.com/amperser/proselint',
    author='Jordan Suchow',
    author_email='suchow@post.harvard.edu',
    license='MIT',
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
    })
