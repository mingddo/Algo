import sys

#sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    while M > 0:
        M -= 1
        numbers.append(numbers.pop(0))
    print('#{} {}'.format(test_case,numbers.pop(0)))