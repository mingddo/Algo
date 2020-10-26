N = int(input())
num = list(map(int,input().split()))
i = 0
d = 0
cnt = 0
count = [0]
while i != N-1:
    if i == 0:
        if num[i] <= num[i]:
            
    else:
        if num[i] - num[i-1] >=0:
            d = 1
            cnt += 1



print(max(count)+1)
