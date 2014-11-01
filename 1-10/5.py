def is_divisible(n, i, j):
    # Whether n is evenly divisible by all values i->j
    for k in range(i, j + 1):
        if n % k != 0: return False
    return True

def find_divisible(i, j):
    # Finds the lowest number divible by all values i->j
    n = 0
    while True:
        n += j
        if is_divisible(n, i, j): return n

assert find_divisible(1, 10) == 2520
print find_divisible(1, 20)
