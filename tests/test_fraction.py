import pytest

import fraction


class TestReduceFraction:
    def test_no_reduction(self):
        assert fraction.reduce_fraction(1, 4) == (1, 4)

    def test_reduce_fraction(self):
        assert fraction.reduce_fraction(9, 12) == (3, 4)
        assert fraction.reduce_fraction(8, 64) == (1, 8)
