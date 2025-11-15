<img src="https://raw.githubusercontent.com/amperser/proselint/main/logo.png" alt="proselint logo" width="200">

![Workflow status](https://github.com/amperser/proselint/actions/workflows/ci-lint-test.yml/badge.svg)
[![codecov](https://codecov.io/gh/amperser/proselint/branch/main/graph/badge.svg?token=8E0I9sRpot)](https://codecov.io/gh/amperser/proselint)
[![License](https://img.shields.io/badge/License-BSD-blue.svg)](https://en.wikipedia.org/wiki/BSD_licenses)

Writing is notoriously hard, even for the best writers, and it's not for lack of
good advice — a tremendous amount of knowledge about the craft is strewn across
usage guides, dictionaries, technical manuals, essays, pamphlets, websites, and
the hearts and minds of great authors and editors. But poring over Strunk &
White hardly makes one a better writer — it turns you into neither Strunk nor
White. And nobody has the capacity to apply all the advice from *Garner’s Modern
English Usage*, an 1100-page usage guide, to everything they write. In fact, the
whole notion that one becomes a better writer by reading advice on writing rests
on untenable assumptions about learning and memory. The traditional formats of
knowledge about writing are thus essentially inert, waiting to be transformed.

We devised a simple solution: `proselint`, a linter for English prose. A linter
is a computer program that, akin to a spell checker, scans through a file and
detects issues — like how a real lint roller helps you get unwanted lint off of
your shirt.

`proselint` places the world's greatest writers and editors by your side, where
they whisper suggestions on how to improve your prose. You’ll be guided by
advice inspired by Bryan Garner, David Foster Wallace, Chuck Palahniuk, Steve
Pinker, Mary Norris, Mark Twain, Elmore Leonard, George Orwell, Matthew
Butterick, William Strunk, Elwyn White, Philip Corbett, Ernest Gowers, and the
editorial staff of the world’s finest literary magazines and newspapers, among
others. Our goal is to aggregate knowledge about best practices in writing and
to make that knowledge immediately accessible to all authors in the form of a
linter for prose; all in a neat command-line utility that you can integrate into
other tools, scripts, and workflows.

## Installation

To get this up and running, install it using [pip].

```bash
pip install proselint
```

[pip]: https://packaging.python.org/installing/#use-pip-for-installing

### Fedora

```bash
sudo dnf install proselint
```

### Debian

```bash
sudo apt install python3-proselint
```

### Ubuntu

```bash
sudo add-apt-repository universe
sudo apt install python3-proselint
```

### Nix

`proselint` is packaged by [`nixpkgs`].

#### Declarative

```nix
environment.systemPackages = [pkgs.proselint];
```

#### Imperative

```bash
nix profile install nixpkgs#proselint
```

[`nixpkgs`]: https://search.nixos.org/packages?channel=25.05&show=proselint

### Plugins for other software

`proselint` is available on:

- A [demo editor](http://proselint.com/write)
- [Sublime Text](https://github.com/amperser/proselint/tree/main/plugins/sublime/SublimeLinter-contrib-proselint)
- [Atom Editor](https://github.com/smockle/linter-proselint) (thanks to [Clay Miller](https://github.com/smockle)).
- Emacs via [Flycheck](http://www.flycheck.org/) or via [Flymake](https://sr.ht/~manuel-uberti/flymake-proselint/)
- Vim via [ALE](https://github.com/w0rp/ale) or [Syntastic](https://github.com/vim-syntastic/syntastic) (thanks to @lcd047, @Carreau, and [Daniel M. Capella](https://github.com/polyzen))
- Neovim via [null-ls](https://github.com/jose-elias-alvarez/null-ls.nvim) (null-ls has [diagnostics](https://github.com/jose-elias-alvarez/null-ls.nvim/blob/main/lua/null-ls/builtins/diagnostics/proselint.lua) and [code actions](https://github.com/jose-elias-alvarez/null-ls.nvim/blob/main/lua/null-ls/builtins/code_actions/proselint.lua) for proselint)
- [Phabricator's `arc` CLI](https://github.com/google/arc-proselint) (thanks to [Jeff Verkoeyen](https://github.com/jverkoey))
- [Danger](https://github.com/dbgrandi/danger-prose) (thanks to [David Grandinetti](https://github.com/dbgrandi) and [Orta Therox](https://github.com/orta))
- [Visual Studio Code](https://github.com/ppeszko/vscode-proselint) (thanks to [Patryk Peszko](https://github.com/ppeszko))
- [coala](https://github.com/coala-analyzer/bear-docs/blob/master/docs/ProseLintBear.rst) (thanks to the [coala Development Group](https://github.com/coala-analyzer))
- [IntelliJ](https://github.com/kropp/intellij-proselint) (by [Victor Kropp](https://github.com/kropp))
- [pre-commit](https://pre-commit.com/) (by [Andy Airey](https://github.com/aairey))
- [Statick](https://github.com/sscpac/statick-md)
- [MegaLinter](https://oxsecurity.github.io/megalinter/latest/descriptors/spell_proselint/)

### Usage

Suppose you have a document `text.md` with the following text:

```md
John is very unique.
```

You can run `proselint` over the document using the command line:

```bash
proselint check text.md
```

This prints a list of suggestions to stdout, one per line. Each suggestion is of
the form:

```bash
file:<line>:<column>: <check_name>: <message>
```

For example,

```bash
text.md:1:9: uncomparables: Comparison of an uncomparable: 'very unique' is not comparable.
```

The command-line utility can also print suggestions in JSON using the
`--output-format json` option. In this case, the output is considerably richer,
following our [stable wire schema].

```jsonc
{
  "result": {
    "file:///path/to/text.md": {
      "diagnostics": [
        {
          // Name of the check that output this suggestion.
          "check_path": "uncomparables",
          // Message to describe the suggestion
          "message": "Comparison of an uncomparable: 'very unique' is not comparable.",
          // Line and column where the error begins in the source
          "pos": [1, 9],
          // Absolute start and end of the error in the source
          "span": [9, 20],
          // Suggested replacements for the content, if applicable
          "replacements": null,
        }
      ]
    }
  }
}
```

To run the linter as part of another Python program, you can use the `LintFile`
class in `proselint.tools`. This requires `CheckRegistry` to be populated.

```python
from proselint.checks import __register__
from proselint.registry import CheckRegistry
from proselint.tools import LintFile

CheckRegistry().register_many(__register__)
suggestions = LintFile("source-name", "This sentence is very unique").lint()
```

This will return a list of suggestions:

```python
[LintResult(
    check_result=CheckResult(
        check_path='uncomparables',
        message="Comparison of an uncomparable: 'very unique' is not comparable.",
        span=(18, 29),
        replacements=None,
    ),
    pos=(1, 18),
)]
```

[stable wire schema]: https://github.com/amperser/proselint/blob/main/docs/wire-schema.md

### Checks

You can disable any of the checks by modifying
`$XDG_CONFIG_HOME/proselint/config.json`. If `$XDG_CONFIG_HOME` is not set or
empty, `~/.config/proselint/config.json` will be used. Additionally, for
compatibility reasons, the legacy configurations `~/.proselintrc` and
`$XDG_CONFIG_HOME/proselint/config` will be checked if
`$XDG_CONFIG_HOME/proselint/config.json` does not exist. Check selection is
granular at any level, illustrated in the following example:

```json
{
  "checks": {
    "typography": true,
    "typography.symbols": false,
    "typography.symbols.curly_quotes": true,
    "typography.punctuation.hyperbole": false,
  }
}
```

This configuration would enable all checks in the `typography` module, excluding
`typography.punctuation.hyperbole` and those in `typography.symbols`, but
preserving `typography.symbols.curly_quotes`. Using this system allows you to
concisely and precisely select checks at an individual level.

| ID    | Description     |
| ----- | --------------- |
| `annotations` | Catch annotations left in the text |
| `archaism` | Avoid archaic forms |
| `cliches.hell` | Avoid a common cliché regarding hell |
| `cliches.misc` | Avoid clichés |
| `dates_times.am_pm` | Format the time of day correctly |
| `dates_times.dates` | Format dates appropriately |
| `hedging` | Avoid undermining yourself with uncertainty |
| `industrial_language.airlinese` | Avoid jargon of the airline industry |
| `industrial_language.bureaucratese` | Avoid bureaucratese |
| `industrial_language.chatspeak` | Avoid lolling and other chatspeak |
| `industrial_language.commercialese` | Avoid jargon of the commercial world |
| `industrial_language.corporate_speak` | Avoid corporate buzzwords |
| `industrial_language.jargon` | Avoid miscellaneous jargon |
| `lexical_illusions` | Avoid repeating words or phrases |
| `malapropisms` | Avoid common malapropisms |
| `misc.apologizing` | Be confident and avoid excessive apologizing |
| `misc.back_formations` | Avoid redundant backformations |
| `misc.but` | Do not start a paragraph with "But..." |
| `misc.capitalization` | Capitalize only what ought to be capitalized |
| `misc.composition` | Adhere to principles of composition |
| `misc.currency` | Avoid redundant currency symbols |
| `misc.debased` | Avoid debased language |
| `misc.false_plurals` | Avoid false plurals |
| `misc.greylist` | Avoid greylisted terms |
| `misc.illogic` | Avoid illogical forms |
| `misc.inferior_superior` | Superior to, not than |
| `misc.institution_name` | Use the correct names of institutions |
| `misc.latin` | Avoid overuse of Latin phrases |
| `misc.many_a` | Use singular forms with "many a" |
| `misc.metadiscourse` | Avoid discussing the discussion |
| `misc.narcissism` | Talk about the subject, not its study |
| `misc.not_guilty` | Avoid "not guilty beyond a reasonable doubt" |
| `misc.phrasal_adjectives` | Hyphenate phrasal adjectives correctly |
| `misc.preferred_forms` | Use the preferred forms of terms |
| `misc.pretension` | Do not be pretentious |
| `misc.professions` | Use the right names for jobs |
| `misc.scare_quotes` | Do not misuse scare quotes |
| `misc.suddenly` | Retain suddenness by not using "suddenly" |
| `misc.tense_present` | Follow advice from Tense Present |
| `misc.waxed` | Use adjectives for waxed, as in "wax poetic" |
| `misc.whence` | Avoid redundancy with "whence" |
| `mixed_metaphors` | Do not mix metaphors |
| `mondegreens` | Avoid mondegreens |
| `needless_variants` | Use preferred forms over uncommon variants |
| `nonwords` | Do not use nonwords |
| `oxymorons` | Avoid oxymorons |
| `psychology` | Avoid misusing psychological terms |
| `redundancy.misc` | Avoid redundancy in phrases |
| `redundancy.ras_syndrome` | Avoid redundancy in acronyms |
| `restricted.elementary` | Restrict writing to terms from elementary school |
| `restricted.top1000` | Restrict writing to the top 1000 words by usage |
| `skunked_terms` | Avoid using skunked terms |
| `social_awareness.lgbtq` | Be aware of LGBTQ+ terminology |
| `social_awareness.nword` | Take responsibility for use of "the n-word" |
| `social_awareness.sexism` | Be aware of sexist language |
| `spelling.able_atable` | Use the correct form of -able and -atable |
| `spelling.able_ible` | Use the correct form of -able and -ible |
| `spelling.ally_ly` | Use the correct form of -ally and -ly |
| `spelling.ance_ence` | Use the correect form of -ance and -ence |
| `spelling.athletes` | Spell the names of athletes correctly |
| `spelling.consistency` | Be consistent in spelling |
| `spelling.ely_ly` | Use the correct form of -ely and -ly |
| `spelling.em_im_en_in` | Use the correct form of -em, -im, -en, and -in |
| `spelling.er_or` | Use the correct form of -er and -or |
| `spelling.in_un` | Use the correct form of -in and -un |
| `spelling.misc` | Spell miscellaneous terms correctly |
| `spelling.ve_of` | Use the correct form of -ve and -of |
| `terms.animal_adjectives` | Use the right adjectives for likening animals |
| `terms.denizen_labels` | Use the right names for denizens |
| `terms.eponymous_adjectives` | Use the right names for likening people |
| `terms.venery` | Use the right names for groups of animals |
| `typography.diacritical_marks` | Use diacritical marks |
| `typography.punctuation` | Use punctuation correctly |
| `typography.symbols` | Use symbols correctly |
| `uncomparables` | Do not compare uncomparables |
| `weasel_words` | Avoid weasel words |

### Contributing

Interested in contributing to `proselint`? Great — there are plenty of ways you
can help. Check out our [contributing guidelines], where we describe how you
can help us build `proselint` into the greatest writing tool in the world.

- [Issue Tracker](http://github.com/amperser/proselint/issues)
- [Source Code](http://github.com/amperser/proselint)

[contributing guidelines]: https://github.com/amperser/proselint/blob/main/CONTRIBUTING.md

### Support

If you run into a problem, please [open an issue](http://github.com/amperser/proselint/issues).

### Running Tests

Automated tests are included in the `tests` directory. To run these
tests locally, you can use `pytest` via `poe test`.

### License

The project is licensed under the [BSD license](LICENSE.md).
