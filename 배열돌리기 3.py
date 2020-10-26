# import sys
# sys.stdin.readline()

def hor(list):
    n = len(list)
    result = [[] for _ in range(n)]
    for i in range(n):
        result[n-i-1] = list[i]
    return result

def ver(list):
    result = []
    for l in list:
        result.append(l[::-1])
    return result

def rotate(list):
    result = []
    m = len(list[0])
    n = len(list)
    for i in range(m):
        sub = []
        for j in range(n):
            sub.append(list[j][i])
        result.append(sub[::-1])
    return  result

def r_rotate(list):
    m = len(list[0])
    n = len(list)
    result = []
    for i in range(m-1,-1,-1):
        sub = []
        for j in range(n):
            sub.append(list[j][i])
        result.append(sub)
    return result

def right(list):
    m = len(list[0])
    n = len(list)
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    result = []
    for i in range(n//2):
        p1.append(list[i][:m//2])
        p2.append(list[i][m//2:])
    for j in range(n//2,n):
        p4.append(list[j][:m // 2])
        p3.append(list[j][m // 2:])
    for x in range(n//2):
        result.append(p4[x] + p1[x])
    for y in range(n // 2):
        result.append(p3[y] + p2[y])
    return  result


def left(list):
    m = len(list[0])
    n = len(list)
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    result = []
    for i in range(n//2):
        p1.append(list[i][:m//2])
        p2.append(list[i][m//2:])
    for j in range(n//2,n):
        p4.append(list[j][:m // 2])
        p3.append(list[j][m // 2:])
    for x in range(n//2):
        result.append(p2[x] + p3[x])
    for y in range(n // 2):
        result.append(p1[y] + p4[y])
    return result

N, M, R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
r = list(map(int, input().split())) # 몇 번 연산을 할 지

for k in r:
    if k == 1:
        arr = hor(arr)
    elif k ==2:
        arr = ver(arr)
    elif k == 3:
        arr = rotate(arr)
    elif k == 4:
        arr = r_rotate(arr)
    elif k == 5:
        arr = right(arr)
    else:
        arr = left(arr)

for ar in arr:
    for a in ar:
        print(a,end=' ')
    print()


