# Special Pythagorean triplet

# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def is_pythagorean_triplet(a, b, c):
    if ((a**2 + b**2) == (c**2)):
        return True
    return False

# one option is to generate all possible combinations where a + b + c = 1000 and a < b < c
def find_specific_pythagorean_triplet (total):
    for a in range (0, total - 2):
        for b in range (a + 1, total - 1):
            for c in range (b + 1, total):
                if (a + b + c != total):
                    continue
                if (is_pythagorean_triplet(a, b, c)):
                    return a*b*c

print(find_specific_pythagorean_triplet(1000))