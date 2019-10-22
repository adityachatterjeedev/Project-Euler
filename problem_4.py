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
            
    
