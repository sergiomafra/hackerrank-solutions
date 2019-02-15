#!/bin/python3

import os

# Function to Transform a String in a Dict
def todict(somestring):

    hash_word = {}
    for letter in somestring:
        if letter in hash_word:
            pass
        else:
            hash_word[letter] = 'Hello World!'

    return hash_word

# Function that returns YES if a dict has the same key as another dict
# and NO if it hasn't
def answer(dict1, dict2):
    for key,_ in dict1.items():
        if key in dict2:
            return 'YES'

    return 'NO'

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    # Transforming String into Dicts
    ds1 = todict(s1)
    ds2 = todict(s2)

    # Condition to send the smallest dict first,
    # so the code will look up for less keys in
    # the second dict and makes the script faster.
    # As Captain Marvel onde said: higher, further, FASTER!
    if len(s1) <= len(s2):
        ans = answer(ds1,ds2)
    else:
        ans = answer(ds2,ds1)

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
