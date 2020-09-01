import sys

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(range(1,13))
    n = len(A)
    cnt = 0
    results = []
    for i in range (1 << n):
        sub = []
        for j in range(n+1):
            if i & (1 << j):
                sub.append(A[j])
        results.append(sub)
    print(results)

    for result in results:
        if len(result) == N and sum(result) == K:
            cnt += 1
    print('#%d'%test_case, cnt)

