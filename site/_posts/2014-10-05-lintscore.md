---
layout:     post
title:      Lintscore
date:       2014-06-10 12:31:19
summary:    Computing the lintscore
categories: proselint performance
---

Proselint's "lintscore" metric, which we use to evaluate its performance, reflects the desire to have a linter that catches many errors, but which takes false alarms seriously. Better to say nothing than to say the wrong thing. And the harm from saying the wrong thing is greater than the benefit of having said the right thing. Thus our score metric is defined as

*T* (*T* / (*F* + *T*)) <sup>*k*</sup>,

where *T* is the number of true positives (hits), *F* is the number of false positives (false alarms), and *k* > 0 is a temperature parameter that determines the penalty for imprecision. In general, we choose as large a value of *k* as we can stomach, one that strongly discourages the creation of rules that can't be trusted. Suppose that *k* = 2. Then if the linter detects 100 errors, of which 10 are false positives, the score is 72.9.

---

For questions and feature requests, write to us at <a href="mailto:hello@proselint.com">hello@proselint.com</a>.
