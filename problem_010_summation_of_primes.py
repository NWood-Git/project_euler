# Summation of primes
# Problem 10
# https://projecteuler.net/problem=10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Additional Notes:
# Some useful facts:
# 1 is not a prime.
# All primes except 2 are odd.
# All primes greater than 3 can be written in the form 6k+/-1.
# Any number n can have only one primefactor greater than n.


def prime_nums_less_than(num):
    prime_list = [2, 3]
    prime_sum = 5
    for i in range(1, int(num/6)+1):
        upper = 6*i + 1
        lower = 6*i - 1
        upper_flag = True
        lower_flag = True
        for j in prime_list:
            if j >= (upper **.5 + 1):
                break
            else:
                if upper_flag is False and lower_flag is False:
                    break
                if upper_flag is True and upper % j == 0: upper_flag = False
                if lower_flag is True and lower % j == 0: lower_flag = False
        if lower_flag is True:
            prime_list.append(lower)
            prime_sum += lower
        if upper_flag is True:
            prime_list.append(upper)
            prime_sum += upper
    return prime_sum #, prime_list
    # return len(prime_list)

# import time
# start = time.time()
# print(prime_nums_less_than(10000000))
# end = time.time()
# print(f"runtime: {end-start}")

import time
start = time.time()
print(prime_nums_less_than(2000000))
end = time.time()
print(f"runtime: {end-start}")

# Congratulations, the answer you gave to problem 10 is correct.
# You are the 326842nd person to have solved this problem.
# You have earned 1 new award:
# Decathlete: Solve ten consecutive problems
# This problem had a difficulty rating of 5%.
# The highest difficulty rating you have solved remains at 5%. 
# The answer is: 142913828922

# This works but 2mm is too big to process

def prime_nums_less_than_slow(num):
    prime_lst = [2]
    prime_sum = 2
    for i in range(3,num,2):
        prime_status = True
        for j in prime_lst:
            if i % j == 0:
                prime_status = False
                break
        if prime_status is True:
            prime_sum += i
            prime_lst.append(i)
    return prime_sum

# print(prime_nums_less_than_slow(5000))
