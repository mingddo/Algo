
import sys

sys.stdin = open("input(1).txt", "r")

for tc in (1, int(input())+1):
    N = int(input())
    result = 'No'
    arr = list(map(int,input().split()))
    num = set()
    arr_set = set()
    for a in arr:
        num.add(a)
    for i in range(1,N+1):
        arr_set.add(i)
    if num == arr_set:
        result = 'Yes'

    print('#{} {}'.format(tc, result))

