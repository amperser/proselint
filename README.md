<img src="logo.png" alt="proselint logo" width="200">

[![Build Status](https://travis-ci.org/amperser/proselint.svg)](https://travis-ci.org/amperser/proselint)
[![Build status](https://ci.appveyor.com/api/projects/status/hfgv05nkjxkg2gcc/branch/master?svg=true)](https://ci.appveyor.com/project/suchow/proselint-knwyf/branch/master)
[![Code Climate](https://codeclimate.com/repos/5538989ee30ba0793100090f/badges/e10a2fe18a9256d69e2a/gpa.svg)](https://codeclimate.com/repos/5538989ee30ba0793100090f/feed)
[![Coverage Status](https://coveralls.io/repos/github/amperser/proselint/badge.svg?branch=master)](https://coveralls.io/github/amperser/proselint?branch=master)
[![Dependency Status](https://gemnasium.com/amperser/proselint.svg)](https://gemnasium.com/amperser/proselint)
[![License](https://img.shields.io/badge/License-BSD-blue.svg)](https://en.wikipedia.org/wiki/BSD_licenses)

Writing is notoriously hard, even for the best writers, and it's not for lack of good advice — a tremendous amount of knowledge about the craft is strewn across usage guides, dictionaries, technical manuals, essays, pamphlets, websites, and the hearts and minds of great authors and editors. But poring over Strunk & White hardly makes one a better writer — it turns you into neither Strunk nor White. And nobody has the capacity to apply all the advice from *Garner’s Modern American Usage*, a 975-page usage guide, to everything they write. In fact, the whole notion that one becomes a better writer by reading advice on writing rests on untenable assumptions about learning and memory. The traditional formats of knowledge about writing are thus essentially inert, waiting to be transformed.

We devised a simple solution: `proselint`, a linter for prose. (A linter is a computer program that, like a spell checker, scans through a document and analyzes it.)

`proselint` places the world’s greatest writers and editors by your side, where they whisper suggestions on how to improve your prose. You’ll be guided by advice inspired by Bryan Garner, David Foster Wallace, Chuck Palahniuk, Steve Pinker, Mary Norris, Mark Twain, Elmore Leonard, George Orwell, Matthew Butterick, William Strunk, E.B. White, Philip Corbett, Ernest Gowers, and the editorial staff of the world’s finest literary magazines and newspapers, among others. Our goal is to aggregate knowledge about best practices in writing and to make that knowledge immediately accessible to all authors in the form of a linter for prose.

`proselint` is a command-line utility that can be integrated into existing tools.
 
### Installation

To get this up and running, install it using pip: `pip install proselint`.

### Plugins for other software

`proselint` is available on:

- [x] A [demo editor](http://proselint.com/write)
- [x] [Sublime Text](https://github.com/amperser/proselint/tree/master/plugins/sublime/SublimeLinter-contrib-proselint)
- [x] [Atom Editor](https://github.com/smockle/linter-proselint) (thanks to [Clay Miller](https://github.com/smockle)).
- [x] [Emacs via Flycheck](https://github.com/amperser/proselint/tree/master/plugins/flycheck) (thanks to [Aaron Jacobs](https://github.com/atheriel))
- [x] [Vim](https://github.com/amperser/proselint/tree/master/plugins/vim) (thanks to [Matthias Bussonnier](https://github.com/Carreau))
- [x] [Phabricator's `arc` CLI](https://github.com/google/arc-proselint) (thanks to [Jeff Verkoeyen](https://github.com/jverkoey))

### Usage

Suppose you had a document `text.md` with the following text:

```
John is very unique.
```

You can run `proselint` over the document using the command line:

```bash
❯ proselint text.md
```

This prints a list of suggestions to stdout, one per line. Each suggestion has the form:

```bash
text.md:<line>:<column>: <check_name> <message>
```

For example,

```bash
text.md:0:10: wallace.uncomparables Comparison of an uncomparable: 'unique' cannot be compared.
```

The command-line utility can also print suggestions in JSON using the `--json` flag. In this case, the output is considerably richer:

```javascript
{
    // Type of check that output this suggestion.
    check: "wallace.uncomparables",

    // Message to describe the suggestion.
    message: "Comparison of an uncomparable: 'unique' cannot be compared.",

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
| `airlinese.misc` | Avoiding jargon of the airline industry |
| `annotations.misc` | Catching annotations left in the text |
| `archaism.misc` | Avoiding archaic forms |
| `cliches.hell` | Avoiding a common cliché |
| `cliches.misc` | Avoiding clichés |
| `consistency.spacing` | Consistent sentence spacing |
| `consistency.spelling` | Consistent spelling |
| `corporate_speak.misc` | Avoiding corporate buzzwords |
| `cursing.filth` | Words to avoid |
| `cursing.nfl` | Avoiding words banned by the NFL |
| `dates_times.am_pm` | Using the right form for the time of day |
| `dates_times.dates` | Stylish formatting of dates |
| `hedging.misc` | Not hedging |
| `hyperbole.misc` | Not being hyperbolic |
| `jargon.misc` | Avoiding miscellaneous jargon |
| `lexical_illusions.misc` | Avoiding lexical illusions |
| `links.broken` | Linking only to existing sites |
| `malapropisms.misc` | Avoiding common malapropisms |
| `misc.apologizing` | Being confident |
| `misc.back_formations` | Avoiding needless backformations |
| `misc.bureaucratese` | Avoiding bureaucratese |
| `misc.but` | Avoid starting a paragraph with "But..." |
| `misc.capitalization` | Capitalizing only what ought to be capitalized |
| `misc.chatspeak` | Avoiding lolling and other chatspeak |
| `misc.commercialese` | Avoiding jargon of the commercial world |
| `misc.currency` | Avoiding redundant currency symbols |
| `misc.debased` | Avoiding debased language |
| `misc.false_plurals` | Avoiding false plurals |
| `misc.illogic` | Avoiding illogical forms |
| `misc.inferior_superior` | Superior to, not than |
| `misc.latin` | Avoiding overuse of Latin phrases |
| `misc.many_a` | Many a singular |
| `misc.metaconcepts` | Avoiding overuse of metaconcepts |
| `misc.narcisissm` | Talking about the subject, not its study |
| `misc.phrasal_adjectives` | Hyphenating phrasal adjectives |
| `misc.preferred_forms` | Miscellaneous preferred forms |
| `misc.pretension` | Avoiding being pretentious |
| `misc.professions` | Calling jobs by the right name |
| `misc.punctuation` | Using punctuation assiduously |
| `misc.scare_quotes` | Using scare quotes only when needed |
| `misc.suddenly` | Avoiding the word suddenly |
| `misc.tense_present` | Advice from Tense Present |
| `misc.waxed` | Waxing poetic |
| `misc.whence` | Using "whence" |
| `mixed_metaphors.misc` | Not mixing metaphors |
| `mondegreens.misc` | Avoiding mondegreen |
| `needless_variants.misc` | Using the preferred form |
| `nonwords.misc` | Avoid using nonwords |
| `oxymorons.misc` | Avoiding oxymorons |
| `psychology.misc` | Avoiding misused psychological terms |
| `redundancy.misc` | Avoiding redundancy and saying things twice |
| `redundancy.ras_syndrome` | Avoiding RAS syndrome |
| `skunked_terms.misc` | Avoid using skunked terms |
| `spelling.able_atable` | -able vs. -atable |
| `spelling.able_ible` | -able vs. -ible |
| `spelling.athletes` | Spelling of athlete names |
| `spelling.em_im_en_in` | -em vs. -im and -en vs. -in |
| `spelling.er_or` | -er vs. -or |
| `spelling.in_un` | in- vs. un- |
| `spelling.misc` | Spelling words corectly |
| `security.credit_card` | Keeping credit card numbers secret |
| `security.password` | Keeping passwords secret |
| `sexism.misc` | Avoiding sexist language |
| `terms.animal_adjectives` | Animal adjectives |
| `terms.denizen_labels` | Calling denizens by the right name |
| `terms.eponymous_adjectives` | Calling people by the right name |
| `terms.venery` | Call groups of animals by the right name |
| `typography.diacritical_marks` | Using dïacríticâl marks |
| `typography.exclamation` | Avoiding overuse of exclamation |
| `typography.symbols` | Using the right symbols |
| `uncomparables.misc` | Not comparing uncomparables |
| `weasel_words.misc` | Avoiding weasel words |
| `weasel_words.very` | Avoiding the word "very" |

### Contributing

Interested in contributing to `proselint`? Great — there are plenty of ways you can help. Read more on [our website](http://proselint.com/contributing/), where we describe how you can help us build `proselint` into the greatest writing tool in the world.

- [Issue Tracker](http://github.com/amperser/proselint/issues)
- [Source Code](http://github.com/amperser/proselint)

### Support 

If you run into a problem, please [open an issue](http://github.com/amperser/proselint/issues) in or send an email to hello@amperser.com.

### License

The project is licensed under the BSD license.
