import math
def problem3():
    """
    Project Euler Problem 3
    https://projecteuler.net/problem=3

    The problem:

    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """
    def is_prime(i):
        """
        checks if i is a prime number or not
        """
        if i == 2 or i == 3:
            return True
        for j in range(2, int(math.sqrt(i) + 1)):
            if i%j == 0:
                return False
        return True

    num = 600851475144
    prime_factor_list = []

    for i in range(2,num):
        if num%i == 0 and is_prime(i):
            prime_factor_list.append(i)

    highest_prime_factor = max(prime_factor_list)

    print("The highest prime factor of 600851475144 is {factor}.".format(factor = highest_prime_factor))