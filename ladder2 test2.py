import sys
sys.stdin = open("input (1).txt", "r")

def dfs(x, y, cnt):
    while y>0:
        if arr[y][x-1]:
            while arr[y][x-1]:
                x -= 1
                cnt += 1
            y -= 1
            cnt += 1
        elif arr[y][x+1]:
            while arr[y][x+1]:
                x += 1
                cnt += 1
            y -= 1
            cnt += 1
        else:
            y -= 1
            cnt += 1
    return (x, cnt)

for T in range(10):
    tc = int(input())
    arr = [list(map(int, input().split()))]
    start = []
    for i in range(100):
        if arr[0][i]:
            start.append(i)
    result = []
    for s in start:
        result.append(dfs(0,s,0))

    r = sorted(result, key=lambda p: (p[0], -p[1]))
    print('#{} {}'.format(tc, r[0][1]))
