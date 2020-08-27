import sys

#sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N = int(input())
    start_num = 1
    d = 0
    r = 0
    c = 0
    d_x = [0, 1, 0, -1]
    d_y = [1, 0, -1, 0]
    arr = [[0] * N for _ in range(N)]
    while start_num <= N * N:
        arr[r][c] = start_num
        start_num += 1
        nr = r + d_x[d]
        nc = c + d_y[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r , c = nr, nc
        else:
            d = (d+1)%4
            r += d_x[d]
            c += d_y[d]
    print('#{}'.format(test_case))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()

