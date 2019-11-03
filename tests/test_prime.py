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

    def test_get_prime_numbers_up_to_100(self):
        assert [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
            89, 97
        ] == prime.get_prime_numbers_up_to(100)

    def test_get_prime_numbers_up_to_1000(self):
        assert [
            2,   3,   5,   7,   11,  13,  17,  19,  23,  29,  31,  37,  41,  43,  47,  53,  59,
            61,  67,  71,  73,  79,  83,  89,  97,  101, 103, 107, 109, 113, 127, 131, 137, 139,
            149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
            239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337,
            347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
            443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557,
            563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653,
            659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769,
            773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883,
            887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
        ] == prime.get_prime_numbers_up_to(1000)
