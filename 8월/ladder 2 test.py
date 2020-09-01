import sys
sys.stdin = open("input (1).txt", "r")

def dfs(a,b):
    global result
    global visited
    visited.append((a,b))
    #맨위에 가면 멈추기
    if a == 0:
        result = b
        return len(visited)
    #델타 탐색으로 위 양옆 탐색 후 이동
    for d in range(3):
        new_x = a + d_x[d]
        new_y =b + d_y[d]
        if (0<= new_x < 100) and (0<= new_y < 100) and (arr[new_x][new_y]==1) and ((new_x,new_y) not in visited):
            return dfs(new_x,new_y)

for _ in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    d_x = [0, 0, -1]
    d_y = [-1, 1, 0]
    result = 0
    end = []
    start = 0
    min = 99999
    for i in range(100):
        if arr[99][i]:
            end.append(i)
    for e in end:
        visited = []
        l = dfs(99,e)
        if min > l:
            min = l
            start = result
        elif min == l:
            if start < result:
                start = result

    print('#{} {}'.format(tc, start))
