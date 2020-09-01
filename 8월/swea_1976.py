import sys


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    clock = list(map(int, input().split()))

    minute_hour = (clock[1] + clock[3]) // 60
    minute = (clock[1] + clock[3]) % 60
    hour = (clock[0] + clock[2] + minute_hour) % 12
    print(f'#{test_case} {hour} {minute}')