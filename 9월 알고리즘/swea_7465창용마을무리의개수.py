import sys

#sys.stdin = open("input.txt", "r")
def bfs(v):
    visited[v] = 1
    q.append(v)
    while q:
        a = q.pop(0)
        for j in arr[a]:
            if not visited[j] :
                visited[j] = 1
                q.append(j)

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [[] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    visited = [0] * (N+1)
    q = []
    cnt = 0
    for n in range(1,N+1):
        if not visited[n]:
            cnt += 1
            bfs(n)
    print("#{} {}".format(test_case,cnt))