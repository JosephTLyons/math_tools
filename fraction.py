def euclids_gcd(a, b):
    remainder = 1

    if a == b:
        return a

    while remainder != 0:
        remainder = a % b
        a = b
        b = remainder

    return a


def reduce_fraction(a, b):
    gcd = euclids_gcd(a, b)
    return (a / gcd, b / gcd)
