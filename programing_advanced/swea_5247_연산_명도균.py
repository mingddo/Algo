from collections import deque
def bfs(n):
    q = deque()
    q.append(n)
    while q:
        k = q.popleft()
        if k == M:
            return
        for res in (k+1, k-1, k*2, k-10):
            if 0 < res <= 1000000 and not visited[res]:
                visited[res] = visited[k]+1
                q.append(res)

for test_case in range(1, int(input()) + 1):
    N, M = map(int,input().split())
    visited = [0]* 1000001
    bfs(N)
    print('#{} {}'.format(test_case, visited[M]))

