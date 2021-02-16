# 10001st prime

# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?

from utils import is_prime

# return the position st prime number
def prime_at_position (position):
    current_prime = 2
    primes_found  = 1
    while (primes_found < position):
        current_prime += 1
        if (is_prime(current_prime)):
            primes_found += 1
    return current_prime

print(prime_at_position(10001))