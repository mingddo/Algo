import sys

#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    result = set(range(10))
    numbers = set()
    i = 1
    cnt = 0
    while True:
        cnt += 1
        num = str(i * N)
        for a in num:
            numbers.add(int(a))
        if numbers == result:
            break
        else:
            i += 1
    print(f'#{test_case} {cnt * N}')
    
