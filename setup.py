from setuptools import setup

setup(
    name='proselint',
    version='0.1',
    description='Making your writing better',
    url='http://github.com/suchow/ProseLinter',
    author='Jordan Suchow',
    author_email='suchow@post.harvard.edu',
    license='MIT',
    packages=['proselint'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'proselint = proselint.command_line:proselint',
        ],
    })
