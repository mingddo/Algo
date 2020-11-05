import sys
#sys.stdin = open("input.txt", "r")
from collections import deque
def min_cost(s):
    key = [[987654321]*N for _ in range(N)]
    key[s[0]][s[1]] = 0
    q = deque([s])
    while q:
        a, b = q.popleft()
        if a == end and b == end:
            continue
        for d in delta:
            na = a + d[0]
            nb = b + d[1]
            if 0 <= na < N and 0 <= nb < N:
                if arr[a][b] < arr[na][nb]:
                    f = key[a][b] + 1 +(arr[na][nb]-arr[a][b])
                else:
                    f = key[a][b] + 1
                if key[na][nb] > f:
                    q.append((na,nb))
                    key[na][nb] = f

    return key[N-1][N-1]




for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    start = (0,0)
    end = N-1
    delta = [(-1,0), (1,0), (0,-1), (0,1)]
    print('#{} {}'.format(test_case,min_cost(start)))

