import sys
import math

def is_prime(n):
    # Determines whether n is a prime number
    if n % 2 == 0: return False
    a = math.ceil(math.sqrt(n))
    b2 = a * a - n
    while (math.sqrt(b2) % 1 != 0):
        a += 1
        b2 = a * a - n
    return a - math.sqrt(b2) == 1

def largest_prime_factor(n):
    # Finds the largest prime factor of a given number, or 0
    # Noting that we know all prime factors will be < sqrt
    m = int(math.ceil(math.sqrt(n)))
    for i in reversed(range(1, m)):
        if n % i == 0 and is_prime(i):
            return i
    return 0

assert largest_prime_factor(13195) == 29
print largest_prime_factor(600851475143)
