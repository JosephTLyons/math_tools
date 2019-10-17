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


class TestLCM:
    def test_lcm_same(self):
        assert number_theory.lcm(1, 1) == 1

    def test_lcm_a_multiple_b(self):
        assert number_theory.lcm(9, 3) == 9

    def test_lcm_b_multiple_b(self):
        assert number_theory.lcm(3, 9) == 9

    def test_lcm_normal(self):
        assert number_theory.lcm(4, 6) == 12
        assert number_theory.lcm(3, 5) == 15
        assert number_theory.lcm(8, 20) == 40

    def test_lcm_of_large_two_primes(self):
        assert number_theory.lcm(1013, 4297) == 4_352_861
