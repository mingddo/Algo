import sys

#sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]
    count = 0
    for b in range(N):
        cnt = ''
        for a in range(N):
            if table[a][b] == 1:
                cnt += 'N'
            elif table[a][b] == 2:
                cnt += 'S'
        if len(cnt) > 1:
            count += cnt.count('NS')
    print('#{} {}'.format(test_case,count))