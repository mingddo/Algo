N = int(input())
card = list(map(int,input().split()))
arr = []
for i in range(N):
    if i == 0:
        arr.append(i+1)
    else:
        if card[i] == 0:
            arr.append(i+1)
        else:
            j = i-card[i]
            arr[j:j] = [i+1]
print(*arr)
