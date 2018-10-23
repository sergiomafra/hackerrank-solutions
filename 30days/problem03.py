#!/bin/python3

weird = "Weird"
not_weird = "Not Weird"

def weirdo(N):
    if N % 2 != 0:
        print(weird)
    else:
        if 2 <= N < 5 or N > 20:
            print(not_weird)
        elif 6 <= N <= 20:
            print(weird)

if __name__ == '__main__':
    N = int(input())
    weirdo(N)
