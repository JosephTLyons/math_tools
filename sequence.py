def fibonacci(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n < 2:
        return n

    total = 0
    previous_one = 1
    previous_two = 0

    while n >= 2:
        total = previous_one + previous_two
        previous_two = previous_one
        previous_one = total
        n -= 1

    return total
