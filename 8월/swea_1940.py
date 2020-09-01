import sys


#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    distance = 0
    v = 0
    for i in range(N):
        a = list(map(int, input().split()))
        if a[0] == 0:
            distance += v
        elif a[0] == 1:
            v += a[1]
            distance += v
        elif  a[0] == 2:
            v -= a[1]
            if v < 0:
                v = 0
            distance += v
    
    print(f'#{test_case} {distance}')
            