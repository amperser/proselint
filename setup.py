"""Installation script for proselint."""

from setuptools import setup

setup(
    name='proselint',
    version='0.1',
    description='Making your writing better',
    url='http://github.com/suchow/proselint',
    author='Jordan Suchow',
    author_email='suchow@post.harvard.edu',
    license='MIT',
    packages=[
        'proselint',
        'proselint.checks',
        'proselint.checks.misc',
        'proselint.checks.consistency',
        'proselint.checks.pinker',
        'proselint.checks.strunkwhite',
        'proselint.checks.garner',
        'proselint.checks.writegood',
        'proselint.checks.wallace',
        'proselint.checks.wallstreetjournal',
        'proselint.checks.butterick'],
    package_data={'': ['demo.md', '.proselintrc']},
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'proselint = proselint.command_line:proselint',
        ],
    })
