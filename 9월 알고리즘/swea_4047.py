import sys

#sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input()) + 1):
    result = 0
    num = ''
    card = input()
    for i in range(len(card)//3):
        c = card[3*i: 3*i+3]
        if c in num:
            result = -1
            print('#{} ERROR'.format(test_case))
            break
        else:
            num += c

    if result != -1:
        S = 13 - num.count('S')
        D = 13 - num.count('D')
        H = 13 - num.count('H')
        C = 13 - num.count('C')
        print('#{} {} {} {} {}'.format(test_case, S, D, H, C))
