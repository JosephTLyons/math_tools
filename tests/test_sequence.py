import pytest

import sequence


class TestFibonacci:
    def test_fib_neg_value(self):
        with pytest.raises(ValueError):
            sequence.fibonacci(-1)

    def test_fib_base_0(self):
        assert sequence.fibonacci(0) == 0

    def test_fib_base_1(self):
        assert sequence.fibonacci(1) == 1

    def test_fib_non_base_values(self):
        assert sequence.fibonacci(2) == 1
        assert sequence.fibonacci(3) == 2
        assert sequence.fibonacci(4) == 3
        assert sequence.fibonacci(5) == 5
        assert sequence.fibonacci(6) == 8
        assert sequence.fibonacci(7) == 13
        assert sequence.fibonacci(8) == 21
        assert sequence.fibonacci(9) == 34
        assert sequence.fibonacci(10) == 55

    def test_fib_large_number(self):
        assert sequence.fibonacci(100) == 354224848179261915075
