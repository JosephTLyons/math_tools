import pytest

from combinatorics import *


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
