import sys
sys.stdin = open("input2.txt", "r")
from itertools import permutations
import time
start = time.time()

def cal(li):
    global r_max, r_min
    total = number[0]
    x = 0
    while x < N-1:
        if li[x] == '+':
            total = total + number[x+1]
        elif li[x] == '-':
            total = total - number[x+1]
        elif li[x] == '*':
            total = total * number[x+1]
        else:
            total = int(total / number[x+1])
        x += 1
    if total < r_min:
        r_min = total
    if total > r_max:
        r_max = total

for test_case in range(1, int(input()) + 1):
    N = int(input())
    sign = '+-*/'
    o_s = ''
    c = list(map(int,input().split()))
    for k in range(4):
        o_s += sign[k]*c[k]
    r_min = 10**12
    r_max = -(10**12)
    number = list(map(int,input().split()))
    o = list(set(permutations(o_s,len(o_s))))
    for s_o in o:
        cal(s_o)
    print('#{} {}'.format(test_case, r_max-r_min))
print("time :", time.time() - start)
