#PROJECT EULER QUESTION #5


#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def find_smallest_num(range_of_nums):
    """range defines the numbers it should be divisible by"""
    
    for num in range(230000000, 240000000):
        
        for i in range(1,(range_of_nums + 1)):
            if num % i == 0:

                if i == (range_of_nums):
                    print(num)
                    return

                else:
                    continue
            
            else:
                break

        



find_smallest_num(20)