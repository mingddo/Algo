def f(a,b,c,d):
    for i in range(a,c):
        for j in range(b,d):
            if arr[i][j] == 0:
                arr[i][j] = 1


arr = [[0]*101 for _ in range(101)]
for _ in range(4):
    x, y, z, r = map(int,input().split())
    f(x,y,z,r)

cnt = 0
for a in arr:
    cnt += a.count(1)

print(cnt)