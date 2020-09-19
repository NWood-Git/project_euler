# Largest prime factor 
# Problem 3
# https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def largest_prime_factor(target):
    prime_list  = []
    for i in range(2, int(target**.5)+1):
        if not prime_list and target % i == 0:
            prime_list.append(i)
        else:
            prime_status = None
            for x in prime_list:
                if i % x == 0:
                    prime_status = False
                    break
            if prime_status is not False and target % i == 0:
                prime_list.append(i)
    return prime_list[-1]

# print(largest_prime_factor(13195))
# print(largest_prime_factor(600851475143)) # Answer = 6857

import time
start = time.time()
print(largest_prime_factor(600851475143))
end = time.time()
print(end-start)

# More Optimized Solutions

# with prime list
def largest_prime_factor_opt_with_list(target):
    prime_list = []
    if target % 2 == 0:
        prime_list.append(2)
        while target % 2 == 0 and target != 2:
            target /= 2
    factor = 3
    while target > factor:
        if target % factor == 0:
            prime_list.append(factor)
            while target % factor == 0 and target != factor:
                target /= factor
        factor += 2
    prime_list.append(int(target))
    return (prime_list, target)

# print(largest_prime_factor_opt_with_list(600851475143))

# p without prime list
def largest_prime_factor_opt_without_list(target):
    if target % 2 == 0:
        while target % 2 == 0 and target != 2:
            target /= 2
    factor = 3
    while target > factor:
        if target % factor == 0:
            while target % factor == 0 and target != factor:
                target /= factor
        factor += 2
    return target


import time
start = time.time()
print(largest_prime_factor_opt_without_list(600851475143))
end = time.time()
print(end-start)

'''
def prime_nums_less_than(num):
    prime_set = set()
    for i in range(num):
        if i >= 2:
            if prime_set == set():
                prime_set.add(i)
            else:
                prime_status = None
                for x in prime_set:
                    if i % x == 0:
                        prime_status = False
                        break
                if prime_status is not False:
                    prime_set.add(i)
    return prime_set
'''