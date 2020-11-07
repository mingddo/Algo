
for tc in range(1, int(input())+1):
    N, M = map(int,input().split())
    front = set()
    cnt = 0
    for _ in range(N):
        w = input()
        for i in range(len(w)+1):
            front.add(w[:i+1])
    for _ in range(M):
        if input() in front:
            cnt+=1

    print('#{} {}'.format(tc, cnt))