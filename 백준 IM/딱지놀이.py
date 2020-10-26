def f(P,Q):
    for j in range(4,-1,-1):
        if P[j] > Q[j]:
           result.append('A')
           break
        elif P[j] < Q[j]:
            result.append('B')
            break
    else:
        result.append('D')

result = []
N = int(input())
for t in range(N):
    A = [0]*5
    B = [0]*5
    for x in range(2):
        k = list(map(int,input().split()))
        if x == 0:
            for i in k[1:]:
                A[i] += 1
        else:
            for i in k[1:]:
                B[i] += 1
    f(A,B)
    #승부 가리는 함수 호출
for r in result:
    print(r)