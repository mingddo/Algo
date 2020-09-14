import sys

#sys.stdin = open("input.txt", "r")

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    cheeze = list(map(int,input().split()))
    oven = cheeze[:N]
    pizza = list(range(N))
    num = list(range(N, M))
    while True:
        for i in range(N):
            if pizza.count(-1) == N - 1:
                break
            if oven[i]:
                oven[i] = oven[i] // 2
                if oven[i] == 0:
                    if len(num):
                        pizza[i] = num.pop(0)
                        oven[i] = cheeze[pizza[i]]
                    else:
                        pizza[i] = -1
        if pizza.count(-1) == N - 1:
            break
    for p in pizza:
        if p != -1:
            result = p

    print('#{} {}'.format(tc, result+1))


