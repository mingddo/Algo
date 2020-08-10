import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    words = ''
    for n in range(N):
        w, num = input().split()
        words += (w * int(num))
    
    if len(words)%10:
        len_words = len(words)//10 + 1
    else:
        len_words = len_words // 10
    start = 0
    print(f'{test_case}')
    for l in range(1, len_words + 1):
        if l == len_words:
            print(words[start:])
        else:
            print(words[start: 10*l])
            start = 10*l

