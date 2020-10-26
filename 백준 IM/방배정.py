


N, K = map(int,input().split())
info = [[0,0] for _ in range(7)]
for _ in range(N):
    a, b = map(int,input().split())
    info[b][a] += 1

cnt = 0
for i in range(1,7):
    for j in range(2):
        if info[i][j] != 0:
            cnt += (info[i][j] // K)
            if info[i][j] % K:
                cnt += 1

print(cnt)
