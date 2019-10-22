"""
The main file for my Project Euler code.
"""
from problem_1 import *
from problem_2 import *
from problem_3 import *
from problem_4 import *

problem_dict = {1 : problem1, 2 : problem2, 3 : problem3, 4 : problem4}

problem_int = int(input("Which problem do you want to solve? \n"))

problem_dict[problem_int]()