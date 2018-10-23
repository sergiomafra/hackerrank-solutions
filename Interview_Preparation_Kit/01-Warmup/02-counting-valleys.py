#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    nv = 0 # Number of Valleys
    altitude = 0
    valley = False

    for step in s:
        if step == 'D':
            altitude += -1
        elif step == 'U':
            altitude += 1

        if altitude < 0:
            valley = True
        else:
            if valley == True:
                valley = False
                nv += 1

    return nv

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
