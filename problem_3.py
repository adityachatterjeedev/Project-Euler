import math
def problem3():
    """
    Project Euler Problem 3
    https://projecteuler.net/problem=3

    The problem:

    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """
    def is_prime(i: int):
        """
        Returns True if i is a prime number else False.
        """
        if i == 2 or i == 3:
            return True
        for j in range(2, int(math.sqrt(i) + 1)):
            if i%j == 0:
                return False
        return True

    num = 600851475143
    prime_factor_list = []

    while (num > 1):
        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i):
                if i not in prime_factor_list:
                    prime_factor_list.append(i)
                num = num // i
                break
        


    highest_prime_factor = max(prime_factor_list)

    print(problem3.__doc__)
    print("    Answer: The highest prime factor of 600851475143 is {factor}.".format(factor = highest_prime_factor))
