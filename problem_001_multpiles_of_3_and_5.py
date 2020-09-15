# Multiples of 3 and 5
# Problem 1
# https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples(num):
    sum_of_multiples = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i
    return sum_of_multiples

# print(multiples(10))
print(multiples(1000))

# Better Solution

def sum_divisible_by(n, target):
    p = target // n
    return n * (p*(p+1)) / 2

def multiples_of_two_num(num1, num2, target):
    num1_sum = sum_divisible_by(num1, target)
    num2_sum = sum_divisible_by(num2, target)
    product_of_nums_sum = sum_divisible_by(num1*num2, target)
    return num1_sum + num2_sum - product_of_nums_sum

print(multiples_of_two_num(3,5,1000))