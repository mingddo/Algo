# import sys
# sys.stdin = open("input.txt", "r")

# print(str(int((0.5*2)%1)))

for test_case in range(1, int(input()) + 1):
    t = float(input())
    result = ''
    while t != 0:
        if len(result) >= 13:
            break
        result += str(int((t*2)//1))
        t = (t*2) % 1
    if len(result) >= 13:
        print('#{} {}'.format(test_case, 'overflow'))
    else:
        print('#{} {}'.format(test_case, result))
