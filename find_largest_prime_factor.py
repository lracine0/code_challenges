# PROJECT EULER QUESTION #3

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def find_largest_prime_factor(number):
    """finds the largest prime factor of any number"""

    largest_prime_factor = 0
    new_num = number

    for factor in range(2, 40000):

        while (new_num % factor == 0) and (new_num != factor):
            new_num = new_num / factor 
            

    print(new_num)



find_largest_prime_factor(600851475143)