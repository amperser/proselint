"""Test the Cliches.misc module."""

from proselint.checks.cliches import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for cliches.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def setUp(self):
        """Create test sentences."""
        self.l_garner = """Worse than a fate worse than death."""
        self.l_write_good = """He's a chip off the old block."""
        self.l_gnu_diction = """It's a matter of concern."""
        self.l_nigel = """He's sick and tired of it."""

    def test_cliches_garner_basic(self):
        """Basic checks on check_cliches_garner."""
        assert chk.check_cliches_garner("""No cliches here.""") == []
        # use one of the example cliches to verify basic functionality
        assert chk.check_cliches_garner(self.l_garner) != []
        assert "cliches.garner" in chk.check_cliches_garner(self.l_garner)[0]

    def test_cliches_write_good_basic(self):
        """Basic checks on check_cliches_write_good."""
        assert chk.check_cliches_write_good("""No cliches here.""") == []
        # use one of the example cliches to verify basic functionality
        assert chk.check_cliches_write_good(self.l_write_good) != []
        assert "cliches.write_good" in chk.check_cliches_write_good(
            self.l_write_good)[0]

    def test_cliches_gnu_diction_basic(self):
        """Basic check on check_cliches_gnu_diction."""
        assert chk.check_cliches_gnu_diction("""No cliches here.""") == []
        # use one of the example cliches to verify basic functionality
        assert chk.check_cliches_gnu_diction(self.l_gnu_diction) != []
        assert "cliches.gnu_diction" in chk.check_cliches_gnu_diction(
            self.l_gnu_diction)[0]

    def test_cliches_nigel_basic(self):
        """Basic check on check_cliches_nigel."""
        assert chk.check_cliches_nigel("""No cliches here.""") == []
        # use one of the example cliches to verify basic functionality
        assert chk.check_cliches_nigel(self.l_nigel) != []
        assert "cliches.nigel" in chk.check_cliches_nigel(
            self.l_nigel)[0]
        