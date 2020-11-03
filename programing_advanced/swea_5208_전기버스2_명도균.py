import sys
#sys.stdin = open("input.txt", "r")
# def charge(x, e, count):
#     global min_cnt
#     if e < 0:
#         return
#     if count > min_cnt:
#         return
#     if x + e >= N-1:
#         if count < min_cnt:
#             min_cnt = count
#         return
#     for k in range(x+1, x+e+1):
#         charge(k, eg[k], count+1)
#
#
#
#
# for test_case in range(1, int(input()) + 1):
#     arr = list(map(int,input().split()))
#     N = arr[0]
#     eg = arr[1:]
#     min_cnt = 987654321987654321
#     visited = [0]*N
#     visited[0] = 1
#     charge(0, eg[0] , 0)
#     print('#{} {}'.format(test_case, min_cnt))


def charge(x, e, count):
    global min_cnt
    if e < 0:
        return
    if count > min_cnt:
        return
    if x == N-1:
        if count< min_cnt:
            min_cnt = count
        return
    else:
        if visited[x] == 0:
            #충전을 하고 가고
            visited[x] = 1
            charge(x+1, eg[x]-1, count+1)
            #충전을 안하고 가고
            visited[x] = 0
            charge(x + 1, e - 1, count)
        else:
            charge(x + 1, e - 1, count)


for test_case in range(1, int(input()) + 1):
    arr = list(map(int,input().split()))
    N = arr[0]
    eg = arr[1:]
    min_cnt = 987654321987654321
    visited = [0]*N
    visited[0] = 1
    charge(0, eg[0] , 0)
    print('#{} {}'.format(test_case, min_cnt))