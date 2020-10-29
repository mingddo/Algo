import sys


#sys.stdin = open("input.txt", "r")
def dfs(a,b,c):
    global result
    if c > result:
        return
    visited[a][b] = 1
    for d in delta:
        x, y = a+d[0], b+d[1]
        if x == N-1 and y == N-1:
            if result > c+num[N-1][N-1]:
                result = c+num[N-1][N-1]
        if 0<= x < N and 0<= y < N and visited[x][y] == 0:
            visited[x][y] = 1
            dfs(x,y,c+num[x][y])
            visited[x][y] = 0


for test_case in range(1, int(input()) + 1):
    N = int(input())
    num = [list(map(int,input().split())) for _ in range(N)]
    delta = [[1, 0], [0, 1]]
    result = 987654321
    visited = [[0]*N for _ in range(N)]
    dfs(0, 0, num[0][0])
    print('#{} {}'.format(test_case, result))