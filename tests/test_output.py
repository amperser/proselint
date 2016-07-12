"""Check that the CLI prints output in the right format"""

import subprocess

def test_output_sorted():
    """Ensure that the output is sorted by line & column number"""

    def extract_line_col(line):
        pieces = line.split(":")
        return (int(pieces[1]), int(pieces[2])) # line number, column number

    try:
        output = subprocess.run(["proselint", "--demo"], stdout=subprocess.PIPE, universal_newlines=True).stdout
        lines = output.split("\n")[:-1] # last line is empty
        numbers = [extract_line_col(line) for line in lines]
        assert sorted(numbers) == numbers

    except subprocess.CalledProcessError:
        assert(False)
