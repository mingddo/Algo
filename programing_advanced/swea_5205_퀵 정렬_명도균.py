def quickSort(a, start, end):
    if end - start <= 0:
        return
    pivot = a[end]
    i = start
    for j in range(start,end):
        if a[j] <= pivot:
            a[i], a[j] = a[j] , a[i]
            i += 1

    a[i], a[end] = a[end], a[i]
    print(i)
    if i == N//2:
        return
    quickSort(a,start, i-1)
    quickSort(a, i+1, end)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))
    quickSort(arr, 0, N-1)
    print('#{} {}'.format(tc,arr[N//2]))
