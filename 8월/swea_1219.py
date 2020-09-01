import sys
sys.stdin = open("input (1).txt", "r")

def dfs(v):
    global result
    visited[v] = 1
    for r in route:
        if r[v] != 0 and visited[r[v]] == 0:
            if r[v] == 99:
                result = 1
            dfs(r[v])
for T in range(10):
    tc, n = map(int, input().split())
    arr = list(map(int, input().split()))
    route = [[0] * 100 for _ in range(2)]
    result = 0
    visited = [0] * 100
    for i in range(n):
        st, end = arr[2 * i], arr[2 * i + 1]
        if route[0][st]:
            route[1][st] = end
        else:
            route[0][st] = end
    dfs(0)

    print('#{} {}'.format(tc, result))
