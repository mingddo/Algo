import sys

sys.stdin = open("input (3).txt", "r")
def bfs(d):
    visited = [0]* (V+1)
    q = []
    q.append(d)
    visited[d] = 1
    while q:
        v = q.pop(0)
        for w in path[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                q.append(w)
                if w == G:
                    return visited[w] -1
    return 0

for tc in range(1, int(input()) + 1):
    V, E = map(int,input().split())
    path = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        path[a].append(b)
        path[b].append(a)

    S, G = map(int,input().split())
    result = bfs(S)
    print('#{} {}'.format(tc,result))