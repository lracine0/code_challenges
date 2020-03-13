"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8
    
    """
    #STEP 1: 
    
    full_list = []
    sorted_nums = sorted(nums)

    for num in range (1, max_num): #starting at 1, not 0
        full_list.append(num)

    index = 0
    for num in sorted_nums:
        if num == full_list[index]:
            index += 1
        elif num != full_list[index]:
            
            return(full_list[index])


 

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. NICELY DONE!\n")
