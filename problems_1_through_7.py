"""
A module that holds all the functions that calculate the solutions to Project Euler problems 1 through 5.
"""
import math

#Problem 1
def problem1():
    """
    Project Euler Problem 1
    https://projecteuler.net/problem=1

    The problem:
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. \n
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    print(problem1.__doc__)
    sum = 0
    for i in range(1000):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    print("    Answer: The sum is {sum}." .format(sum = sum))

#Problem 2
def problem2():
    """
    Project Euler Problem 2
    https://projecteuler.net/problem=2

    The problem:

    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    print(problem2.__doc__)
    sum = 0
    f0 = 0
    f1 = 1
    fib = 1
    while (fib <= 4.0e6):
        if (fib % 2 == 0):
            sum += fib
        temp = f1 + fib #the next fibonacci number
        f0 = f1
        f1 = fib
        fib = temp
    print("    Answer: The sum is {sum}.".format(sum = sum))

#Problem 3
def problem3():
    """
    Project Euler Problem 3
    https://projecteuler.net/problem=3

    The problem:

    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """

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

#Problem 4
def problem4():
    """
    Project Euler Problem 4
    https://projecteuler.net/problem=4

    The problem: 

    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    def is_palindrome(string: str):
        """
        Returns True if num is a palindrome, else False
        """
        if len(string) == 0 or len(string) == 1:
            return True
        else:
            return is_palindrome(string[1:-1]) and (string[0] == string[-1])

    palindrome_list = []
    factors_list = []

    for i in range(999,100,-1):
        for j in range(999,100,-1):
            if (i % 11 == 0 or j % 11 == 0) and (i % 100 !=0 and j % 100 != 0):
                prod = i*j
                string = str(prod)
                if is_palindrome(string):
                    palindrome_list.append(prod)
                    factors_list.append((i,j))

    max_palindrome = palindrome_list[0]
    max_palindrome_index = 0
    for i in range(len(palindrome_list)):
        if palindrome_list[i] > max_palindrome:
            max_palindrome = palindrome_list[i]
            max_palindrome_index = i

    factors = factors_list[max_palindrome_index]
    factor1 = factors[0]
    factor2 = factors[1]

    print(problem4.__doc__)
    print("    Answer: The largest palindrome that is a product of two 3-digit numbers is {palindrome} which can be written as {palindrome} = {factor1} * {factor2}.".format(palindrome = max_palindrome, factor1 = factor1, factor2 = factor2))

#Problem 5
def problem5():
    """
    Project Euler Problem 5.
    https://projecteuler.net/problem=5

    The problem:

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    #These are the steps I took to optimise my program, as my initial implementation was woefully slow:
    #The problem itself tells us that 2520 is the smallest number that is divisible by the numbers 1 through 10
    #Thus it is a reasonable thing to assume that any number divisible by the numbers 1 through 20 must be a multiple of 2520
    #Furthermore, the first multiple of 2520 that is divisible by 11 is 2520 * 11 = 27720. However, this is not the 
    #answer we need since it isn't divisible by 13. Thus the number that we need must be a multiple of 27720 * 13 = 360360. 
    #Proceeding like this lets us solve this problem by hand, but if we had to do that then there would be no point in writing
    #a computer program. So, we let the program do the rest.
    #
    #Furthermore, a little more analysis of the problem shows that in order for the number to be divisible by all 
    #numbers between 1 - 20, it is sufficient to check if it is divisible by the numbers 11, 13, 14, 16, 17, 18, 19, and 20.
    #However since we're testing multiples of 360360, which is divisible by 1 to 11 and 13, we only need to check for
    #14, 16, 17 , 18, 19 and 20.
    flag = False
    num = 360360
    while not flag:
        num += 360360
        flag = (num % 14 == 0) and (num % 16 == 0) and (num % 17 == 0) and (num % 18 == 0) and (num % 19 == 0) and (num % 20 == 0)
        
    print(problem5.__doc__)
    print("    Answer: The smallest number divisible by all the numbers from 1 to 20 is {num}.".format(num = num))

#Problem 6
def problem6():
    """
    Project Euler Problem 6
    https://projecteuler.net/problem=6

    The problem:

    The sum of the squares of the first ten natural numbers is,
    1**2 + 2**2 + ... + 10**2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)**2 = 55**2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    sum_squares = 0

    for i in range(1, 101):
        sum_squares += i**2

    sum_of_numbers = (100 * 101)/2 # 1 + 2 + ... + n = n * (n+1)/2

    answer = int(sum_of_numbers**2 - sum_squares)

    print(problem6.__doc__)
    print("    Answer: The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is {answer}.".format(answer = answer))

#Problem 7
def problem7():
    """
    Project Euler Problem 7
    https://projecteuler.net/problem=7

    The problem:

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10001st prime number?

    """    
    #Since 13 is the 6th prime, 31 is the 11th prime. This is where we start our calculations

    counter = 11
    num = 31

    while counter < 10001:
        num += 1
        if is_prime(num):
            counter += 1

    print(problem7.__doc__)
    print("    Answer: The 10001st prime number is {num}.".format(num = num))

#------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------- Helper functions ----------------------------------------------------------------
def is_prime(i: int):
        """
        Helper function for problem3() and problem7()
        Returns True if i is a prime number else False.
        """
        if i == 2 or i == 3:
            return True
        for j in range(2, int(math.sqrt(i) + 1)):
            if i%j == 0:
                return False
        return True