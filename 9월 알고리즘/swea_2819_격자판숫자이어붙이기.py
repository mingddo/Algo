import sys

sys.stdin = open("input(1).txt", "r")
# def bfs(x,y,num):
#     if len(num) == 7:
#         numbers.add(num)
#     else:
#         for d in range(4):
#             n_x = x + d_x[d]
#             n_y = y + d_y[d]
#             if 0 <= n_x < 4 and 0 <= n_y < 4:
#                 bfs(n_x,n_y, num)
#
#
#
# for test_case in range(1, int(input()) + 1):
#     arr = [list(input().split()) for _ in range(4)]
#     numbers = set()
#     d_x = [0, 0, -1, 1]
#     d_y = [-1, 1, 0, 0]
#     #함수 호출하기
#     for a in range(4):
#         for b in range(4):
#             bfs(a,b,arr[a][b])
# print('#{} {}'.format(test_case,len(numbers)))



# def f(r, c, num):
#     if len(num) == 7:
#         used.add(num)
#     else:
#         for i in range(4):
#             dr, dc = r + d_row[i], c + d_col[i]
#             if 0 <= dr < 4 and 0 <= dc < 4:
#                 f(dr, dc, num + arr[dr][dc])
#
#
# d_row = [-1, 1, 0, 0]
# d_col = [0, 0, -1, 1]
# for t in range(1, int(input()) + 1):
#     arr = [list(input().split()) for _ in range(4)]
#     used = set()
#     for rr in range(4):
#         for cc in range(4):
#             f(rr, cc, arr[rr][cc])
#
#     print("#{} {}".format(t, len(used)))

