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

## Verification

Retaining the trust of users is essential to the advisory role of Proselint. We
are responsible for providing an explanation and justification for every check
we implement, and in this section we will explore the format such information
should be laid out in.

All check modules must have documentation strings with three sections: the
brief, the data, and the description. Below you will find descriptions of each.

- **The Brief**: In line with our code style, this is a single line of no more
  than 80 characters summarizing what the module helps the user to achieve in
  the imperative tense. For example, `hedging` has the brief "Avoid undermining
  yourself with uncertainty"
- **The Data**: This is a YAML header section enclosed with single lines of
  three dashes on both sides. It has several fields designed to store useful
  information about the module and where its checks originate. Any fields in
  this section exceeding 80 characters to one line should be broken up with a
  folded-style stripping block scalar (`>-`) according to the YAML specification
  - `title`: The Title Cased name of the check module
  - `source`: The source of the checks, formatted according to the citation
    style of the 9th edition MLA Handbook of The Modern Language Association of
    America ([summary]). You should omit the dates, URL, and location
  - `source_url`: A link to a reliable archive hosting the source if it is
    open-access, or the link to its DOI otherwise
  - `format`: The type of source cited. This is expected to be `book` in most
    cases, but the kebab-cased form of any MLA source type is acceptable
  - `date_published`: The date the source was published, formatted as a
    delimited ISO 8601 date
  - `date_retrieved`: The date you accessed the source
- **The Description**: This is where the module's checks are described and
  justified in more detail, with references to and excerpts from the source

These sections are to be laid out in that order and separated with a single
blank line each. All together, the format can be summarized with the following
bare template.

```py
"""
<brief description>

---
title:
source:
source_url:
format:
date_published:
date_retrieved:
---

<detailed explanation with source excerpts>
"""
```

[summary]: https://owl.purdue.edu/owl/research_and_citation/mla_style/mla_formatting_and_style_guide/mla_formatting_and_style_guide.html
