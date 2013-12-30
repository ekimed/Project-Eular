#largest palindrome produce from two 3-digit numbers

import sys
import time

min = 100
max = 999

def palindrome(product):
    palindrome = False
    str_product = str(product)
    if str_product[0:]==str_product[::-1]:
        palindrome = True
        return palindrome
    else:
        return palindrome

def get_factors():
    max_product = 0
    for a in range (min, max+1):
        for b in range(a+1, max+1):
            prod = a*b
            check = palindrome(prod)
            if check == True and prod>max_product:
                max_product = prod
    print max_product

start_time = time.time()
get_factors()
end_time = time.time()
time_difference=end_time-start_time
print time_difference
    