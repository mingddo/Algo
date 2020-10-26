
C, R = map(int,input().split())
K = int(input())
hall = [[0]*C for _ in range(R)]
if K > C*R:
    print(0)
else:
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    d = 0
    r = R-1
    c = 0
    num = 1
    while num <= R*C:
        hall[r][c] = num
        if num == K:
            break
        num += 1

        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr <R and 0<= nc < C and hall[nr][nc] == 0:
            r, c = nr, nc
        else:
            d = (d+1)%4
            r += dr[d]
            c += dc[d]
    print('{} {}'.format(c+1,R-r))

