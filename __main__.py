"""
The main file for my Project Euler code.
"""
from problems_1_through_10 import *
from problem_11 import *


problem_dict = {1 : problem1, 2 : problem2, 3 : problem3, 4 : problem4, 5 : problem5, 
                6 : problem6, 7: problem7, 8: problem8, 9 : problem9, 10 : problem10,
                11: problem11}

def solve_problems():
    """
    The main function.
    """
    character = 'y'
    while character == 'y' or character == 'Y':    
        problem_int = int(input("Which problem do you want to solve? "))

        problem_dict[problem_int]()

        character = input("\nDo you want to solve another problem? (y/n) ")


if __name__ == '__main__':
    solve_problems()