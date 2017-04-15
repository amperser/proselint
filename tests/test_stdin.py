"""Run the demo."""

from click.testing import CliRunner
from proselint.command_line import proselint, demo_file

runner = CliRunner()
demo = runner.invoke(proselint, ['--demo'])

with open(demo_file) as f:
    stdin = runner.invoke(proselint, ['--stdin'], input=f.read())

assert stdin.output == demo.output.replace(demo_file, 'stdin')
