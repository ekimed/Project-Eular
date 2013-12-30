#project eular problem 6
#Sum Square Difference
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

def difference (x,y):
    sum_of_square = 0
    sum = 0
    for number in range(x, y+1):
        sum_of_square = number**2 + sum_of_square
        sum = sum + number
    print sum**2 - sum_of_square

difference(1,100)



