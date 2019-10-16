from number_theory import euclids_gcd


def reduce_fraction(a, b):
    gcd = euclids_gcd(a, b)
    return (a / gcd, b / gcd)
