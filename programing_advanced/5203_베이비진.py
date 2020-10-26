import sys

#sys.stdin = open("input.txt", "r")
def run(list):
    cnt = 0
    s = 0
    if len(list) < 3:
        return 0
    for p in range(len(list)-3+1):
        if list[p]!=0 and list[p+1] !=0 and list[p+2] !=0:
            return 1
    return 0


def triple(list):
    for li in list:
        if li == 3:
            return 1
    return 0

for test_case in range(1, int(input()) + 1):
    card = list(map(int,input().split()))
    o = []
    o_idx = [0]*10
    t = []
    t_idx = [0]*10
    result = 0
    for i in range(12):
        k = card[i]
        if i % 2:
            t.append(k)
            t_idx[k] += 1
            #run인지 triple인지 확인.
            if triple(t_idx) ==1 or run(t_idx) == 1:
                result = 2
                break
        else:
            o.append(k)
            o_idx[k] += 1
            if triple(o_idx) == 1 or run(o_idx) == 1:
                result = 1
                break
    print('#{} {}'.format(test_case, result))
