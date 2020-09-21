# 10001st prime
# Problem 7
# https://projecteuler.net/problem=7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# Notes: 
# If n is a composite number, then it must be divisible by a prime pp such that:
# p <= sqrt{n}

def nth_prime(n):
    prime_list = [2, 3, 5, 7]
    prime_counter = 4
    num = 9
    while prime_counter < n:
        limit = round(num**.5) +1 
        i = 0
        prime_flag = True
        while prime_list[i] < limit or i == len(prime_list):
            if num % prime_list[i] == 0:
                prime_flag = False
                break
            i +=1
        if prime_flag == True:
            prime_list.append(num)
            prime_counter += 1
        num += 1
    return prime_list[-1]

import time
start = time.time()
print(nth_prime(10001))
end = time.time()
print(f"runtime: {end-start}")

# Congratulations, the answer you gave to problem 7 is correct.
# You are the 420904th person to have solved this problem.
# This problem had a difficulty rating of 5%.
# The highest difficulty rating you have solved remains at 5%.
# Answer is 104743


# Additional Notes:
# Some useful facts:
# 1 is not a prime.
# All primes except 2 are odd.
# All primes greater than 3 can be written in the form 6k+/-1.
# Any number n can have only one primefactor greater than n.

## Interesting - this actually takes longer

def nth_prime_6(n):
    prime_list = [2, 3]
    prime_counter = 2
    num = 6
    while prime_counter < n:
        limit = round(num**.5) +1 
        minus_prime_flag = True
        plus_prime_flag = True
        num_minus = num -1
        num_plus = num + 1
        i = 0
        while prime_list[i] < limit or i == len(prime_list):
            if num_minus % prime_list[i] == 0:
                minus_prime_flag = False
            if num_plus % prime_list[i] == 0:
                plus_prime_flag = False
            i += 1
        if minus_prime_flag == True and plus_prime_flag ==True:
            prime_list.append(num_minus)
            prime_list.append(num_plus)
            prime_counter += 2
        elif minus_prime_flag == True:
            prime_list.append(num_minus)
            prime_counter += 1
        elif plus_prime_flag == True:
            prime_list.append(num_plus)
            prime_counter += 1
        num += 6
    return prime_list[n-1]

import time
start = time.time()
print(nth_prime_6(10001))
end = time.time()
print(f"runtime: {end-start}")