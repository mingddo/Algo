
import sys


#sys.stdin = open("input.txt", "r")


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1):
    test_case = int(input())
    numbers = []
    for i in range(100):
        numbers.append(list(map(int,input().split())))
    
    sums = []
    #가로의 합 먼저 구하기
    for h in range(100):
        sums.append(sum(numbers[h]))

    #세로의 합 구하기
    
    for v1 in range(100):
        total_v = 0
        for v2 in range(100):
            total_v += numbers[v2][v1]
        sums.append(total_v)
            
    #대각선의 합 구하기
    total_h1 = 0
    for h in range(100):
        total_h1 += numbers[h][99-h]
    sums.append(total_h1)

    total_h2 = 0
    for g in range(100):
        total_h2+= numbers[g][g]
    sums.append(total_h2)

    print(f'#{test_case} {max(sums)}')