import sys
#sys.stdin = open("input.txt", "r")
def cost(x, total):
    global result
    if total > result:
        return
    if x == N and total < result:
        result = total
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                cost(x+1, total+temp[x][i])
                visited[i] = 0



for test_case in range(1, int(input()) + 1):
    N = int(input())
    temp = [list(map(int,input().split())) for _ in range(N)]
    result = 99 * 15 * 15
    visited = [0] * N
    cost(0,0)
    print('#{} {}'.format(test_case, result))
