<img src="logo.png" alt="proselint logo" width="200">

[![Build Status](https://travis-ci.org/amperser/proselint.svg)](https://travis-ci.org/amperser/proselint)
[![Code Climate](https://codeclimate.com/repos/5538989ee30ba0793100090f/badges/e10a2fe18a9256d69e2a/gpa.svg)](https://codeclimate.com/repos/5538989ee30ba0793100090f/feed)
[![Coverage Status](https://coveralls.io/repos/amperser/proselint/badge.svg?branch=master&service=github&t=2lhJpx)](https://coveralls.io/github/amperser/proselint?branch=master)
![Lint score](http://img.shields.io/badge/lintscore_v0.1.0-98.8-blue.svg)
[![Dependency Status](https://gemnasium.com/amperser/proselint.svg)](https://gemnasium.com/amperser/proselint)

Writing is notoriously hard, even for the best writers. Yet there is a tremendous amount of knowledge about the discipline strewn across usage guides, dictionaries, technical manuals, essays, pamphlets, websites, and the hearts and minds of great authors and editors. But poring over Strunk & White hardly makes one a better writer — it turns you into neither Strunk nor White. And nobody has the capacity to apply all the advice from *Garner’s Modern American Usage*, a 975-page usage guide, to everything they write. In fact, the whole notion that one becomes a better writer by reading advice on writing rests on untenable assumptions about learning and memory. The traditional formats of knowledge about writing are thus essentially inert, waiting to be transformed.

We devised a simple solution: `proselint`, a linter for prose. (A linter is a computer program that, like a spell checker, scans through a document and analyzes it.)

`proselint` places the world’s greatest writers and editors by your side, where they whisper suggestions on how to improve your prose. You’ll be guided by advice inspired by Bryan Garner, David Foster Wallace, Chuck Palahniuk, Steve Pinker, Mary Norris, Mark Twain, Elmore Leonard, George Orwell, Matthew Butterick, William Strunk, E.B. White, Philip Corbett, Ernest Gowers, and the editorial staff of the world’s finest literary magazines and newspapers, among others. Our goal is to aggregate knowledge about best practices in writing and to make that knowledge immediately accessible to all authors in the form of a linter for prose.

`proselint` is a command-line utility that can be integrated into existing tools.
 
### Installation

To get this up and running, install it using pip: `pip install proselint`.

### Usage

You can run `proselint` on a document:

```bash
❯ proselint text.md
```

This prints a list of suggestions to stdout, one per line. Each suggestion will have the form:

```bash
text.md:<line>:<column>: <check_name> <message>
```

For example,

```bash
text.md:0:10: wallace.uncomparables Comparison of an uncomparable: 'unique' can not be compared.
```

The command-line utility can also print the list of suggestions in JSON using the `--json` flag. In this case, the output is considerably richer:

```javascript
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

### Available plugins for text editors

`proselint` is available on:

- [x] A live [demo page](http://proselint.com/write)
- [x] [Sublime Text](https://github.com/amperser/proselint/tree/master/plugins/sublime/SublimeLinter-contrib-proselint)
- [x] [Atom Editor](https://github.com/smockle/linter-proselint) (thanks to [Clay Miller](https://github.com/smockle)).
- [x] [Emacs via Flycheck](https://github.com/amperser/proselint/tree/master/plugins/flycheck) (thanks to [Aaron Jacobs](https://github.com/atheriel))
- [x] [Vim](https://github.com/amperser/proselint/tree/master/plugins/vim) (thanks to [Matthias Bussonnier](https://github.com/Carreau))

### Checks

You can disable any of the checks by modifying `.proselintrc`.

| ID    | Description     |
| ----- | --------------- |
| `butterick.symbols` | Using the right symbol |
| `carlin.filth` | Words to avoid |
| `consistency.spacing` | Consistent sentence spacing |
| `consistency.spelling` | Consistent use of British vs. American spelling |
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
| `garner.diacritical_marks` | Using dïacríticâl marks |
| `garner.illogic` | Avoiding illogical forms |
| `garner.jargon` | Avoiding miscellaneous jargon |
| `garner.malapropisms` | Avoiding common malapropisms |
| `garner.many_a` | Many a singular |
| `garner.misspelling` | Avoiding common misspellings missed by spell-check |
| `garner.mixed_metaphors` | Not mixing metaphors |
| `garner.mondegreens` | Avoiding mondegreens |
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
| `oxford.venery_terms` | Call groups of animals by the right name |
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

Interested in contributing to `proselint`? Great — there are plenty of ways you can help. Read more on [our website](http://proselint.com/contributing/), where we describe how you can help us build `proselint` into the greatest writing tool in the world.
