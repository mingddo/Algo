import sys

#90도 회전하는 함수:
def turn (l):
    result = []
    for i in range(N):
        row = []
        for j in range(N-1, -1, -1):
            row.append(str(l[j][i]))
        result.append(row)
    return result

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    original = [list(map(int,input().split())) for _ in range(N)]
    one = turn(original) #90도 회전한 것
    two = turn (one)    #180도 회전
    three = turn(two)    #270도 회전
    print('#{}'.format(test_case))
    for idx in range(N):
        a = ''.join(one[idx])
        b = ''.join(two[idx])
        c = ''.join(three[idx])
        print(f'{a} {b} {c}')
