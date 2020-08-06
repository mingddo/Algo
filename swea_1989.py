
import sys


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    words = input()
    result = 1
    length = len(words)//2
    for i in range(length):
        if words[i] != words[-(i+1)]:
            result = 0
    print('#{} {}'.format(test_case, result))