# Largest Palindrome Product
# Problem 4
# https://projecteuler.net/problem=4

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
    num = str(num)
    split_point = len(num) // 2
    if len(num) % 2 == 0:
        first_half = num[:split_point]
        rev_second_half = num[split_point:][::-1]
    else:
        first_half = num[:split_point]
        rev_second_half = num[split_point+1:][::-1]
    return first_half == rev_second_half

# print(is_palindrome(9009))
# print(is_palindrome(90509))

def palindrome_product_in_range(num1, num2):
    palindrom_products = []
    lon = []
    for i in range(num1, num2+1):
        lon.insert(0,i)
    lon_copy = lon.copy()
    for i in lon:
        for x in lon_copy:
            product = i * x
            if is_palindrome(product) is True:
                palindrom_products.append(product)
        lon_copy.pop(0)
    return max(palindrom_products)

print(palindrome_product_in_range(10,99))
print(palindrome_product_in_range(100,999))

# Congratulations, the answer you gave to problem 4 is correct.
# You are the 485880th person to have solved this problem.
# This problem had a difficulty rating of 5%. The highest difficulty rating you 
# have solved remains at 5%.
## Answer = 96609