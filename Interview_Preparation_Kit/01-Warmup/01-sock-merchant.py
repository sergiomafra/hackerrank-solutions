#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks_dict = {}

    for element in ar:
        if element not in socks_dict:
            socks_dict[element] = 1
        else:
            socks_dict[element] += 1

    number_of_pairs = 0
    for key, value in socks_dict.items():
        number_of_pairs += int(value / 2)

    return number_of_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
