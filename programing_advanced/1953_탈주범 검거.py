import sys

sys.stdin = open("탈주범.txt", "r")
from collections import deque
def BFS(r,c):
    cnt = 1
    visited[r][c] = 1
    q =deque([(r,c,1)])
    while q:
        x, y, t = q.popleft()
        if t == L:
            break
        ty = tunnel[x][y]
        for d in delta[ty]:
            nx = x + d[0]
            ny = y + d[1]
            dr = d[2]
            if 0 <= nx <N and 0 <= ny <M and tunnel[nx][ny] in direction[dr] and not visited[nx][ny]:
                # if t == 6:
                #     visited[nx][ny] = 1
                #     cnt += 1
                # else:
                q.append((nx, ny, t+1))
                visited[nx][ny] = 1
                cnt += 1

    return cnt


for test_case in range(1, int(input()) + 1):
    N, M, R, C, L = map(int,input().split())
    tunnel = [list(map(int,input().split())) for _ in range(N)]
    delta = {1: [(-1, 0, 1), (1, 0, 2), (0, -1, 3), (0, 1, 4)],
             2: [(-1, 0, 1), (1, 0, 2)],
             3: [(0, -1, 3), (0, 1, 4)],
             4: [(-1, 0, 1), (0, 1, 4)],
             5: [(1, 0, 2), (0, 1, 4)],
             6: [(1, 0, 2), (0, -1, 3)],
             7: [(-1, 0, 1), (0, -1, 3)]}
    direction = {1: {1, 2, 5, 6},
                 2: {1, 2, 4, 7},
                 3: {1, 3, 4, 5},
                 4: {1, 3, 6, 7}}
    # up = {1, 2, 5, 6}
    # down = {1, 2, 4, 7}
    # left = {1, 3, 4, 5}
    # right = {1, 3, 6, 7}
    visited = [[0]*M for _ in range(N)]
    res = BFS(R,C)
    print('#{} {}'.format(test_case,res))
