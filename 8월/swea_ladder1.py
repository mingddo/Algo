import sys
sys.stdin = open("input.txt", "r")
def dfs(a,b):
    global result
    visited.append((a,b))
    #맨위에 가면 멈추기
    if a == 0:
        result = b
        return
    #델타 탐색으로 위 양옆 탐색 후 이동
    for d in range(3):
        new_x = a + d_x[d]
        new_y =b + d_y[d]
        if (0<= new_x < 100) and (0<= new_y < 100) and (arr[new_x][new_y]==1) and ((new_x,new_y) not in visited):
            return dfs(new_x,new_y)

for _ in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    visited = []
    d_x = [0, 0, -1]
    d_y = [-1, 1, 0]
    result = 0
    dfs(99,arr[99].index(2))

    print('#{} {}'.format(tc, result))


#
# def dfs(i,v):
#     global result
#     visited.append((i,v))
#     if i == 0:
#         result = v
#         return
#     for d in range(3):
#         new_x = i + d_x[d]
#         new_y = v + d_y[d]
#         if (-1 < new_x < 100) and (-1< new_y < 100) and (arr[new_x][new_y]==1) and ((new_x,new_y) not in visited):
#             return dfs(new_x,new_y)
#
#
# for t in range(100):
#     tc = int(input())
#     arr = [list(map(int,input().split())) for _ in range(100)]
#     visited = []
#     d_x = [0, 0, -1]
#     d_y = [-1, 1, 0]
#     end = arr[99].index(2)
#     result = 0
#     dfs(98,end)
#
#     print('#{} {}'.format(tc, result))