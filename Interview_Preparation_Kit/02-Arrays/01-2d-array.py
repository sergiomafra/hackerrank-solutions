#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    alen = len(arr[1])
    hourglass_sum_list = []

    for j, line in enumerate(arr):
        if j+2 == alen:
            break
        for i, element in enumerate(line):
            if i+2 == alen:
                break
            else:
                hourglass_sum_list.append( \
                    arr[j][i] + arr[j][i+1] + arr[j][i+2] + arr[j+1][i+1] + \
                    arr[j+2][i] + arr[j+2][i+1] + arr[j+2][i+2] \
                )

    return max(hourglass_sum_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
