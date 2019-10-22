import pytest

from fraction import Fraction


class TestReduceFraction:
    def test_no_reduction(self):
        fraction = Fraction(1, 4)
        fraction.reduce()
        print(fraction)
        assert fraction.get_fraction_tuple() == (1, 4)

    def test_reduce_fraction(self):
        fraction = Fraction(9, 12)
        fraction.reduce()
        assert fraction.get_fraction_tuple() == (3, 4)

        fraction = Fraction(8, 64)
        fraction.reduce()
        assert fraction.get_fraction_tuple() == (1, 8)


class TestFractionOperations:
    def test_add_fraction(self):
        assert (Fraction(3, 4).add(Fraction(5, 6))).get_fraction_tuple() == (19, 12)

    def test_subtract_fraction(self):
        assert (Fraction(3, 4).subtract(Fraction(5, 6))).get_fraction_tuple() == (-1, 12)
