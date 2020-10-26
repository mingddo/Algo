import time
start = time.time()

def f(li, color_num):
    for i in range(li[0],li[0]+li[2]):
        for j in range(li[1],li[1]+li[3]):
            if arr[i][j] == 0:
                arr[i][j] = color_num

N = int(input())
arr = [[0]*101 for _ in range(101)]
paper = [list(map(int, input().split())) for _ in range(N)]
paper = reversed(paper)
num = N
for p in paper:
    f(p,num)
    num -= 1

cnt = 0
for a in arr:
    cnt += a.count(1)
result = [0]*(N+1)
for a in arr:
    for x in range(1,N+1):
        result[x] += a.count(x)
for r in result[1:]:
    print(r)