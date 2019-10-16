import math

from number_theory import euclids_gcd


def is_prime(n):
    return get_first_prime_factor(n) is None


def are_coprimes(a, b):
    return euclids_gcd(a, b) == 1


def get_first_prime_factor(x):
    upper_limit = int(math.sqrt(x))

    for possible_factor in range(2, upper_limit + 1):
        if x % possible_factor == 0:
            return possible_factor

    return None


def get_prime_factors(x):
    prime_list = []
    first_factor = get_first_prime_factor(x)

    if first_factor is None:
        return []

    while first_factor is not None:
        prime_list.append(first_factor)
        x /= first_factor
        first_factor = get_first_prime_factor(int(x))

    if len(prime_list) != 0:
        prime_list.append(x)

    return prime_list


# def get_primes_up_to(n):
# using sieve
# algorithm to get first x amount of primes
