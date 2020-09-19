# Sum square difference
# Problem 6
# https://projecteuler.net/problem=6

# The sum of the squares of the first ten natural numbers is,

# 1**2 + 2**2 + . . . + 10**2 = 385

# The square of the sum of the first ten natural numbers is,

# (1 + 2 + . . . + 10)**2 = 55**2 = 3025

# Hence the difference between the sum of the squares of the 
# first ten natural numbers and the square of the sum is:

# 3025 -385 = 2640

# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.

import time

def sum_square_difference(start, end):
    import numpy as np
    num_list = np.array([i for i in range(start, end+1)])
    sum_of_squares = np.square(num_list).sum()
    square_of_sum = (num_list.sum())**2
    return square_of_sum - sum_of_squares

start = time.time()
print(sum_square_difference(1,100))
end = time.time()
print(end-start)

#Answer = 25164150
# Missed the correct blurb

# Without numpy -- It is daster without numpy

def sum_list(lst):
    total = 0
    for i in lst:
        total += i
    return total

def sum_square_difference_no_np(start, end):
    num_list = [i for i in range(start, end+1)]
    square_of_sum = sum_list(num_list)**2
    sum_of_squares = sum_list([i**2 for i in num_list])
    return square_of_sum - sum_of_squares

start = time.time()
print(sum_square_difference_no_np(1,100))
end = time.time()
print(end-start)

