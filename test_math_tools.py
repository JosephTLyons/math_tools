#!/usr/bin/env python3

import pytest
from math_tools import *


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