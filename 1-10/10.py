import math

def find_primes(n):
    # Finds all prime numbers below n, returning as an array
    # Uses the 'Sieve of Eratosthenes' method
    is_prime = [False, False]
    for i in range(2, n):
        is_prime.append(True)
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        j = i + i
        while j < n:
            is_prime[j] = False
            j += i
    primes = []
    for i in range(0, len(is_prime)):
        if is_prime[i]: primes.append(i)
    return primes

assert sum(find_primes(10)) == 17
print sum(find_primes(2000000))
