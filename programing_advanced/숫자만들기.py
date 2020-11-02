import sys
sys.stdin = open("input2.txt", "r")

def make_number(x, total):
    if x > N-1:
        if total < result[0]:
            result[0] = total
        if total > result[1]:
            result[1] = total
            return
    for i in range(len(o_s)):
        if o_s[i]:
            o_s[i] -= 1
            if sign[i] == '+':
                make_number(x+1, total + number[x])
            elif sign[i] == '-':
                make_number(x+1, total - number[x])
            elif sign[i] == '*':
                make_number(x+1, total * number[x])
            else:
                make_number(x+1, int(total / number[x]))
            o_s[i] += 1



for test_case in range(1, int(input()) + 1):
    N = int(input())
    sign = '+-*/'
    o_s = list(map(int,input().split()))
    # 0번 인덱스는 min값, 1번 인덱스는 max값
    result = [10**12,-(10**12)]
    number = list(map(int,input().split()))
    make_number(1,number[0])
    print('#{} {}'.format(test_case, result[1]-result[0]))

