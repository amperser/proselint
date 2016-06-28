"""Test the spaCy tool."""

from spacy.en import English
from proselint.tools import create_nlp


def test_spacy():
    """Test spaCy as a standalone package."""
    nlp = English()
    doc = nlp(u'Time flies like an arrow.')
    token = doc[0]
    assert token.orth_ == u"Time"


def test_spacy_tool():
    """Test spaCy as a Proselint tool."""
    nlp = create_nlp()
    doc = nlp(u"Man bites dog.")
    token = doc[0]
    assert token.orth_ == u"Man"
