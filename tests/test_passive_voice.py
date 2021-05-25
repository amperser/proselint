"""Tests for passive_voice.passive_voice check."""
from __future__ import absolute_import
from proselint.checks.passive_voice import misc as chk
from .check import Check


class TestCheck(Check):
    """The test class for passive_voice.passive_voice."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    @property
    def test_smoke(self):
        """Basic smoke test for passive_voice.passive_voice."""
        assert self.passes("This sentence is in the active voice.")
        assert self.passes("Harry ate six shrimp at dinner.")
        assert not self.passes("At dinner, six shrimp were eaten by Harry.")
        assert self.passes("Beautiful giraffes roam the savannah.")
        assert not self.passes("The savannah is roamed by beautiful giraffes.")
        assert self.passes("Sue changed the flat tire.")
        assert not self.passes("The flat tire was changed by Sue.")
        assert self.passes("I ran the course in record time.")
        assert not self.passes("The course was run by me in record time.")
        assert self.passes("The choir really enjoys that piece.")
        assert not self.passes("That piece is really enjoyed by the choir.")
        assert self.passes("The two kings are signing the treaty.")
        assert not self.passes("The treaty is being signed by two kings.")

    def test_special_cases(self):
        """
        Test for special cases in passive voice.
        https://multimedia-english.com/grammar/passive-voice-special-cases-52
        """
        assert self.passes(["I got fired yesterday.",
                            "I was fired yesterday.",
                            "If you get mugged, report it."
                            "The balloon got filled with gas."
                            "There was a fight, but nobody got hurt.",
                            "Mary was given some flowers",
                            "I am thought to be a spy",
                            "I was considered to be a tourist.",
                            "I was made to do it.",
                            "We were allowed to go."])
        # Passive imperative, gramatically correct nonesense.
        assert not self.passes(["Let the television be turned off.",
                                "Let your money be given to me."])
        assert self.passes(["We should let him go.",
                            "Let it be known that I will not stand for this.",
                            "This house is available to let. So be it."])
