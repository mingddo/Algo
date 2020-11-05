import sys
#sys.stdin = open("input.txt", "r")
def bfs(n):
    global cnt
    visited[n] = 1
    q = [n]
    while q:
        k = q.pop(0)
        for j in node[k]:
            if not visited[j]:
                visited[j] = 1
                q.append(j)




for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    temp = list(map(int,input().split()))
    node = [[] for _ in range(N+1)]
    for i in range(M):
        a = temp[2*i]
        b = temp[(2*i)+1]
        node[a].append(b)
        node[b].append(a)
    visited = [0]*(N+1)
    cnt = 0
    # bfs(temp[0])
    for idx in range(1, len(visited)):
        if not visited[idx]:
            bfs(idx)
            cnt += 1
    print('#{} {}'.format(test_case, cnt))



