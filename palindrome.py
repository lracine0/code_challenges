#PROJECT EULER QUESTION #4


#A palindromic number reads the same both ways. The largest palindrome made from 
#the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def find_largest_palindrome():

    for index in range(1, 999):
        largest_palindrome = 999 * (999 - index)
        compare_nums = list(largest_palindrome)

