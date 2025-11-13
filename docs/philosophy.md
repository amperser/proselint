# Philosophy

## Brief

The philosophy of Proselint is preserved here as a direct excerpt from posts
made on the website on 2014-06-10 05:31:19Z-07. It should be referred to in
matters of deciding what the project should aim to achieve, and what it should
avoid.

Note that for lack of an open corpus, we are currently unable to keep track of
the lintscore. We aim to resolve this in the future.

## Approach

Is `proselint` yet another awful grammar checker?

*No*. Here's why not:

1. `proselint` does not focus on grammar, which is at once too easy and too hard
   — too eassy because, for most native speakers, it comes naturally; too hard
   because, in its most general form, detecting grammatical errors is
   AI-complete, requiring human-level intelligence to get things right. Instead,
   we consider usage: redundancy, illogic, clichés, sexism, misspelling,
   inconsistency, misuse of symbols, malapropisms, oxymorons, security gaffes,
   hedging, apologizing, pretension, and more.
2. `proselint` is precise. Existing tools for improving prose raise so many
   false alarms that their advice cannot be trusted. Instead, the writer must
   carefully consider whether to accept or reject each change. We aim for a tool
   so precise that it becomes possible to unquestioningly adopt its
   recommendations and still come out ahead — with stronger, tighter prose.
   Better to be quiet and authoritative than loud and unreliable. We measure the
   performance of `proselint` by tracking its [lintscore](#lintscore).
3. `proselint` defers to the world's greatest writers and editors. We didn't
   make up this advice on our own. Instead, we aggregated their expertise,
   giving you direct access to humanity's collective understanding about the
   craft of writing.

## Lintscore

Proselint's "lintscore" metric, which we use to evaluate its performance,
reflects the desire to have a linter that catches many errors, but which takes
false alarms seriously. Better to say nothing than to say the wrong thing. And
the harm from saying the wrong thing is greater than the benefit of having said
the right thing. Thus our score metric is defined as

$$T \left(\frac{T}{F + T}\right)^k$$

where *T* is the number of true positives (hits), *F* is the number of false
positives (false alarms), and *k* > 0 is a temperature parameter that determines
the penalty for imprecision. In general, we choose as large a value of *k* as we
can stomach, one that strongly discourages the creation of rules that can't be
trusted. Suppose that *k* = 2. Then if the linter detects 100 errors, of which
10 are false positives, the score is 72.9.
