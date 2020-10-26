
M, N = map(int,input().split())
s_cnt = int(input())
directions = [0, [0,0,0,1,2],[0,0,0,2,3],[0,1,2,0,0],[0,2,3,0,0]]
shops = [list(map(int,input().split())) for _ in range(s_cnt)]
dong = list(map(int,input().split()))
min_dt = 0
for s in shops:
    # 같은 방향에 있을 때
    if s[0] == dong[0]:
        min_dt += abs(s[1]-dong[1])
    # 인접 방향에 있을 때 (1일 때)
    elif directions[dong[0]][s[0]] == 1:
        min_dt += dong[1] + s[1]
    elif directions[dong[0]][s[0]] == 3:
        if dong[0] == 4:
            min_dt += (N-dong[1]) + (M-s[1])
        else:
            min_dt += (M - dong[1]) + (N - s[1])
    elif directions[dong[0]][s[0]] == 2:
        if dong[0] == 1:
            min_dt += (M-dong[1]) + s[1]
        elif dong[0] == 4:
            min_dt += dong[1] + (M-s[1])
        elif dong[0] == 2:
            min_dt += dong[1] + (N - s[1])
        else:
            min_dt += (N-dong[1]) + s[1]

            # 마주보는 방향에 있을 때 (0일 때)
    else:
        if dong[0] == 3 or dong[0]==4:
            if (M + dong[1] + s[1]) > (M+N):
                min_dt += (M+N)*2 - (M + dong[1] + s[1])
            else:
                min_dt += (M + dong[1] + s[1])
        else:
            if (N + dong[1] + s[1]) > (M+N):
                min_dt += (M+N)*2 - (N + dong[1] + s[1])
            else:
                min_dt += (N + dong[1] + s[1])

print(min_dt)