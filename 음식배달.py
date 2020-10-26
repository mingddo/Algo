#import sys

#sys.stdin = open("input.txt", "r")

def bfs(b):
    visited = [[0]*N for _ in range(N)]
    total = 0
    while b:
        r, c, p = b.pop(0)
        for x, y in delta:
            nr = x + r
            nc = y + c
            if 0 <= nr < N and 0 <= nc < N and d_mapp[nr][nc] < 2 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                b.append([nr,nc,d_mapp[nr][nc])
                if d_map[nr][nc] == 1:




while start:
    x, y = start.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<= nx < N and 0<= ny < M and arr[nx][ny] == 0 and visited[nx][ny] == 0:
            start.append((nx,ny))
            arr[nx][ny] = 1
            visited[nx][ny] = visited[x][y] + 1



for test_case in range(1, int(input()) + 1):
    N = int(input())
    d_map = [list(map(int, input().split())) for _ in range(N)]

    # 음식점 후보 (2 이상인 곳을 찾아서 저장해[r,c,운용 비용]
    store = []
    home = []
    for s in range(N):
        for t in range(N):
            if d_map[s][t] >= 2:
                store.append([s,t,d_map[s][t]])
            elif d_map[s][t] == 1:
                home.append([s,t])

    # 비트연산자로 순열 만들기
    powerset = []
    sn = lem(store)
    for k in range(1<<sn):
        sub = []
        for l in range(sn):
            if k & (1<<l):
                sub.append(store[l])
        powerset.append(sub)
    r_p = reversed(powerset)
    delta = [(-1,-1), (-1,0), (1,-1), (0,-1), (0,1), (1,1), (1,0), (1,-1)]
    min = 987654321
    for a in r_p:
        if a != []:
            bfs(a)