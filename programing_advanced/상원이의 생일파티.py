import sys

#sys.stdin = open("input.txt", "r")
from collections import deque
def bfs(v):
    global cnt
    visited[v] = 1
    q = deque([v])
    while q:
        k = q.popleft()
        if visited[k] == 3:
            continue
        for idx in range(N+1):
            if f[k][idx] == True and not visited[idx]:
                visited[idx] = visited[k]+1
                if visited[idx] <= 3:
                    cnt += 1
                q.append(idx)


for test_case in range(1, int(input()) + 1):
    N, M = map(int,input().split())
    visited = [0] * (N+1)
    f = [[False]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        f[a][b] = True
        f[b][a] = True
    cnt = 0
    bfs(1)
    print('#{} {}'.format(test_case, cnt))