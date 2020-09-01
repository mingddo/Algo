
# import sys

# #sys.stdin = open("input.txt", "r")
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    flags = [list(input()) for _ in range(N)]
    result = []
# 1차 list 를 3개 구간으로 나누기
# 구간을 표현할 때 (시작 인덱스, 끝 인덱스)
# 3개 구간 : (0,i ) (i+1, j) (j+1, N-1)
# 3개 구간으로 나누기 위한 2개의 분할 지점.
    arr = list(range(1,N+1))
    n = len(arr)
    for i in range(0, n-3+1):
        for j in range(i+1, n-2+1):
            change = 0
            for w in arr[:i+1]:
                w_c = M - flags[w-1].count('W')
                change += w_c
            for b in arr[i+1: j+1]:
                b_c = M - flags[b-1].count('B')
                change += b_c
            for r in arr[j+1: n]:
                r_c = M - flags[r-1].count('R')
                change += r_c
            result.append(change)
    
    print('#{} {}'.format(tc, min(result)))

            # print(arr[:i+1], arr[i+1:j+1], arr[j+1:n]) 
            
