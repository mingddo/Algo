import sys

sys.stdin = open("input.txt", "r")
def find(n):
    global cash
    i = n
    for x in range(n+1):
        cash += sum(arr[i+x][x:N-x])
        cash += sum(arr[i-x][x:N-x])
    return



for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    cash = 0
    n = N//2
    find(n)
    cash = cash- sum(arr[n])
    print('#{} {}'.format(test_case,cash))