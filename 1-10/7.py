import math

def is_prime(n):
    # Determines whether n is a prime number
    a = 2
    while n > a:
        if n % a == 0 and a != n:
            return False
        a += 1
    return True

i = 1
count = 0
while True:
    i += 1
    if is_prime(i): count += 1
    print count
    if count == 10001:
        print i
        break
