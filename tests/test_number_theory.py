import pytest

import number_theory


class TestEuclidsGCD:
    def test_gcd_of_1(self):
        assert number_theory.euclids_gcd(1, 4) == 1
        assert number_theory.euclids_gcd(4, 12) == 4
        assert number_theory.euclids_gcd(6, 12) == 6
        assert number_theory.euclids_gcd(3, 12) == 3

    def test_standard_euclid(self):
        assert number_theory.euclids_gcd(4, 12) == 4
        assert number_theory.euclids_gcd(6, 12) == 6
        assert number_theory.euclids_gcd(3, 12) == 3
        assert number_theory.euclids_gcd(9, 21) == 3
