
import sys

#sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N, M = map(int,input().split())
    word = set()
    valid = set()
    cnt = 0
    for _ in range(N):
        word.add(input())
    for _ in range(M):
        w = input()
        if w in word and w not in valid:
            valid.add(w)
            cnt += 1
    print('#{} {}'.format(test_case,cnt))
