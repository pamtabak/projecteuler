# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from utils import is_prime
import math

def largest_prime_factor (number):
    prime_factor = -1
    for i in range(2, int(math.floor(math.sqrt(number)))):
        if (is_prime(i) and number % i == 0):
            prime_factor = i
    return prime_factor

print(largest_prime_factor(600851475143))
