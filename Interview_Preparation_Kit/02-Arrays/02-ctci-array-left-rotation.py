def answer(a):
    answer = ''
    for element in a:
        answer += str(element) + ' '

    return answer

# Complete the rotLeft function below.
def rotLeft(a, d):
    n = len(a)

    if n == d or d % n == 0:
        print( answer(a) )
    else:
        if d > n:
            d = d % n
        print( answer(a[d:] + a[:d]) )

rotLeft( [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58,
    26, 10, 86, 51], 10 )
