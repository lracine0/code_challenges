# PROJECT EULER QUESTION #3

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def find_largest_prime_factor(number):
    largest_prime_factor = 0

    for i in range(number):
        if (i % 2 != 0) and (i % 3 != 0) and (i % 4 != 0) and (i % 5 != 0) 
        and (i % 6 != 0) and (i % 7 != 0) and (i % 8 != 0) and (i % 9 != 0):

        largest_prime_factor = i

    print(largest_prime_factor)






find_largest_prime_factor(600851475143)