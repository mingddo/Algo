
def selectSort(idx):
    if idx == len(arr)-1:
        return
    i = idx
    j = idx + 1
    min_number = 987654321
    min_idx = 0
    for j in range(j, len(arr)):
        if arr[j] < min_number:
            min_idx = j
            min_number = arr[j]
    if arr[i] > min_number:
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return selectSort(i+1)

arr = [7, 5, 1, 8, 6, 10, 2, 9, 1, 4, 3,4, 6, 5, 7, 2]
selectSort(0)
print(arr)
