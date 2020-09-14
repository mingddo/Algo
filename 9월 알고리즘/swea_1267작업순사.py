import sys

#sys.stdin = open("input.txt", "r")
def f(n):
    global result
    q= []
    result[n-1] = [n,1]
    q.append(n)
    while q:
        a = q.pop(0)
        for i in order[a]:
            if result[i-1]==0:
                result[i-1] = [i,result[a-1][1]+1]
                q.append(i)
            else:
                if result[i-1][1] < result[a-1][1]+1:
                    result[i - 1][1] = result[a - 1][1] + 1
                    q.append(i)
    return


for test_case in range(1, 11):
    V, E = map(int, input().split())
    path = list(map(int,input().split()))
    order = [[] for _ in range(V+1)]
    arrival = []
    for m in range(E):
        a, b = path[2*m], path[2*m+1]
        order[a].append(b)
        arrival.append(b)
    result = [0]*V
    for v in range(1, V+1):
        if v not in arrival:
            f(v)
    n_result = sorted(result,key=lambda x: x[1])
    #print(n_result)
    print('#{}'.format(test_case),end=' ')
    for nr in n_result:
        print(nr[0],end=' ')
    print()
