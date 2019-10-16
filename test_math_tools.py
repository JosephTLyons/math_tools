#!/usr/bin/env python3

import pytest
from math_tools import *


class TestQuadratic:
    def test_has_x_intercepts_1(self):
        # -2x^2 + x + 3
        assert [-1.0, 1.5] == quadratic(-2, 1, 3)

    def test_has_x_intercepts_2(self):
        # x^2 - 4
        assert [-2.0, 2.0] == quadratic(1, 0, -4)

    def test_has_x_intercepts_3(self):
        # 3x^2 + 3x
        assert [-1.0, 0] == quadratic(3, 3, 0)

    def test_has_one_x_intercept_1(self):
        # x^2
        assert [0] == quadratic(1, 0, 0)

    def test_has_one_x_intercept_2(self):
        # -x^2
        assert [0] == quadratic(-1, 0, 0)

    def test_has_no_x_intercepts_1(self):
        # x^2 + 1 : no X intercepts
        assert [] == quadratic(1, 0, 1)

    def test_has_no_x_intercepts_2(self):
        # -x^2 - 1 : no X intercepts
        assert [] == quadratic(-1, 0, -1)

    def test_is_not_a_quadratic_function(self):
        # 0x^2 + 1x + 0 : isn't a quadratic
        with pytest.raises(ValueError):
            quadratic(0, 1, 0)


class TestFactorial:
    def test_factorial_neg_value(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_factorial_base(self):
        assert factorial(0) == 1

    def test_factorial_none_base_values(self):
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120
        assert factorial(6) == 720


class TestFibonacci:
    def test_fib_neg_value(self):
        with pytest.raises(ValueError):
            fibonacci(-1)

    def test_fib_base_0(self):
        assert fibonacci(0) == 0

    def test_fib_base_1(self):
        assert fibonacci(1) == 1

    def test_fib_non_base_values(self):
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5
        assert fibonacci(6) == 8
        assert fibonacci(7) == 13
        assert fibonacci(8) == 21
        assert fibonacci(9) == 34
        assert fibonacci(10) == 55

    def test_fib_large_number(self):
        assert fibonacci(100) == 354224848179261915075


class TestIntersection:
    def test_for_intersection(self):
        assert intersection(2, 1, 3, 1) == (0, 1)
        assert intersection(-3, 3, (1 / 5), 3) == (0, 3)

    def test_for_no_intersection(self):
        with pytest.raises(ValueError):
            intersection(0, 1, 0, 2)


class TestEuclidsGCD:
    def test_euclid(self):
        assert euclids_gcd(4, 12) == 4
        assert euclids_gcd(6, 12) == 6
        assert euclids_gcd(3, 12) == 3


class TestEuclidsGCD:
    def test_gcd_of_1(self):
        assert euclids_gcd(1, 4) == 1

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


class TestAreCoprimes:
    def test_are_coprimes(self):
        assert not are_coprimes(3, 9)
        assert are_coprimes(11, 18)


class TestGetFirsTPrimeFactor:
    def test_get_first_prime_factor(self):
        assert get_first_prime_factor(24) == 2
        assert get_first_prime_factor(15) == 3
        assert get_first_prime_factor(29) is None


class TestGetPrimeFactors:
    def test_prime_numbers_for_input(self):
        assert get_prime_factors(1) == []
        assert get_prime_factors(2) == []
        assert get_prime_factors(982_451_653) == []

    def test_non_prime_numbers_for_input(self):
        assert get_prime_factors(4) == [2, 2]
        assert get_prime_factors(12) == [2, 2, 3]
        assert get_prime_factors(5 * 6 * 7 * 8 * 9) == [2, 2, 2, 2, 3, 3, 3, 5, 7]
        assert get_prime_factors(1024) == ([2] * 10)