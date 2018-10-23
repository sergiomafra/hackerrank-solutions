number_of_test_cases = int( input() )

for n in range(1, number_of_test_cases + 1):
    s = input()
    print('{} {}'.format( s[0::2], s[1::2] ))
