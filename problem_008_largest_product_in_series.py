# Largest product in a series
# Problem 8
# https://projecteuler.net/problem=8

# The four adjacent digits in the 1000-digit number that have 
# the greatest product are 9 × 9 × 8 × 9 = 5832.

big_num = int("""
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace("\n", ""))

# Find the thirteen adjacent digits in the 1000-digit number that have the 
# greatest product. What is the value of this product?

def largest_product_k_adjacent_digits(num, k):
    num = str(num)
    len_num = len(num)
    start = 0
    stop = k
    largest_product = 0
    while stop <= len_num:
        section = [int(i) for i in num[start:stop]]
        total = 1
        for i in section:
            total *= i
        if total > largest_product:
            largest_product = total
        start += 1
        stop += 1
    return largest_product

print (largest_product_k_adjacent_digits(big_num, 13))

# Congratulations, the answer you gave to problem 8 is correct.
# You are the 351584th person to have solved this problem.
# This problem had a difficulty rating of 5%. 
# The highest difficulty rating you have solved remains at 5%.
# Answer is 23514624000

# Recurisve Solution hits max recursion depth - works with shorter number does not work with the big number

def largest_product_k_adjacent_digits_recursive(num, k):
    num = str(num)
    start = 0
    stop = k
    largest_product = 0
    return _largest_product_k_adjacent_digits_recursive(num, start, stop, largest_product)

def _largest_product_k_adjacent_digits_recursive(num, start, stop, largest_product):
    if stop > len((num)):
        return largest_product
    section = [int(i) for i in num[start:stop]]
    total = 1
    for i in section:
        total *= i
    if total > largest_product:
        largest_product = total
    start += 1
    stop += 1
    return _largest_product_k_adjacent_digits_recursive(num, start, stop, largest_product)


# print (largest_product_k_adjacent_digits_recursive(big_num, 4)) #doesn't work need a shorter number then it works