# Smallest multiple

# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

def is_prime (number):
    #to check if a number is prime we dont need to check if it is divided by all number - 1
    #we only need to check until sqrt
    for i in range (2, int(math.ceil(math.sqrt(number))) + 1):
        if (number % i == 0):
            return False
    return True

def prime_factorization (number):
    factors        = {}
    current_prime  = 2
    current_number = number
    while (current_number != 1):
        if (current_number % current_prime == 0):
            if (current_prime not in factors):
                factors[current_prime] = 0
            factors[current_prime] += 1
            current_number = current_number/current_prime
        else:
            current_prime += 1
            while (not is_prime(current_prime)):
                current_prime += 1
    return factors

def smallest_evenly_divisible(numbers):
    divs = {}
    for i in range(len(numbers) - 1, -1, -1):
        number  = numbers[i]
        factors = prime_factorization(number)
        for f in factors:
            if (f not in divs):
                divs[f] = factors[f]
            else:
                if (divs[f] < factors[f]):
                    divs[f] = factors[f]
    smallest_div = 1
    for d in divs:
        smallest_div *= d**(divs[d])
    return smallest_div

#all numbers divisible by 20 are also divisible by 2, 4, 5 an 10
#all numbers divisible by 18 are also divisible by 3, 6
#all numbers divisible by 16 are also divisible by 8
#all numbers divisible by 14 are also divisible by 7
numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(smallest_evenly_divisible(numbers))