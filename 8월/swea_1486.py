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
    if k == n:
        if cur_sum >= B:
            result.append(cur_sum - B)
        return
    else:
        bits[k] = 1
        A.append(li[k])
        subset(k + 1, n, cur_sum + li[k])
        A.pop

        bits[k] = 0
        subset(k + 1, n, cur_sum)

for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    li = list(map(int,input().split()))
    bits = [0]*N
    A = []
    result = []
    subset(0, N, 0)
    print('#{} {}'.format(tc, min(result)))

