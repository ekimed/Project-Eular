import math


def check_prime(n):
    limit = math.sqrt(n)
    i = 3
    
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True

def main():
    prime = [2]
    num=3
    while len(prime)<10001:
        if check_prime(num)==True:
            prime.append(num)
        num+=2
    print prime[-1]

main()
  
        

            
    
        

