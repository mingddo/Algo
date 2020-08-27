import sys

sys.stdin = open("GNS_test_input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for T in range(1, int(input()) + 1):
    numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    tc, N = map(str, input().split())
    num = list(map(str,input().split()))
    num_dict = {}
    for n in numbers:
        if n in  num:
            num_dict[n] = num.count(n)
    # 다 저장 했으면 정렬해서 프린트하기.
    values = list(num_dict.keys())
    print('{}'.format(tc))
    for v in values:
        print((v + ' ') * num_dict[v], end='')
    print()