import sys
sys.stdin = open("input4.txt", "r")
from collections import deque

def BFS():
    q = deque([(0,0)])
    time[0][0] = 0
    while q:
        x, y = q.popleft()
        for d in delta:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < N and 0 <= ny < N:
                if time[nx][ny] > time[x][y] + arr[nx][ny]:
                    time[nx][ny] = time[x][y] + arr[nx][ny]
                    q.append((nx,ny))


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    time = [[987654321]*N for _ in range(N)]
    delta = [(-1,0), (1, 0), (0, -1), (0, 1)]
    BFS()
    print('#{} {}'.format(test_case, time[N-1][N-1]))