"""
shows usage of proselint in your own scripts

Note: when combining multiprocessing (parallelize option) on windows
      the calling script must be encapsulated in 'if __name__ == '__main__''
      as long as python updates its processing-implementation.
      py312 is still unchanged.

"""
from pathlib import Path

import proselint.tools as plt

if __name__ == "__main__":
    # direct text input
    results = plt.lint("This sentence contains a clear as mud error")

    # result is a list of LintResult tagged tuples with all essential data included
    print("\n## Custom Error-Printing")
    for item in results:
        print(f"{item.line}:{item.column}: {item.message}")

    # it's also possible to use builtin comfort-functions
    # for output to json or print to console
    print("\n## Output as JSON")
    print(plt.convert_to_json(results))

    print("\n## Default Error Printing")
    plt.print_to_console(results)

    # text from file - v1
    print("\n## Linting a file")

    file = Path(__file__).parent.parent / "proselint/demo.md"
    with file.open() as f_handle:
        text = f_handle.read()
    result1 = plt.lint(text)
    print(f"V1 found {len(result1)} warnings")

    # text from file - v2
    result2 = plt.lint_path(file)
    print(f"V2 found {len(result2)} files")
    for _fname, _warnings in result2.items():
        print(f"- {_fname.name} has {len(_warnings)} warnings")
