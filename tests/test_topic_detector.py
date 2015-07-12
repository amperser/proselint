"""Test the topic detector tool."""

from proselint.tools import topics


def test_50_Cent_detector_on_topic():
    """Check precision of the 50 Cent topic-detector."""
    text = """With the aid of Eminem and Dr. Dre (who produced his first
           major-label album, Get Rich or Die Tryin'), Jackson became one
           of the world's best selling rappers and rose to prominence with
           East Coast hip hop group G-Unit (which he leads de facto). """

    assert("50 Cent" in topics(text))

    text = """Hip hop was started in the early 50's."""
    assert("50 Cent" not in topics(text))

    text = """Nowadays it costs 50 cents to buy a lollipop."""
    assert("50 Cent" not in topics(text))
