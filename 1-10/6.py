def sum_squares(n):
    # Sums the squares of the the numbers 1 -> n
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

def sum_squared(n):
    # The square of the sum of the numbers 1 -> n
    total = n * (n + 1) / 2
    return total * total

def sum_square_difference(n):
    # The differencer between sum_squared and sum_squares for n
    return sum_squared(n) - sum_squares(n)

assert sum_square_difference(10) == 2640
print sum_square_difference(100)
