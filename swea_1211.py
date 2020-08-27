import sys
sys.stdin = open("input (1).txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def dfs(x, y):
    global  visited
    visited.append((x,y))
    if x == 99:
        return (len(visited), s)
    for d in range(3):
        dx = x + d_x[d]
        dy = y + d_y[d]
        if 0 <= dx < 100 and 0 <= dy < 100 and ladder[dx][dy] == 1 and not (dx,dy) in visited:
            return dfs(dx,dy)

for test_case in range(1, 11):
    tc= int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    start = []
    d_x = [0, 0, 1]
    d_y = [-1, 1, 0]
    #모든 출발점을 start리스트에 저장
    for i in range(100):
        if ladder[0][i] == 1:
            start.append(i)
    min = 9999999
    result = []
    for s in start:
        visited = []
        result.append(dfs(0,s))
    r = sorted(result, key=lambda x: (x[0],-x[1]))


    print('#{} {}'.format(tc, r[0][1]))

