# Contributing

Interested in contributing to `proselint`? Great — there are plenty of ways you
can help. In the following sections, we describe how you can help us build
`proselint` into the greatest writing tool in the world.

## Skills

### Coding

Have coding skills? You can:

- Implement a new piece of advice in the linter. In our issue tracker on GitHub,
  we maintain an ever-growing [list of rules] that have been extracted from
  expert advice on writing. Some of these are one-liners that will take only a
  moment to complete; others are full-blown research projects. Use existing
  checks as a guide for creating your own. Then open a pull request.
- Fix [bugs].
- Improve [performance].
- Write tests. Our test coverage is too low. Keeping out false alarms is key to
  the tool's success and anything we can do to uncover false alarms and prevent
  regressions is thus key to the tool's success.

[list of rules]: https://github.com/amperser/proselint/labels/cat:%20new-check
[bugs]: https://github.com/amperser/proselint/labels/type:%20fix
[performance]: https://github.com/amperser/proselint/labels/type:%20perf

### Writing and editing

Have writing or editing skills? You can:

- Extract rules from expert sources of advice. Read through some entries of a
  book like *Garner's Modern American usage*, find rules that are feasible to
  implement, and then [open a Check Request issue]. Here's an [example] of a
  successfully extracted rule.
- Find false positives. Run `proselint` over your favourite books or magazine
  articles — maybe even your own writing — and find places where `proselint`
  says there's an error, but in reality, there is none. [Open a False Positive
  issue] and describe the problem.
- Improve the copy or documentation surrounding the project and within its code.

[open a Check Request issue]: https://github.com/amperser/proselint/issues/new?template=check-request.md
[example]: https://github.com/amperser/proselint/issues/163
[Open a False Positive issue]: https://github.com/amperser/proselint/issues/new?template=false-positive.md

## Process

### Prerequisites

Before you spend valuable time contributing to Proselint, please first discuss
the change you wish to make with us. The best way to do this is by filing an
issue with your proposal, since you'll need an issue number to refer to in your
pull request. Alternatively, you can skip this if an issue relating to your
changes already exists.

Next, ensure your environment is prepared. If you're using [Nix], this is as
simple as running `nix develop`. For other systems, you'll need to install
[`uv`], and then run `uv sync --locked --dev --all-extras --group test` for the
full suite of development and testing tools.

[Nix]: https://nixos.org
[`uv`]: https://docs.astral.sh/uv

### Workflow

1. Fork and clone this repository.
2. Create a new branch in your fork based off the **main** branch.
3. Make your changes.
4. Commit your changes, and push them.
5. Submit a pull request.

### Linting and Testing

We use [Poe] as a job runner. This makes the process of linting and testing your
changes in the same way they'll be verified in CI trivial. Please do ensure
these pass before you submit a pull request to keep your changes consistent with
our codebase.

- **Linting**: `uv run poe lint`
- **Formatting**: `uv run poe format`
- **Testing**: `uv run poe test`

[Poe]: https://poethepoet.natn.io
