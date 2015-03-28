<img src="logo.png" alt="proselint logo" width="200">

`proselint` places the world's greatest writers and editors by your side, where they whisper suggestions on how to improve your prose. They include Bryan Garner, Mark Twain, David Foster Wallace, Steve Pinker, Chuck Palahniuk, Elmore Leonard, Matthew Butterick, The Wall Street Journal, William Struk, and E.B. White. Many more are on their way and will shortly arrive. Our goal is to aggregate human knowledge about best practices in writing and to make that knowledge immediately available to all authors in the form of a linter for prose — we call it proselint.

### Installation

To get this up and running as a command line utility, run `python setup.py develop` from inside the root directory.

```
$ python setup.py develop
```

### API

```js
proselint --json
```

The output is a JSON structure with the following format:

```js
{
    // Type of check that output this suggestion
    check: "wallace.uncomparables",

    // Level of importance
    // "suggestion", "warning", "error"
    level: "warning",

    // Line where the error occurred.
    line: 0,

    // Column where the error occurred.
    column: 10,

    // Index in the text
    start: 10,

    // Size of the section in the text
    end: 2,

    // Message to describe the suggestion
    message: "Comparison of an uncomparable: 'very unique' is not comparable.",

    // Replacements suggestion
    replacements: [
        {
            value: ""
        }
    ]
}
```

### Checks

You can disable any of the checks by modifying `.proselintrc`.

| ID    | Description     |
| ----- | --------------- |
| `passive` | Checks for passive voice |
| `lexical-illusion` | Checks for lexical illusions – cases where a word is repeated. |
| `so` | Checks for `so` at the beginning of the sentence. |
| `adverbs` | Checks for adverbs that can weaken meaning: really, very, extremely, etc. |
| `readibility` | Checks for readibility of sentences. |
| `simplicity` | Checks for simpler expressions |
| `weasel` | Checks for "weasel words." |

### Contributing

We'd love to accept your patches and contributions to improve `proselint`. Learn more about how to contribute in [CONTRIBUTING.md](./CONTRIBUTING.md).
