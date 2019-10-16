def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    total = 1

    while n > 0:
        total *= n
        n -= 1

    return total
