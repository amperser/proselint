<img src="logo.png" alt="proselint logo" width="200">

[![Build Status](https://magnum.travis-ci.com/suchow/proselint.svg?token=ygVLzsadbn3UbxEk8GzT&branch=master)](https://magnum.travis-ci.com/suchow/proselint)
[![Code Climate](https://codeclimate.com/repos/5538989ee30ba0793100090f/badges/e10a2fe18a9256d69e2a/gpa.svg)](https://codeclimate.com/repos/5538989ee30ba0793100090f/feed)
[![Coverage Status](https://coveralls.io/repos/suchow/proselint/badge.svg?branch=master&service=github&t=V9yd9l)](https://coveralls.io/github/suchow/proselint?branch=master)
![Lint score](http://img.shields.io/badge/lint_score-98.8,_v0.1.0-blue.svg)

`proselint` places the world's greatest writers and editors by your side, where they whisper suggestions on how to improve your prose. You'll be guided by Bryan Garner, David Foster Wallace, Mark Twain, Chuck Palahniuk, Steve Pinker, Mary Norris, Elmore Leonard, Matthew Butterick, William Strunk, E.B. White, Philip Corbett, and the editorial staff of the world's finest literary magazines and newspapers. Others are on their way and will arrive shortly. Our goal is to aggregate knowledge about best practices in writing and to make that knowledge immediately accessible to all authors in the form of a linter for prose. We call it `proselint`.

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
| `butterick.symbols` | Using the right symbol |
| `consistency.spacing` | Consistent sentence spacing |
| `consistency.spelling` | Consistent use of British vs. American spelling |
| `garner.a_vs_an` | Using 'a' vs. 'an' as a determiner  |
| `garner.airlinese ` | Avoiding jargon of the airline industry |
| `garner.animal_labels` | Likening things to animals using fun words |
| `garner.archaism` | Avoiding archaic forms |
| `garner.back_formations` | Avoiding needless backformations |
| `garner.capitalization` | Captializing what ought to be capitalized |
| `garner.cliches` | Avoiding cliché |
| `garner.commercialese` | Avoiding jargon of the commercial world |
| `garner.dates` | Stylish formatting of dates |
| `garner.denizen_labels` | Calling people the right names |
| `garner.illogic` | Avoiding illogical forms |
| `garner.jargon` | Avoiding miscellaneous jargon |
| `garner.malaproprisms` | Avoiding common malaproprisms |
| `garner.many_a` | Many a singular |
| `garner.misspelling` | Avoiding common misspellings missed by spellcheck |
| `garner.mixed_metaphors` | Not mixing metaphors |
| `garner.needless_variants` | Using the preferred form |
| `garner.oxymorons` | Aoviding oxymorons |
| `garner.preferred_forms` | Miscellaneous preferred forms |
| `garner.punctuation` | Using the right punctuation |
| `garner.redundancy` | Avoiding redunancy |
| `garner.sexism` | Avoiding sexist language |
| `leonard.exclamation` | Avoiding hyperbolic use of exclamation |
| `leonard.hell` | Avoiding a common cliche |
| `misc.annotations` | Catching annotations left in the text |
| `misc.chatspeak` | ... |
| `misc.credit_card` | |
| `misc.currency` | |
| `misc.hyperbolic` | |
| `misc.link_checker` | |
| `misc.password` | |
| `nordquist.redundancy` | |
| `norris.denizen_labels` | |
| `ogilvy.pretension` | |
| `orwell.debased` | |
| `palahniuk.suddenly` | |
| `pinker.apologizing` | |
| `pinker.hedging` | |
| `pinker.latin` | |
| `pinker.metaconcepts` | |
| `pinker.narcisissm` | |
| `pinker.scare_quotes` | |
| `strunk_white.composition` | |
| `strunk_white.greylist` | |
| `strunk_white.usage` | |
| `twain.damn` | |
| `wallace.tense_present` | |
| `wallace.uncomparables` | |
| `write_good.cliches` | |
| `write_good.lexical_illusions` | |
| `write_good.weasel_words` | |
| `wsj.athletes` | |
### Contributing

We'd love to accept your patches and contributions to improve `proselint`. Learn more about how to contribute in [CONTRIBUTING.md](./CONTRIBUTING.md).
