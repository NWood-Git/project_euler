# Highly divisible triangular number
# Problem 12
# https://projecteuler.net/problem=12

# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

# faster count divisor

def count_divsor(num):
    import math
    limit = math.floor(num ** .5)
    factor_count = 1 if limit ** 2  == num else 0
    step = 2 if num % 2 != 0 else 1
    for i in range(1,limit,step):
        if num % i == 0:
            factor_count += 2
    return factor_count

# real    0m1.971s
# user    0m1.962s
# sys     0m0.008s

def triangle_number_divisors(num_div):
    triangle_num = 3
    curr_num = 2
    while True:
        curr_num += 1
        triangle_num += curr_num
        if count_divsor(triangle_num) >= num_div + 1:
            break
    return triangle_num

print(triangle_number_divisors(500))

# Congratulations, the answer you gave to problem 12 is correct.
# You are the 220531st person to have solved this problem.
# This problem had a difficulty rating of 5%.
# The highest difficulty rating you have solved remains at 5%. 


'''
# Original Slower Count Divisor Fucntion

def count_divsor(num):
    import math
    limit = math.floor(num ** .5)
    factor_count = 1 if limit ** 2  == num else 0
    for i in range(1,limit):
        if num % i == 0:
            factor_count += 2
    return factor_count

# real    0m2.549s
# user    0m2.541s
# sys     0m0.008s
'''


# def get_factors(num):
#     limit = math.floor(num ** .5)
#     factor_set = set()
#     for i in range(1,limit):
#         if num % i == 0:
#             factor_set.add(i)
#             factor_set.add(int(num/i))
#     return factor_set

# print(get_factors(28))