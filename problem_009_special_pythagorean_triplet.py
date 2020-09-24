# Special Pythagorean triplet
# Problem 9
# https://projecteuler.net/problem=9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Brute Force
def pythagorean_triple_sums_to(num):
    for a in range(1,num):
        for b in range(1, num):
            c = (a**2 + b**2)**.5
            if a + b + c == num: return a * b * c

print(pythagorean_triple_sums_to(1000))

# Congratulations, the answer you gave to problem 9 is correct.
# You are the 357087th person to have solved this problem.
# This problem had a difficulty rating of 5%.
# The highest difficulty rating you have solved remains at 5%.
# The answer is 31875000

# modified brute force
def modified_pythagorean_triple_sum(s):
    a_limit = int((s-3)/3)
    for a in range(1,a_limit):
        b_limit = int((s-a)/2)
        for b in range(1, b_limit):
            c = (a**2 + b**2)**.5
            if a + b + c == s: 
                # print(a,b,c)
                return a * b * c

print(modified_pythagorean_triple_sum(1000))
