def factorial(n):
    return factorial_division(n, 0)


# This function can be called when you have (numerator! / denominator!)
# and is more efficient than computing the factorials first then dividing
def factorial_division(numerator, denominator):
    if numerator < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    total = 1

    while numerator > denominator:
        total *= numerator
        numerator -= 1

    return total


# n = objects, r = sample
def ncr(n, r):
    return npr(n, r) / factorial(r)


# n = objects, r = sample
def npr(n, r):
    if n < 0 or r < 0:
        raise ValueError("nCr/nPr requires non-negative n and r values")

    if r == 0:
        return 1

    return factorial_division(n, n - r)
