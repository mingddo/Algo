def qs(a, start, end):
    if end - start <= 0:
        return
    pivot = a[end]
    i = start
    for j in range(start,end):
        if a[j] <= pivot:
            a[i], a[j] = a[j] , a[i]
            i += 1

    a[i], a[end] = a[end], a[i]
    print(a)
    print(i)
    print(end)
    qs(a,start, i-1)
    qs(a, i+1, end)

a = list(map(int,input().split()))
qs(a, 0, len(a)-1)
print(a)




#
# def quickSort(li):
#     if len(li) <= 1:
#         return li
#     left = []
#     right = []
#     pivot = li[len(li)//2]
#
#     a = 0
#     b = len(li)-1
#     while a < len(li)//2:
#         if li[a] > pivot and li[b] < pivot:
#             li[a], li[b] = li[a], li[b]
#         a =+ 1
#         b -= 1
#
#     li[a], li[-1] = li[-1], li[a]
#     return quickSort(li[:a]) + [pivot] + quickSort(li[a+1:])

    # for i in li:
    #     if i < pivot:
    #         left.append(i)
    #     elif i == pivot:
    #         same.append(i)
    #     else:
    #         right.append(i)
    # return quickSort(left) + same + quickSort(right)
# list = list(map(int,input().split()))
# print(quickSort(list))


# 11 45 23 81 28 34
# 11 45 22 81 23 34 99 22 17 8
# 1 1 1 1 1 0 0 0 0 0