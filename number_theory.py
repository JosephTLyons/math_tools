def euclids_gcd(a, b):
    remainder = 1

    if a == b:
        return a

    while remainder != 0:
        remainder = a % b
        a = b
        b = remainder

    return a


def lcm(a, b):
    if a == b:
        return a

    if a % b == 0:
        return a

    elif b % a == 0:
        return b

    return (a * b) / euclids_gcd(a, b)
