# Summation of primes

# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from utils import is_prime
import time
from functools import reduce

# this is a simple solution
def sum_all_primes_below(number):
    first_primes = [2, 3, 5]
    sum = reduce(lambda x, y: x + y, first_primes)
    for i in range(first_primes[-1] + 1, number + 1):
        # we can improve it a little bit by removing
        # some numbers that are divisible by the first prime numbers
        if any(i % prime == 0 for prime in first_primes):
            continue
        if is_prime(i):
            sum += i
    return sum


init_time = time.time()
print(sum_all_primes_below(2000000))
end_time = time.time()
print(end_time - init_time)
