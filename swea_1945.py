

import sys


#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while True:
        if N % 2:
            break
        else:
            a += 1
            N = N // 2
    
    while True:
        if N % 3:
            break
        else:
            b += 1
            N = N // 3
    while True:
        if N % 5:
            break
        else:
            c += 1
            N = N // 5

    while True:
        if N % 7:
            break
        else:
            d += 1
            N = N // 7

    while True:
        if N % 11:
            break
        else:
            e += 1
            N = N // 11
        
    print(f'#{test_case} {a} {b} {c} {d} {e}')
    