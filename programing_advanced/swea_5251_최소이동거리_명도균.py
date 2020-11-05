import sys
#sys.stdin = open("input.txt", "r")
def d(k):
    #k는 시작점.
    n = k
    m = set([k])
    visited[k] = 1
    temp = dst[0][:]
    temp[k] = 0
    while m != r:
        if n == N:
            return temp[n]
        min_d = 987654321
        for i in range(N+1):
            temp[i] = min(temp[i], temp[n]+dst[n][i])
            if temp[i] < min_d and not visited[i]:
                min_d = temp[i]
                n = i
        visited[n] = 1
        m.add(n)
    return temp[N]



for test_case in range(1, int(input()) + 1):
    N, E = map(int,input().split())
    dst = [[987654321]*(N+1) for _ in range(N+1)]
    r= set(range(N+1))
    for _ in range(E):
        a, b, c = map(int,input().split())
        dst[a][b] = c
        dst[b][a] = c
    visited = [0]*(N+1)
    result = d(0)
    print ('#{} {}'.format(test_case, result))


