#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#Euclid's algorithm to find GCD
#Use GCD to find LCM

#find the great common divisor

import timeit

def gcd(a,b):
    while b != 0:
        temp = a%b
        a = b
        a, b = b, temp
    return a

#find least common multiple
def lcm(a,b):
    result = (a*b)/gcd(a,b)
    return result

#lcm is idempotent
#finds the lcm for range of numbers leading up to and including x
def main(x):
    y = x - 1
    start = lcm (x,y)
    for num in range((y-1),0,-1):
        next_=lcm(start, num)
        start = next_
    print start
    

start = timeit.timeit()
main(20)
stop = timeit.timeit()
print stop - start