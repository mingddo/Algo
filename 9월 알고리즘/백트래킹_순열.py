# arr = ['+', '+', '+', '-', '*', '-', '-', '*', '*', '*','/']
# arr = 'ABAACEEHHHK'
# N = len(arr)
# sel = [0] * N
# visited = [0] * N
# d = {}
# def perm(idx):
#     if idx == N:
#         if d.get(''.join(sel),1):
#             d[''.join(sel)] = 0
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             sel[idx] = arr[i]
#             visited[i] = 1
#             perm((idx+1))
#             visited[i] = 0
# perm(0)
# print(len(d.keys()))
# print(d.keys())
from itertools import permutations
arr = '+++-*--***/'
# arr = 'ABAACEEHHHK'
result =list(set(permutations(arr,len(arr))))

print(result)
