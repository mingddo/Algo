import sys
sys.setrecursionlimit(10000)
# sys.stdin = open("input(1).txt", "r")

def dfs(a, cnt):
    global result
    if cnt > result:
        return
    if a == K and cnt < result:
        result = cnt
        return

    for i in range(3):
        if i != 0:
            n_a = a + dx[i]
            if n_a < 100000:
                cnt += 1
                dfs(n_a, cnt)
        if i == 1:
            n_a = a * dx[i]
            if n_a < 100000:
                cnt += 1
                dfs(n_a, cnt)


N, K = map(int,input().split())
dx = [1, 2, -1]
result = 987654321
dfs(N,0)
print(result)
