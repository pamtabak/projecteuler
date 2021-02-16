import math

def is_prime (number):
    #to check if a number is prime we dont need to check if it is divided by all number - 1
    #we only need to check until sqrt
    for i in range (2, int(math.ceil(math.sqrt(number))) + 1):
        if (number % i == 0):
            return False
    return True