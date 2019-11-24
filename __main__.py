"""
The main file for my Project Euler code.
"""
from problems_1_through_10 import *
from problems_11_through_20 import *
from problems_21_through_30 import *
problem_dict = {1 : problem1, 2 : problem2, 3 : problem3, 4 : problem4, 5 : problem5, 
                6 : problem6, 7: problem7, 8: problem8, 9 : problem9, 10 : problem10,
                11: problem11, 12: problem12, 13: problem13, 14: problem14, 15: problem15,
                16: problem16, 17: problem17, 18: problem18, 19: problem19, 20: problem20,
                21: problem21, 22: problem22}

def solve_problems():
    """
    The main function.
    """
    character = 'y'
    while character == 'y' or character == 'Y':    
        try:
            problem_int = int(input("\nWhich problem do you want to solve? "))

            if problem_int > 0:
                try:
                    problem_dict[problem_int]()
                except KeyError:
                    print("\nI haven't implemented a solution to this problem yet, sorry. \
    Try pulling from this repository a few days later and maybe I'll have solved the problem by then. \nThanks for your patience.")
            else:
                print("\nThe problem number needs to be a positive integer!")
        except ValueError:
            print('\nThe problem number needs to be a positive integer!')
        character = input("\nDo you want to solve another problem? (y/n) ")


if __name__ == '__main__':
    solve_problems()