# Largest palindrome product

# Problem 4
# A palindromic number reads the same both ways.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome (number):
    str1 = str(number)
    str2 = str1[::-1]
    return str1 == str2

def largest_palindrome (digit):
    largest_number     = (10**digit) - 1
    smallest_number    = (10**(digit -1)) - 1
    largest_palindrome = -1
    for first_number in range (largest_number, smallest_number, -1):
        for second_number in range (first_number, smallest_number, -1):
            product = first_number * second_number
            if (is_palindrome(product) and product > largest_palindrome):
                largest_palindrome = product
                #we dont need to go all the way in the inner foreach
                #since this is the largest palindrome for this iteraction, we can reduce the amount
                #of iterations by updating the smallest_number
                smallest_number = second_number
    return largest_palindrome

print(largest_palindrome(3))

