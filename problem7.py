# 10001st prime

# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?

import math

def is_prime (number):
    #to check if a number is prime we dont need to check if it is divided by all number - 1
    #we only need to check until sqrt
    for i in range (2, int(math.ceil(math.sqrt(number))) + 1):
        if (number % i == 0):
            return False
    return True

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