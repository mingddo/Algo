import sys

sys.stdin = open("input.txt", "r")
def dfs(x,y):
    global result
    global arr
    arr[x][y] = 1
    for d in range(4):
        new_x = x + d_x[d]
        new_y = y + d_y[d]
        if 0<new_x<16 and 0<new_y<16 and arr[new_x][new_y] != 1:
            if arr[new_x][new_y] == 3:
                result = 1
                return
            dfs(new_x,new_y)



for T in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    d_x = [0, 1, 0, -1]
    d_y = [1, 0, -1, 0]
    for a in arr:
        for b in range(16):
            if a[b] == 2:
                start_x = arr.index(a)
                start_y = b
    result = 0
    dfs(start_x,start_y)
    print('#{} {}'.format(tc, result))
