# PROJECT EULER PROBLEM #6


# The sum of the squares of the first ten natural numbers is,

# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,

# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares of the first ten natural 
#numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first one hundred 
#natural numbers and the square of the sum.


def sum_of_squares():

    sum_of_squares = 0
    squared_sum = 0

    for i in range(101):
        square = i * i
        sum_of_squares += square 
        squared_sum += i

    difference = (squared_sum)**2 - sum_of_squares
    print(sum_of_squares, squared_sum, difference)



sum_of_squares()
