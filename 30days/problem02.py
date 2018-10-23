#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    final_meal_cost = str(round( meal_cost * (1 + float(tip_percent + tax_percent)/100) ))
    print("The total meal cost is " + final_meal_cost + " dollars.")

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
