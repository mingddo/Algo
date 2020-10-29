
import sys

#sys.stdin = open("input.txt", "r")
def combi(li):
    global result
    if len(li) == N-1:
        s_min = 0
        n_li = [1] + li + [1]
        print(li)
        for j in range(N):
            if s_min > result:
                break
            s_min += arr[n_li[j]-1][n_li[j+1]-1]
        if result > s_min:
            result = s_min
    else:
        for i in range(2,N+1):
            if visited[i] == 0:
                visited[i] = 1
                li.append(i)
                combi(li)
                li.pop()
                visited[i] = 0




for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    sub = []
    visited = [0,1]+[0]*(N)
    result = 987654321
    combi(sub)
    print('#{} {}'.format(test_case, result))



