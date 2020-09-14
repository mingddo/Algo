import sys
sys.stdin = open("input (3).txt", "r")

for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_cnt = 0
    start_num = 0
    d_x = [1,-1,0,0]
    d_y = [0,0,-1,1]
    for i in range(N):
        for j in range(N):
            q = []
            start = arr[i][j]
            cnt = 1
            num = arr[i][j]
            q.append((i, j))
            while q:
                x, y = q.pop(0)
                for d in range(4):
                    nx = x + d_x[d]
                    ny = y + d_y[d]
                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == arr[x][y] + 1:
                        q.append((nx, ny))
                        num += 1
                        cnt += 1

            if max_cnt < cnt:
                max_cnt = cnt
                start_num = start
            elif max_cnt == cnt:
                if start_num > start:
                    start_num = start

    print('#{} {} {}'.format(test_case,start_num,max_cnt))