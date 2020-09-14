import sys

sys.stdin = open("input.txt", "r")
def bfs(s_x,s_y):
    global result
    visited = []
    q = []
    visited.append((s_x, s_y))
    q.append((s_x, s_y))
    while q:
        x, y = q.pop(0)
        # if path[x][y] == 3:
        #     result = 1
        #     break
        for d in range(4):
            n_x = x + d_x[d]
            n_y = y + d_y[d]
            if 0 <= n_x < 16 and 0 <= n_y < 16 and path[n_x][n_y] != 1 and (n_x,n_y) not in visited:
                if path[n_x][n_y] == 3:
                    return 1
                visited.append((n_x,n_y))
                q.append((n_x, n_y))

    return 0

for T in range(1, 11):
    tc = int(input())
    path = [list(map(int,input())) for _ in range(16)]
    # 출발점 찾기
    for a in range(16):
        for b in range(16):
            if path[a][b] == 2:
                start_x = a
                start_y = b
                break
    d_x = [0, 0, -1, 1]
    d_y = [-1, 1, 0, 0]
    # BFS로 탐색
    result = bfs(start_x,start_y)
    print('#{} {}'.format(tc,result))