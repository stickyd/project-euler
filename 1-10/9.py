def find_triplet(n):
    # Finds a Pythagorean triplet where abc=n, returning [a,b,c]
    for a in range(1, n / 3):
        for b in range(a + 1, n - a - 1):
            c = n - b - a
            if a * a + b * b == c * c: return [a, b, c]

assert find_triplet(12) == [3, 4, 5]

triplet = find_triplet(1000)
print triplet
print reduce(lambda i, j: i * j, triplet)
