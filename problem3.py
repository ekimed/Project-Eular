#What is the largest prime factor of the number 600851475143
import sys
import math


def check_prime(n):
    limit = math.sqrt(n)
    i = 3
    
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True

    

def get_factors(number): #gets the prime factors
    i = 2
    while i <= number: 
        if number % i == 0:
            number = number / i 
        elif check_prime(number)==True:
            print number
            break
        else:
            i += 1

get_factors(600851475143)
            

