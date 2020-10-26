def f(a,b):
    for i in range(b,b+10):
        for j in range(a, a+10):
            if arr[i][j] == 0:
                arr[i][j] = 1


N = int(input())
arr = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    f(x,y)

cnt = 0
for a in arr:
    cnt += a.count(1)

print(cnt)