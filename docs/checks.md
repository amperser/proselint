# Guidelines for Checks

## Terminology

In the interest of keeping documentation and discussions of Proselint clear and
consistent, we use a standard set of terms.

- A *check* is one of Proselint's lint rules, for example `annotations.misc`
- A *term* is a word or phrase that Proselint will either flag or recommend as a
  replacement
- A *term pair* or *entry* is a set of two terms that make up part of a check,
  where one will be flagged, and the other will be recommended.
- A *lint file* is a document that Proselint will analyze text from
- A *check result* is an individual suggestion from one check, lacking
  contextual information about the lint file
- A *lint result* is an extension of a check result, including contextual
  information about the lint file

## Technical Requirements

Checks can be rather cumbersome, particularly in large volumes. To combat this,
we have devised a set of implementation requirements:

- Checks with more than 150 entries should be batched into chunks of 150
- Checks with more than 50 entries should have their contents factored out into
  a separate file, formatted as a CSV and bearing the same name as the last
  element of the check path. For example, `cliches.misc.write_good` has the
  associated file `write-good`

## Suitability

It is difficult to ensure Proselint's catalog of checks remains both tidy and
as useful as possible. We have established guidance here for deciding how
suitable a check is for inclusion. These are written in descending order of the
number of checks they are likely to impact.

### Infrastructure

Analysis of the English language is no easy task. The same intricacy and
flexibility that makes it beautiful often lead to ambiguities that projects like
Proselint cannot efficiently handle.

For now, most of the checks that Proselint cannot implement are ones that
require syntactic analysis to differentiate acceptable forms from wildly
incorrect ones. We intend to resolve this in the future with Natural Language
Processing, but in the meantime, it precludes many checks.

You should also consider how useful a check is in contrast with its
implementation cost. Checks that require a lot of work to support may not be
worthwhile if they are only applicable in niche cases. Along similar lines, the
aim of the project is to give writing advice — some checks, such as those for
features of specific document formats like URLs, are wholly unsuitable for
Proselint.

### False Positives

One of the core tenets of the project is to minimize false positives, as
discussed in our [philosophy declaration]. Checks that encounter frequent false
positives, thereby producing a poor [lintscore], may be unsuitable for Proselint
if they cannot be refined for precision.

[philosophy declaration]: https://github.com/amperser/proselint/blob/main/docs/philosophy.md
[lintscore]: https://github.com/amperser/proselint/blob/main/docs/philosophy.md#lintscore

### Sources

We are fully accountable for the advice Proselint presents to its users. On this
basis, it should be possible for anyone at any time to read and reason about the
justification for a check. All checks **must** cite at least one open-access
source from a credible author, article, or usage guide.

### Common Usage

While there is an inherently prescriptivist nature in giving advice on prose, it
is important to acknowledge that language evolves freely and continuously.
Common usage should have the final say in situations where sources may disagree
or there is no clear advantage to a particular solution.

Another relevant factor is consistency. Two opposing solutions may not be
necessarily wrong on their own, but they are definitely wrong when they are
mixed. An elementary example of this is spellings from British English and
American English.
