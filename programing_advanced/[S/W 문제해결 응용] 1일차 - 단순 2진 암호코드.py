import sys

#sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input()) + 1):
    code = {'0001101':0, '0011001':1,'0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9 }
    N, M = map(int, input().split())
    arr = ''
    temp = [input() for _ in range(N)]
    for t in temp:
        if t.find('1') != -1:
            arr = t.replace(" ","")
            break
    end = 0
    for i in range(M-1,-1,-1):
        if arr[i]=='1':
            end = i
            break
    start = end - 56 + 1
    num = []
    for j in range(8):
        num.append(code.get(arr[start+(j*7) : start+(j*7)+7]))
    v = num[-1]
    s_1 = 0
    s_2 = 0
    for k in range(7):
        # 찍수번
        if k%2:
            s_2 += num[k]
        else:
            s_1 += num[k]

    total = s_1*3 + s_2 + v
    if total % 10 == 0:
        result = sum(num)
    else:
        result = 0

    print('#{} {}'.format(test_case, result))