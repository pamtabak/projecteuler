# Sum square difference
# Problem 6

# Find the difference between the sum of the squares of the first one hundred natural numbers 
# and the square of the sum

def sum_of_squares (first_number, last_number):
    total = 0
    for number in range (first_number, last_number + 1):
        total += (number**2)
    return total

def square_of_sum (first_number, last_number):
    total = 0
    for number in range (first_number, last_number + 1):
        total += number
    total = total ** 2
    return total

diff = sum_of_squares(1, 100) - square_of_sum(1, 100)
print(diff)