"""
The main file for my Project Euler code.
"""
from problems_1_through_8 import *


problem_dict = {1 : problem1, 2 : problem2, 3 : problem3, 4 : problem4, 5 : problem5, 
                6 : problem6, 7: problem7, 8: problem8}

problem_int = int(input("Which problem do you want to solve? "))

problem_dict[problem_int]()