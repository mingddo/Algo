def find_p(x):
    if p[x] != x:
        p[x] = find_p(p[x])
    return p[x]


for test_case in range(1, int(input()) + 1):
    V, E = map(int,input().split())
    dst = []
    p = list(range(V+1))
    for _ in range(E):
        a, b, c = map(int, input().split())
        dst.append((a, b, c))
    dst = sorted(dst, key = lambda x : x[2])
    cnt = 0
    total = 0
    for d in dst:
        if cnt == V:
            break
        x = find_p(d[0])
        y = find_p(d[1])
        if x != y:
            if x > y:
                p[x] = y
            else:
                p[y] = x
            total += d[2]
            cnt += 1

    print('#{} {}'.format(test_case, total))
