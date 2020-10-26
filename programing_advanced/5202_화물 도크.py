import sys

sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N = int(input())
    temp = [list(map(int,input().split())) for _ in range(N)]
    #끝나는 시간으로 정렬
    arr = sorted(temp, key= lambda x : x[1])
    cnt = 1
    end = arr[0][1]
    for j in range(1,N):
        if arr[j][0] >= end:
            cnt += 1
            end = arr[j][1]

    print('#{} {}'.format(test_case, cnt))
