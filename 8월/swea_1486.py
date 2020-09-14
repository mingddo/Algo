# def powerset(n):
#     global B
#     for i in range(1<<n):
#         cnt = 0
#         for j in range(n):
#             subset = i & (1<<j)
#             if subset:
#                 cnt += li[j]
#         if cnt >= B:
#             s.append(cnt - B)
#     return
#
# for tc in range(1, int(input())+1):
#     N, B = map(int, input().split())
#     li = list(map(int,input().split()))
#     s = []
#     powerset(N)
#     print('#{} {}'.format(tc, min(s)))
#
#
def subset(k, n, cur_sum):
    global result
    if cur_sum-B > result:
        return
    if k == n:
        if cur_sum >= B and result > cur_sum-B:
            result = cur_sum - B
        return
    else:
        bits[k] = 1
        subset(k + 1, n, cur_sum + li[k])
        bits[k] = 0
        subset(k + 1, n, cur_sum)

for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    li = list(map(int,input().split()))
    bits = [0]*N
    result = 987654321
    subset(0, N, 0)
    print('#{} {}'.format(tc,result))

