#!/bin/python3

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    hash_mag = {}
    for word in magazine:
        if word in hash_mag:
            hash_mag[word] += 1
        else:
            hash_mag[word] = 1

    for word in note:
        if word in hash_mag:
            hash_mag[word] -= 1
            if hash_mag[word] == 0:
                del hash_mag[word]
        else:
            print('No')
            return

    print('Yes')

if __name__ == '__main__':
    # Unnecessary in Python
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    # Magazine words
    magazine = input().rstrip().split()

    # Note words
    note = input().rstrip().split()

    checkMagazine(magazine, note)
