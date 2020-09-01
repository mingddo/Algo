import sys
sys.stdin = open("input(1).txt.", "r")
# 오셀로 색깔 바꾸기
def othello(a, b, c):
    global board
    # 저장된 di 리스트 돌면서 같은 돌 나올 때 까지 뒤집기.
    for d in di:
        dx = a - 1 + d_x[d]
        dy = b - 1 + d_y[d]
        while True:
            if board[dx][dy] == co[c-1]:
                break
            board[dx][dy] = co[c-1]
            dx += d_x[d]
            dy += d_y[d]


# 방향탐색해 8개 방향 중 바꿀 수 있는 돌 탐색해서 di에 해당 방향 저장.
def search (a, b, c):
    for d in range(8):
        dx = a - 1 +d_x[d]
        dy = b - 1 + d_y[d]
        if 0 <= dx < N and 0 <= dy < N and board[dx][dy] == co[c % 2]:
            while 0 <= dx < N and 0 <= dy < N :
                if board[dx][dy] == co[c-1]:
                    di.append(d)
                    break
                elif board[dx][dy] == 0:
                    break
                dx += d_x[d]
                dy += d_y[d]

for tc in range(1, int(input())+1):
    co = [1, 2]
    N , M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    board[N//2-1][N//2-1] = board[N//2][N//2] = 2
    board[N//2-1][N//2] = board[N//2][N//2-1] = 1
    d_x = [0, 0, -1, 1, -1, 1, -1, 1]
    d_y = [-1, 1, 0, 0, -1, -1, 1, 1]
    for _ in range(M):
        y, x, color = map(int, input().split())
        board[x - 1][y - 1] = co[color - 1]
        di = []
        search(x, y, color)
        othello(x, y, color)
        # for k in board:
        #     print(*k)
        # print()
    w = 0
    b = 0
    for bor in board:
        w += bor.count(2)
        b += bor.count(1)


    print('#{} {} {}'.format(tc, b, w))