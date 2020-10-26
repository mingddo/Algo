for test_case in range(1, int(input()) + 1):
    N, M = map(int,input().split())
    weight = list(map(int,input().split()))
    truck = list(map(int,input().split()))
    total = 0
    weight.sort(reverse=True)
    truck.sort(reverse=True)
    for w in weight:
        for i in range(len(truck)):
            if w <= truck[i]:
                total += w
                truck.pop(i)
                break

    print('#{} {}'.format(test_case, total))