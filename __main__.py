"""
The main file for my Project Euler code.
"""
from problems_1_through_5 import *


problem_dict = {1 : problem1, 2 : problem2, 3 : problem3, 4 : problem4, 5 : problem5}

problem_int = int(input("Which problem do you want to solve? \n"))

problem_dict[problem_int]()