---
layout:     post
title:      How to contribute
date:       2014-06-10 12:31:19
summary:    How to contribute to Proselint.
categories: proselint contributors
---

Interested in contributing to <tt>proselint</tt>? Great &mdash; there are plenty of ways you can help. In the following sections, we describe how you can help us build <tt>proselint</tt> into the greatest writing tool in the world.

## Coding
Have coding skills? You can:

+ Implement a new piece of advice in the linter. In our issue tracker on Github, we maintain an ever-growing [list of rules](https://github.com/amperser/proselint/labels/rule) that have been extracted from expert advice on writing. Some of these are one-liners that will take only a moment to complete; others are full-blown research projects. Use existing checks as a guide for creating your own. Then open a pull request.
+ Create a plugin for a new text editor. We currently have a plugin for Sublime Text plugin and a web editor. Many [more are needed](https://github.com/amperser/proselint/labels/plugin), most notably Microsoft Word, emacs, vim, and Google Docs.
+ Fix [bugs](https://github.com/amperser/proselint/labels/bug).
+ Improve [performance](https://github.com/amperser/proselint/labels/speed).
+ Write tests. Our test coverage is too low. Keeping out false alarms is key to the tool's success and anything we can do to uncover false alarms and prevent regressions is thus key to the tool's success.

## Writing and editing
Have writing or editing skills? You can:

+ Extract rules from expert sources of advice. Read through some entries of a book like *Garners Modern American Usage* find rules that are feasible to implement in code, and then [open an issue on Github](https://github.com/amperser/proselint/issues/new). Here's an [example](https://github.com/amperser/proselint/issues/163) of a successfully extracted rule. And here's a list of [sources](https://github.com/amperser/proselint/labels/extraction) from which rules can be extracted.
+ Find false alarms. Run <tt>proselint</tt> over your favorite books or magazine articles — maybe even some of your own writing, and find places where <tt>proselint</tt> says that there is an error, but in reality, there is none. [open an issue on Github] describing the problem.
+ Improve the copy on this website. Or write documentation in the code.

## Donations
Looking to donate to an open-source software and research project? We accept.

+ Donate via [PayPal](https://www.paypal.com/webapps/mpp/donations).

<hr/>

For questions and feature requests, write to us at <a href="mailto:hello@proselint.com">hello@proselint.com</a>.
