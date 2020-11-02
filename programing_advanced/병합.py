def merge_sort(Data):
    if len(Data) <= 1:
        return Data

    mid = len(Data) // 2
    left = merge_sort(Data[:mid])
    right = merge_sort(Data[mid:])
    return merge(left, right)

def merge(left, right):
    global cnt

    left_N, right_N = len(left), len(right)
    result = [0] * (left_N + right_N)
    left_i, right_i = 0, 0
    i = 0

    if left[-1] > right[-1]:
        cnt += 1

    while left_i != left_N and right_i != right_N:
        if left[left_i] <= right[right_i]:
            result[i] += left[left_i]
            i += 1
            left_i += 1
        else:
            result[i] += right[right_i]
            i += 1
            right_i += 1

    if left_i != left_N:
        while left_i != left_N:
            result[i] += left[left_i]
            i += 1
            left_i += 1

    if right_i != right_N:
        while right_i != right_N:
            result[i] += right[right_i]
            i += 1
            right_i += 1

    return result


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Data = list(map(int, input().split()))
    cnt = 0
    Data = merge_sort(Data)

    print('#%d %d %d'%(tc, Data[N//2], cnt))