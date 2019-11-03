import pytest

import prime


class TestAreCoprimes:
    def test_are_coprimes(self):
        assert not prime.are_coprimes(3, 9)
        assert prime.are_coprimes(11, 18)


class TestGetFirsTPrimeFactor:
    def test_get_first_prime_factor(self):
        assert prime.get_first_prime_factor(24) == 2
        assert prime.get_first_prime_factor(15) == 3
        assert prime.get_first_prime_factor(29) is None


class TestGetPrimeFactors:
    def test_prime_numbers_for_input(self):
        assert prime.get_prime_factors(1) == []
        assert prime.get_prime_factors(2) == []
        assert prime.get_prime_factors(982_451_653) == []

    def test_non_prime_numbers_for_input(self):
        assert prime.get_prime_factors(4) == [2, 2]
        assert prime.get_prime_factors(12) == [2, 2, 3]
        assert prime.get_prime_factors(5 * 6 * 7 * 8) == [2, 2, 2, 2, 3, 5, 7]
        assert prime.get_prime_factors(1024) == ([2] * 10)


class TestIsPrime:
    def test_primes(self):
        assert prime.is_prime(3)
        assert prime.is_prime(7)
        assert prime.is_prime(11)
        assert prime.is_prime(23)

    def test_non_primes(self):
        assert not prime.is_prime(4)
        assert not prime.is_prime(6)
        assert not prime.is_prime(12)
        assert not prime.is_prime(14)


class TestGetPrimeNumbersUpTo:
    def test_get_prime_numbers_up_to_zero(self):
        assert [] == prime.get_prime_numbers_up_to(0)

    def test_get_prime_numbers_up_to_5(self):
        assert [2, 3, 5] == prime.get_prime_numbers_up_to(5)

    def test_get_prime_numbers_up_to_10(self):
        assert [2, 3, 5, 7] == prime.get_prime_numbers_up_to(10)

    def test_get_prime_numbers_up_to_40(self):
        assert [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37] == prime.get_prime_numbers_up_to(40)
