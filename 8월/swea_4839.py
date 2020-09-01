import sys

T = int(input())

for tc in range(1, T + 1):
    num = list(map(int, input().split()))
    result = []
    for i in range(2):
        start = 1
        end = num[0]
        cnt = 0
        page = num[i+1]

        while start <= end:
            c = (start + end) // 2
            
            if c == page:
                break
            elif c < page:
                start = c
                cnt += 1
            else:
                end = c 
                cnt += 1
        result.append(cnt)   
    
    if result[0] < result[1]:
        print('#%d'%tc, 'A')
    elif result[0] == result[1]:
        print('#%d'%tc,'0')
    
    else:
        print('#%d'%tc,'B')
