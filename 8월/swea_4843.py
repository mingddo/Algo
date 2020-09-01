import sys

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N-1):
        if i %2: 
            min_n = i
            for j in range(i+1, N):
                if arr[min_n] > arr[j]:
                    min_n = j
            arr[i], arr[min_n] = arr[min_n], arr[i] 

        else: 
            max_n = i
            for j in range(i+1, N):
                if arr[max_n] < arr[j]:
                    max_n = j
            arr[i], arr[max_n] = arr[max_n], arr[i] 

    
    print(f'#{test_case}',end=' ')
    for a in range(10):
        if a == 9:
            print(arr[a])
        else: 
            print(arr[a], end=' ')
	