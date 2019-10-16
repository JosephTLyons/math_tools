import pytest

from sequence import *


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
