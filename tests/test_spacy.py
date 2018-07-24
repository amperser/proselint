"""Tests for spaCy integration."""
import spacy


def test_spacy_nlp():
    """Load spaCy and run it on a sample sentence."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(u"The quick brown fox jumped over the lazy dog")
    assert len([n for n in doc.noun_chunks]) == 2
    assert len([s for s in doc.sents]) == 1
