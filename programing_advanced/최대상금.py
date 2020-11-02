import sys
sys.stdin = open("input1.txt", "r")

def money(cnt):
    global result
    if cnt == 0:
        res = int(''.join(number))
        if result < res:
            result = res
        return
    for i in range(n):
        for j in range(i+1, n):
            number[i], number[j] = number[j], number[i]
            a = ''.join(number)
            if (a,cnt - 1) not in visited:
                visited.append((a,cnt - 1))
                money(cnt-1)
            number[i], number[j] = number[j], number[i]


for test_case in range(1, int(input()) + 1):
    q = list(input().split())
    count = int(q[1])
    number = list(q[0])
    result = 0
    n = len(number)
    visited = []
    money(count)
    print('#{} {}'.format(test_case, result))