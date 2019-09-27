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
