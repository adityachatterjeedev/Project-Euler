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
    print("    The sum is {sum}." .format(sum = sum))


