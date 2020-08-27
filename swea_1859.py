import sys


#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    princes = list(map(int, input().split()))
    max_price = max(princes)
    idx_max = princes.index(max_price)
    result = 0
    k = 0
    if idx_max == 0:
        result = 0
    elif idx_max == len(prices)-1:
        for c in a[:-1:-1]:
            result += max_price - c
    else:
        for a in a[:idx_max:-1]:
            result += (max_price - princes[a])

        for b in a[idx_max+1: :-1]: 
            if k < b:
                k = b
            else:
                result += k-b
    print(f'#{test_case} {result}')


    

    
