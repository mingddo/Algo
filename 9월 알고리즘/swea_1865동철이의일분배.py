import sys
sys.stdin = open("input.txt", "r")
# def bfs(x, result):
#     global max_work
#     if result <= max_work:
#         return
#     if x == N:
#         if max_work < result:
#             max_work = result
#         return
#     for y in range(N):
#         if not idx[y]:
#             idx[y] = 1
#             bfs(x+1, result * work[x][y]*0.01)
#             idx[y] = 0
#
#
# for test_case in range(1, int(input()) + 1):
#     N = int(input())
#     work = [ list(map(int,input().split())) for _ in range(N)]
#     idx = [0]*N
#     max_work = 0
#     bfs(0,1)
#
#     print('#{} {:6f}'.format(test_case, max_work*100))
#



# def DFS(flag, idx, value):
#     global ans
#     if flag == (1 << N) - 1:
#         if ans < value * 100:
#             ans = value * 100
#         return
#         # 진행할 수록 값이 작아지니 이미 구한 값보다 작다면 필요없다.
#     if value * 100 <= ans:
#         return
#
#     for i in range(N):
#         # 해당 일은 이미 배정되어서 처리함.
#         # print(flag, end='||')
#         # print(flag & (1 << i), end='||')
#         # print(flag | 1 << i)
#         if flag & (1 << i): continue
#         DFS(flag | 1 << i, idx + 1, value * (work[idx][i] / 100))
#
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#
#     work = [list(map(int, input().split())) for _ in range(N)]
#
#     ans = 0
#     #flag, idx, value
#
#     DFS(0, 0, 1)
#
#     print("#{} {:.6f}".format(tc, ans))

#
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     M = 1 << N
#     dp = [[0.0 for _ in range(M)] for _ in range(N)]
#
#     G = []
#     for i in range(N):
#         G.append(list(map(float, input().split())))
#         for j in range(N):
#             G[i][j] = G[i][j] / 100
#
#     for i in range(N):
#         dp[0][1 << i] = G[0][i]
#
#     for i in range(1, N):
#         for cur in range(1, M):
#             if dp[i - 1][cur] == 0:
#                 continue
#
#             for j in range(N):
#                 if cur & (1 << j) != 0 or G[i][j] == 0:
#                     continue
#                 next = cur | (1 << j)
#
#                 dp[i][next] = max(dp[i][next], dp[i - 1][cur] * G[i][j])
#     print("#%d %.6f" % (test_case, dp[N - 1][M - 1] * 100))



for t in range(int(input())):
    n=int(input())
    m=1<<n
    d=[0]*m
    p=[[*map(lambda x:x*.01,map(int,input().split()))]for _ in range(n)]
    d[0]=1
    for i in range(m-1):
        x=bin(i).count('1')
        for j in range(n):
            if(1<<j)&i==0:
                d[i|(1<<j)]=max(d[i|(1<<j)],d[i]*p[x][j])
    print(f'#{t+1} {d[-1]*100:.6f}')