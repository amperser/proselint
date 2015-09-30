<img src="logo.png" alt="proselint logo" width="200">

![Version](https://img.shields.io/badge/version-v0.3.1-yellow.svg)
[![Build Status](https://magnum.travis-ci.com/amperser/proselint.svg?token=ygVLzsadbn3UbxEk8GzT&branch=master)](https://magnum.travis-ci.com/amperser/proselint)
[![Code Climate](https://codeclimate.com/repos/5538989ee30ba0793100090f/badges/e10a2fe18a9256d69e2a/gpa.svg)](https://codeclimate.com/repos/5538989ee30ba0793100090f/feed)
[![Coverage Status](https://coveralls.io/repos/amperser/proselint/badge.svg?branch=master&service=github&t=2lhJpx)](https://coveralls.io/github/amperser/proselint?branch=master)
![Lint score](http://img.shields.io/badge/lintscore_v0.1.0-98.8-blue.svg)
[![Dependency Status](https://gemnasium.com/7cf4ad9bbb5fd951b6ffb79e9552609c.svg)](https://gemnasium.com/amperser/proselint)

`proselint` places the world's greatest writers and editors by your side, where they whisper suggestions on how to improve your prose. You'll be guided by Bryan Garner, David Foster Wallace, Mark Twain, Chuck Palahniuk, Steve Pinker, Mary Norris, Elmore Leonard, Matthew Butterick, William Strunk, E.B. White, Philip Corbett, and the editorial staff of the world's finest literary magazines and newspapers. Others are on their way and will arrive shortly. Our goal is to aggregate knowledge about best practices in writing and to make that knowledge immediately accessible to all authors in the form of a linter for prose. We call it `proselint`.

`proselint` is a command-line utility and web API that can be integrated into existing tools.
 
### Installation

To get this up and running as a command line utility, run `python setup.py develop` from inside the root directory.

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
| `carlin.filth` | Words to avoid |
| `consistency.spacing` | Consistent sentence spacing |
| `consistency.spelling` | Consistent use of British vs. American spelling |
| `garner.a_vs_an` | Using 'a' vs. 'an' as a determiner  |
| `garner.airlinese` | Avoiding jargon of the airline industry |
| `garner.am_pm` | Using the right form for the time of day |
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
| `garner.malapropisms` | Avoiding common malapropisms |
| `garner.many_a` | Many a singular |
| `garner.misspelling` | Avoiding common misspellings missed by spell-check |
| `garner.mixed_metaphors` | Not mixing metaphors |
| `garner.needless_variants` | Using the preferred form |
| `garner.oxymorons` | Avoiding oxymorons |
| `garner.preferred_forms` | Miscellaneous preferred forms |
| `garner.punctuation` | Using the right punctuation |
| `garner.redundancy` | Avoiding redundancy |
| `garner.sexism` | Avoiding sexist language |
| `gowers.overworked_metaphors` | Overworked metaphors |
| `inc.corporate_speak` | Avoiding corporate buzzwords |
| `leonard.exclamation` | Avoiding hyperbolic use of exclamation |
| `leonard.hell` | Avoiding a common cliché |
| `lilienfeld.terms_to_avoid` | Avoiding misused psychological terms |
| `misc.annotations` | Catching annotations left in the text |
| `misc.chatspeak` | Avoiding lolling and other chatspeak |
| `misc.credit_card` | Keeping credit card numbers secret |
| `misc.currency` | Avoiding redundant currency symbols |
| `misc.hyperbolic` | Not being hyperbolic |
| `misc.link_checker` | Linking only to existing sites |
| `misc.password` | Keeping passwords secret |
| `misc.whence` | Usage of the word "whence" |
| `nfl.naughty_words` | Avoiding words banned by the NFL |
| `nordquist.redundancy` | Avoiding redundancy and saying things twice |
| `norris.denizen_labels` | Using the right denizen label |
| `ogilvy.pretension` | Avoiding being pretentious |
| `orwell.debased` | Avoiding debased language |
| `palahniuk.suddenly` | Avoiding the word suddenly |
| `pinker.apologizing` | Being confident |
| `pinker.hedging` | Not hedging |
| `pinker.latin` | Avoiding overuse of Latin phrases |
| `pinker.metaconcepts` | Avoiding overuse of metaconcepts |
| `pinker.narcisissm` | Talking about the subject, not its study |
| `pinker.scare_quotes` | Using scare quotes only when needed |
| `strunk_white.composition` | Avoiding wordy phrases |
| `strunk_white.greylist` | Words to avoid |
| `strunk_white.usage` | Misc. usage recommendations |
| `twain.damn` | Avoiding the word "very" |
| `wallace.tense_present` | Misc. advice |
| `wallace.uncomparables` | Not comparing uncomparables |
| `write_good.cliches` | Avoiding cliches |
| `write_good.lexical_illusions` | Avoiding lexical illusions |
| `write_good.weasel_words` | Avoiding weasel words |
| `wsj.athletes` | Spelling the names of athletes correctly |

### Contributing

We'd love to accept your patches and contributions to improve `proselint`. Learn more about how to contribute in [CONTRIBUTING.md](./CONTRIBUTING.md).
