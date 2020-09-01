def dfs(v):
    #방문체크
    # v의 인접한 정점 중에서 방문 안한 정점을 재귀 호출
    visited[v] = 1
    print(v, end=' ')
    for w in range(1, W+1):
        if arr[v][w] == 1 and visited[w] == 0:
            dfs(w)



W, L = map(int,input().split())
arr = [[0] * (W+1) for _ in range(W+1))
visited = [0] * (W+1)

for l in range(L):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1


dfs(1)

