# set (중복되지 않는 값)
T = int(input())

for test_case in range(1, T + 1):
    numbers = [list(map(int, input().split()))for i in range(9)]
    arr = {range(1,10)}
    ver = {0} * 9
    hor = {0} * 9
    