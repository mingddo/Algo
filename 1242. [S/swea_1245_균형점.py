import sys
sys.stdin = open("input2.txt", "r")

for test_case in range(1, int(input()) + 1):
    N= int(input())
    arr = list(map(int, input().split()))
    m = arr[:N]
    w = arr[N:]
    result = []
    for i in range(N-1):
        l = m[i]
        h = m[i+1]
        while h-l > 1/(10**12):
            mid = (l + h) / 2
            l_s = 0
            r_s = 0
            for k in range(N):
                s = w[k] / (m[k]-mid)**2
                if m[k] < mid:
                    l_s += s
                else:
                    r_s += s
            if l_s < r_s:
                h = mid
            else:
                l = mid
        result.append(mid)
    print('#%s %s' % (test_case, ' '.join('%.10f' % f for f in result)))

#
#
#
#

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     line = list(map(int, input().split()))
#     X = line[:N]
#     M = line[N:]
#     ans = []
#     for i in range(1, N):
#         low = X[i-1]
#         high = X[i]
#         while high - low > 1 / (10**12):
#             mid = (low + high) / 2
#             left = right = 0
#             for i in range(N):
#                 force = M[i] / (mid-X[i])**2
#                 if X[i] < mid:
#                     left += force
#                 else:
#                     right += force
#             if left < right:
#                 high = mid
#             else:
#                 low = mid
#         ans.append(mid)
#     print('#%s %s' % (tc, ' '.join('%.10f' % f for f in ans)))
