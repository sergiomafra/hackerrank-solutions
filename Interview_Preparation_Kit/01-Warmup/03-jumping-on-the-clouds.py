#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n, c):
    jcounter = 0 # Jumps counter

    i = 0
    while i < n:
        if c[i] == 1:
            i += 1
            pass
        else:
            if i+2 < n:
                if c[i+2] == 0:
                    i += 2
                    jcounter += 1
                elif i+1 < n:
                    if c[i+1] == 0:
                        i += 1
                        jcounter += 1
            elif i+1 < n:
                if c[i+1] == 0:
                    i += 1
                    jcounter += 1
            else:
                break

    return jcounter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
