import pytest

from fraction import Fraction


class TestReduceFraction:
    def test_no_reduction(self):
        fraction = Fraction(1, 4)
        fraction.reduce()
        assert fraction == Fraction(1, 4)

    def test_reduce_fraction(self):
        fraction = Fraction(9, 12)
        fraction.reduce()
        assert fraction == Fraction(3, 4)

        fraction = Fraction(8, 64)
        fraction.reduce()
        assert fraction == Fraction(1, 8)


class TestFractionOperations:
    def test_add_fraction(self):
        assert Fraction(3, 4) + Fraction(5, 6) == Fraction(19, 12)

    def test_subtract_fraction(self):
        assert Fraction(3, 4) - Fraction(5, 6) == Fraction(-1, 12)

    def test_multiply_fraction(self):
        assert Fraction(3, 4) * Fraction(5, 6) == Fraction(5, 8)

    def test_divide_fraction(self):
        assert Fraction(3, 4) / Fraction(5, 6) == Fraction(9, 10)
