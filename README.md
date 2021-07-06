<img src="https://raw.githubusercontent.com/amperser/proselint/main/logo.png" alt="proselint logo" width="200">

![Workflow status](https://github.com/amperser/proselint/actions/workflows/ci-lint-test.yml/badge.svg)
[![Reviewed by Hound](https://img.shields.io/badge/Reviewed_by-Hound-8E64B0.svg)](https://houndci.com)
[![Code Climate](https://codeclimate.com/repos/5538989ee30ba0793100090f/badges/e10a2fe18a9256d69e2a/gpa.svg)](https://codeclimate.com/repos/5538989ee30ba0793100090f/feed)
[![codecov](https://codecov.io/gh/amperser/proselint/branch/main/graph/badge.svg?token=8E0I9sRpot)](https://codecov.io/gh/amperser/proselint)
[![License](https://img.shields.io/badge/License-BSD-blue.svg)](https://en.wikipedia.org/wiki/BSD_licenses)

Writing is notoriously hard, even for the best writers, and it's not for lack of good advice — a tremendous amount of knowledge about the craft is strewn across usage guides, dictionaries, technical manuals, essays, pamphlets, websites, and the hearts and minds of great authors and editors. But poring over Strunk & White hardly makes one a better writer — it turns you into neither Strunk nor White. And nobody has the capacity to apply all the advice from *Garner’s Modern English Usage*, an 1100-page usage guide, to everything they write. In fact, the whole notion that one becomes a better writer by reading advice on writing rests on untenable assumptions about learning and memory. The traditional formats of knowledge about writing are thus essentially inert, waiting to be transformed.

We devised a simple solution: `proselint`, a linter for English prose. A linter is a computer program that, akin to a spell checker, scans through a file and detects issues — like how a real lint roller helps you get unwanted lint off of your shirt.

`proselint` places the world's greatest writers and editors by your side, where they whisper suggestions on how to improve your prose. You’ll be guided by advice inspired by Bryan Garner, David Foster Wallace, Chuck Palahniuk, Steve Pinker, Mary Norris, Mark Twain, Elmore Leonard, George Orwell, Matthew Butterick, William Strunk, Elwyn White, Philip Corbett, Ernest Gowers, and the editorial staff of the world’s finest literary magazines and newspapers, among others. Our goal is to aggregate knowledge about best practices in writing and to make that knowledge immediately accessible to all authors in the form of a linter for prose; all in a neat command-line utility that you can integrate into other tools, scripts, and workflows.

### Installation

To get this up and running, install it using [pip]:

```bash
pip install proselint
```

[pip]: https://packaging.python.org/installing/#use-pip-for-installing

#### Fedora

```bash
sudo dnf install proselint
```

#### Debian

```bash
sudo apt install python3-proselint
```

#### Ubuntu

```bash
sudo add-apt-repository universe
sudo apt install python3-proselint
```

### Plugins for other software

`proselint` is available on:

- A [demo editor](http://proselint.com/write)
- [Sublime Text](https://github.com/amperser/proselint/tree/master/plugins/sublime/SublimeLinter-contrib-proselint)
- [Atom Editor](https://github.com/smockle/linter-proselint) (thanks to [Clay Miller](https://github.com/smockle)).
- [Emacs via Flycheck](http://www.flycheck.org/).
- Vim via [ALE](https://github.com/w0rp/ale) or [Syntastic](https://github.com/vim-syntastic/syntastic) (thanks to @lcd047, @Carreau, and [Daniel M. Capella](https://github.com/polyzen))
- [Phabricator's `arc` CLI](https://github.com/google/arc-proselint) (thanks to [Jeff Verkoeyen](https://github.com/jverkoey))
- [Danger](https://github.com/dbgrandi/danger-prose) (thanks to [David Grandinetti](https://github.com/dbgrandi) and [Orta Therox](https://github.com/orta))
- [Visual Studio Code](https://github.com/ppeszko/vscode-proselint) (thanks to [Patryk Peszko](https://github.com/ppeszko))
- [coala](https://github.com/coala-analyzer/bear-docs/blob/master/docs/ProseLintBear.rst) (thanks to the [coala Development Group](https://github.com/coala-analyzer))
- [IntelliJ](https://github.com/kropp/intellij-proselint) (by [Victor Kropp](https://github.com/kropp))
- [pre-commit](https://pre-commit.com/) (by [Andy Airey](https://github.com/aairey))

### Usage

Suppose you have a document `text.md` with the following text:

```
John is very unique.
```

You can run `proselint` over the document using the command line:

```bash
proselint text.md
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

```jsonc
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

  // length from start -> end
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

To run the linter as part of another Python program, you can use the `lint` function in `proselint.tools`:

```python
import proselint

suggestions = proselint.tools.lint("This sentence is very unique")
```

This will return a list of suggestions:

```python
[('weasel_words.very', "Substitute 'damn' every time you're inclined to write 'very;' your editor will delete it and the writing will be just as it should be.", 0, 17, 17, 22, 5, 'warning', None), ('uncomparables.misc', "Comparison of an uncomparable: 'very unique.' is not comparable.", 0, 17, 17, 29, 12, 'warning', None)]
```

### Checks

You can disable any of the checks by modifying `$XDG_CONFIG_HOME/proselint/config`. If `$XDG_CONFIG_HOME` is not set or empty, `~/.config/proselint/config` will be used. Additionally, for compatibility reasons, the legacy configuration `~/.proselintrc` will be checked if `$XDG_CONFIG_HOME/proselint/config` does not exist.

```json
{
  "checks": {
    "typography.diacritical_marks": false
  }
}
```

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
| `lgbtq.offensive_terms` | Avoding offensive LGBTQ terms |
| `lgbtq.terms` | Misused LGBTQ terms |
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
| `misc.narcissism` | Talking about the subject, not its study |
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

Interested in contributing to `proselint`? Great — there are plenty of ways you can help. Read more on [our website], where we describe how you can help us build `proselint` into the greatest writing tool in the world.

- [Issue Tracker](http://github.com/amperser/proselint/issues)
- [Source Code](http://github.com/amperser/proselint)

[our website]: http://proselint.com/contributing/

### Support

If you run into a problem, please [open an issue](http://github.com/amperser/proselint/issues) in or send an email to hello@amperser.com.

### Running Automated Tests

Automated tests are included in the `proselint/tests` directory. To run these tests locally, you can use `./run_ci_checks.sh`.

### License

The project is licensed under the BSD license.
