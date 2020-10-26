w, h = map(int,input().split())
n = int(input())
arr = [[0]*101 for _ in range(101)]
num = 1
for _ in range(n):
    a, b = map(int,input().split())
    if a == 1:
        for i in range(1,h+1):
            for j in range(1,b+1):
                arr[i][j] = num
        num += 1
        for l in range(1, h+1):
            for k in range(b+1,w+1):
                arr[l][k] = num
        num += 1
    else:
        for x in range(1,b+1):
            for y in range(1,w+1):
                arr[x][y] = num
        num += 1

        for c in range(b+1,h+1):
            for d in range(1,w+1):
                arr[c][d] = num
        num += 1

for r in range(1,num):
