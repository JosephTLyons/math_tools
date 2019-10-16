import pytest

from fraction import *


class TestEuclidsGCD:
    def test_gcd_of_1(self):
        assert euclids_gcd(1, 4) == 1
        assert euclids_gcd(4, 12) == 4
        assert euclids_gcd(6, 12) == 6
        assert euclids_gcd(3, 12) == 3

    def test_standard_euclid(self):
        assert euclids_gcd(4, 12) == 4
        assert euclids_gcd(6, 12) == 6
        assert euclids_gcd(3, 12) == 3
        assert euclids_gcd(9, 21) == 3


class TestReduceFraction:
    def test_no_reduction(self):
        assert reduce_fraction(1, 4) == (1, 4)

    def test_reduce_fraction(self):
        assert reduce_fraction(9, 12) == (3, 4)
        assert reduce_fraction(8, 64) == (1, 8)
