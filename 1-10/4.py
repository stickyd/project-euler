import math

def is_palendrome(s):
    # Determines whether the string 's' is a palendrome
    for i in range(0, int(math.ceil(len(s) / 2))):
        if s[i] != s[len(s) - i - 1]: return False
    return True

assert not is_palendrome("hello")
assert is_palendrome("abccba")
assert is_palendrome("abcba")

largest = 0
for i in range(100,1000):
    for j in range(i,1000):
        n = i * j
        if is_palendrome(str(n)):
            largest = max(largest, n)

print largest
