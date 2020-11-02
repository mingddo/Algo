
import sys

sys.stdin = open("input3.txt", "r")
def distance(cnt,total, x, y):
    global min_d
    if total > min_d:
        return
    if cnt == N:
        total = total + abs(x-temp[2]) + abs(y-temp[3])
        if min_d > total:
            min_d = total
        return
    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            distance(cnt+1, total+ abs(x-temp[j*2+4])+ abs(y-temp[j*2+5]), temp[j*2+4], temp[j*2+5])
            visited[j] = 0

for test_case in range(1, int(input()) + 1):
    N = int(input())
    temp = list(map(int,input().split()))
    min_d = 100**10
    visited = [0]*N
    distance(0,0,temp[0],temp[1])
    print('#{} {}'.format(test_case, min_d))
