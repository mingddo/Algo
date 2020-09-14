import sys

sys.stdin = open("input (1).txt", "r")
def bfs(s):
    visited[s] = 1
    q.append(s)

    while q:
        v = q.pop(0)
        for w in path[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                q.append(w)
    return



for test_case in range(1, 11):
    L, Start = map(int, input().split())
    strings = list(map(int, input().split()))
    path = [[] for _ in range(101) ]
    for a in range(L//2):
        f , t = strings[2*a], strings[2*a+1]
        path[f].append(t)
    visited = [0] * 101
    q = []
    bfs(Start)
    max_visited = max(visited)
    if visited.count(max_visited) > 1:
        idx = 0
        for j in range(len(visited)):
            if visited[j] == max_visited and idx < j:
                idx = j
        print('#{} {}'.format(test_case, idx))
    else:
        print(('#{} {}').format(test_case,visited.index(max_visited)))