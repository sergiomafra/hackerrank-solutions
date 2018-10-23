#!/bin/python3

if __name__ == '__main__':
    n = int(input())

    binary = bin(n)[2:]

    counter = 0
    max_value = 0

    for b in binary:
        if b is '1':
            counter += 1
            if counter > max_value:
                max_value = counter
        else:
            counter = 0

    print(str(max_value))
