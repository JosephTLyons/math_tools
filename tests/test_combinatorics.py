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