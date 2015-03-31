<img src="logo.png" alt="proselint logo" width="200">

`proselint` places the world's greatest writers and editors by your side, where they whisper suggestions on how to improve your prose. You'll be guided by Bryan Garner, David Foster Wallace, Mark Twain, Chuck Palahniuk, Steve Pinker, Mary Norris, Elmore Leonard, Matthew Butterick, William Strunk, E.B. White, Philip Corbett, and the editorial staff of various literary magazines and newspapers. Others are on their way and will arrive shortly. Our goal is to aggregate knowledge about best practices in writing and to make that knowledge immediately accessible to all authors in the form of a linter for prose. We call it `proselint`.

`proselint` is a command-line utility and web API that can be integrated into existing tools.
 
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
    // Type of check that output this suggestion.
    check: "wallace.uncomparables",

    // Message to describe the suggestion.
    message: "Comparison of an uncomparable: 'unique' can not be compared.",

    // The person or organization giving the suggestion.
    source: "David Foster Wallace"

    // URL pointing to the source material.
    source_url: "http://www.telegraph.co.uk/a/9715551"

    // Line where the error starts.
    line: 0,

    // Column where the error starts.
    column: 10,

    // Index in the text where the error starts.
    start: 10,

    // Index in the text where the error ends.
    end: 21,

    // start - end
    extent: 11,

    // How important is this? Can be "suggestion", "warning", or "error".
    severity: "warning",

    // Possible replacements.
    replacements: [
        {
            value: "unique"
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
