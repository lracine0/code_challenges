#PROJECT EULER QUESTION #4


#A palindromic number reads the same both ways. The largest palindrome made from 
#the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def find_largest_palindrome():

    upper_limit = 993
    index = 1
    j = 0

    while j < 100:

        while (upper_limit - index) > 100:

            for index in range(1, upper_limit - j):
                largest_palindrome = (upper_limit - j) * (upper_limit - index)

                compare_nums = str(largest_palindrome)

                if is_palindrome(compare_nums):
                    print(largest_palindrome , j)
            j += 1

    print("nope, not working")


def is_palindrome(nums):
    """Gets sent an array of numbers, checks if reflective"""


    end = len(nums) - 1
    for i in range(0, len(nums)):
        if nums[i] != nums[end - i]:
            return False
        elif i > (end - i):
            return True

    return False


find_largest_palindrome()



