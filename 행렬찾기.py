import sys
# 가로 길이 찾기
def y_search (i,j):
    cnt = 1
    while j < n:
        j +=1
        if matrix[i][j]:
            cnt += 1
        else: 
            break
    return cnt

# 세로 길이 찾기
def x_search (i,j):
    cnt = 1
    while j < n:
        i +=1
        if matrix[i][j]:
            cnt += 1
        else:
            break
    return cnt
# 초기화하기
def reset (a, b, c, d):
    for rx in range(a, c):
        for ry in range(b, d):
            matrix[rx][ry] = 0
    return matrix

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    small = []
    for x in range(n):
        for y in range(n):
            if matrix[x][y]: 
                len_y = y_search(x,y)
                len_x = x_search(x,y)
                small.append([len_x, len_y, (len_x*len_y)])
                matrix = reset(x, y, (x+len_x), (y+len_y))
    small_s = sorted(small, key = lambda x: (x[2],x[0]))
    print("#{} {}".format(test_case, len(small_s)), end=' ')
    for s in small_s:
        print(f'{s[0]} {s[1]}', end=' ')
    print()


