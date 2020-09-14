import sys


sys.stdin = open("input (2).txt", "r")

def bfs(s_x,s_y):
    d_x = [0, 0, -1, 1]
    d_y = [-1, 1, 0, 0]
    visited[s_x][s_y] = 1
    q.append((s_x,s_y))
    while q:
        x,y = q.pop(0)
        for d in range(4):
            n_x = x + d_x[d]
            n_y = y + d_y[d]
            if 0 <= n_x < N and 0 <= n_y < N and path[n_x][n_y] != 1 and not visited[n_x][n_y]:
                visited[n_x][n_y] = visited[x][y] + 1
                q.append((n_x,n_y))
                if path[n_x][n_y] == 3:
                    return visited[n_x][n_y] -2

    return 0
for test_case in range(1, int(input()) + 1):
    N = int(input())
    path = [list(map(int,input())) for _ in range(N)]
    # 시작점 (x,y)찾기
    for i in range(N):
        for j in range(N):
            if path[i][j] == 2:
                start_x = i
                start_y = j
                break
    visited = [[0] * N for _ in range(N)]
    q = []
    result = bfs(start_x,start_y)
    print('#{} {}'.format(test_case, result))