# 124783
# 667767
# 054060
# 101123


# def run(list):
#     cnt = 0
#     s = 0
#     if len(list) < 3:
#         return 0
#     for p in range(len(list)-3+1):
#         if list[p]!=0 and list[p+1] !=0 and list[p+2] !=0:
#             return 1
#     return 0
#
#
# def triple(list):
#     for li in list:
#         if li == 3:
#             return 1
#     return 0
#
# for tc in range(1,5):
#     card = list(map(int,input()))
#     idx = [0]*10
#     result = 'NO'
#     for i in card:
#         idx[i] += 1
#         if triple(idx) == 1 or run(idx) == 1:
#             result = 'Babygin'
#             break
#     print('#{} {}'.format(tc, result))





# number = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# n = len(number)
# result = []
# for i in range(1<<n):
#     sub = []
#     for j in range(n):
#         if i &(1<<j):
#             sub.append(number[j])
#     if sum(sub) == 0:
#         result.append(sub)
# print(*result)
# a = [1]
# a[0:0] = [5]
# print(a[:0]+a[0:0] + a)
a = [8, 7, 1, 2]
a = sorted(a)
print(type(a))