# Smallest multiple
# Problem 5
# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by 
# all of the numbers from 1 to 20?

# Notes:
# All numbers are divisible by 1
# All even numbers are divisible by 2
# All even numbers that are multiples of 10 are divisible by 5
# Multiples of 30 to cover 2,3,5

# 2520 is the number  

# only for nums between 1 and 20
# start at 2520 go every 30

def smallest_multiple(multiple, start, end):
    multiple = 2520
    nums_list = [i for i in range(2,21)]

    while True:
        multiple_flag = True
        for i in nums_list:
            if multiple % i != 0:
                multiple_flag = False
        if multiple_flag == True:
            break
        multiple += 30

    return multiple

# import time
# start = time.time()
# print(smallest_multiple(2520,2,21)) # Start Multiple at 2520
# end = time.time()
# print(end-start) # time = 6.6 

# Congratulations, the answer you gave to problem 5 is correct.
# You are the 489556th person to have solved this problem.
# This problem had a difficulty rating of 5%.
# The highest difficulty rating you have solved remains at 5%.
# Answer is 232792560

# More Efficient Way

def prime_factor_list(target):
    prime_list = []
    if target % 2 == 0:
        while target % 2 == 0 and target != 1:
            target /= 2
            prime_list.append(2)
    factor = 3
    while target > factor:
        if target % factor == 0:
            while target % factor == 0 and target != factor:
                prime_list.append(factor)
                target /= factor
        factor += 2
    if target != 1: prime_list.append(int(target))
    return (prime_list)

# Note: end is inclusive 
def smallest_multiple_better(start, end):
    high_level_prime_factor_list = []

    for i in range(start,end+1):
        curr_factor_list = prime_factor_list(i)
        for i in curr_factor_list:
            if i in high_level_prime_factor_list:
                high_level_prime_factor_list.remove(i)
        high_level_prime_factor_list.extend(curr_factor_list)

    product = 1
    for i in high_level_prime_factor_list:
        product *= i
    return product

import time
start = time.time()
print(smallest_multiple_better(2,21))
end = time.time()
print(end-start)