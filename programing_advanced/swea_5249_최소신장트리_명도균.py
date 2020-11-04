import sys

#sys.stdin = open("input.txt", "r")


# for test_case in range(1, int(input()) + 1):
#     V, E = map(int,input().split())
#     m = set()
#     dst = []
#     for _ in range(E):
#         a, b, c = map(int, input().split())
#         dst.append((a, b, c))
#     dst = sorted(dst, key = lambda x : x[2])
#     total = dst[0][2]
#     m.add(dst[0][0])
#     m.add(dst[0][1])
#     for t in dst:
#         if len(m) == V+1:
#             break
#         if t[0] not in m and t[1] in m:
#             m.add(t[0])
#             m.add(t[1])
#             total += t[2]
#         elif t[1] not in m and t[0]in m:
#             m.add(t[0])
#             m.add(t[1])
#             total += t[2]
#     print('#{} {}'.format(test_case, total))

from collections import  deque
def d(k):
    temp = cost[k][:]
    curent = 0
    q = deque([k])
    visited.add(k)
    while q:
        k = q.popleft()
        m_cost = 987654321
        m_idx = 0
        for c in range(V+1):
            if c not in visited:
                temp[c] = min(curent + cost[k][c], temp[c])
                if m_cost > temp[c]:
                    m_cost = temp[c]
                    m_idx = c
        q.append(m_idx)
        visited.add(m_idx)
        curent += cost[k][m_idx]
    return curent





for test_case in range(1, int(input()) + 1):
    V, E = map(int,input().split())
    cost = [[987654321]*(V+1) for _ in range(V+1)]
    visited = set()
    for _ in range(E):
        a, b, c = map(int, input().split())
        cost[a][b] = c
        cost[b][a] = c
    res = d(0)
    print(res)

