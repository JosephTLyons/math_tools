import pytest

import combinatorics


class TestFactorial:
    def test_factorial_neg_value(self):
        with pytest.raises(ValueError):
            combinatorics.factorial(-1)

    def test_factorial_base(self):
        assert combinatorics.factorial(0) == 1

    def test_factorial_none_base_values(self):
        assert combinatorics.factorial(1) == 1
        assert combinatorics.factorial(2) == 2
        assert combinatorics.factorial(3) == 6
        assert combinatorics.factorial(4) == 24
        assert combinatorics.factorial(5) == 120
        assert combinatorics.factorial(6) == 720


class TestFactorialDivision:
    def test_negative_numerator(self):
        with pytest.raises(ValueError):
            combinatorics.factorial_division(-10, 2)

    def test_negative_demonimator(self):
        with pytest.raises(ValueError):
            combinatorics.factorial_division(10, -2)

    def test_factorial_division(self):
        assert combinatorics.factorial_division(10, 8) == 90
        assert combinatorics.factorial_division(20, 19) == 20


class TestNCR:
    def test_negative_ncr_values(self):
        with pytest.raises(ValueError):
            combinatorics.ncr(-1, 3)

    def test_zero_ncr(self):
        assert combinatorics.ncr(20, 0) == 1

    def test_normal_ncr(self):
        assert combinatorics.ncr(4, 3) == 4
        assert combinatorics.ncr(8, 3) == 56


class TestNPR:
    def test_negative_npr_values(self):
        with pytest.raises(ValueError):
            combinatorics.npr(-1, 3)

    def test_zero_npr(self):
        assert combinatorics.npr(20, 0) == 1

    def test_normal_npr(self):
        assert combinatorics.npr(5, 2) == 20
        assert combinatorics.npr(10, 4) == 5040
        assert combinatorics.npr(10, 8) == 1814400
