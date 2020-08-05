import sys

def bi_search (p,k):
    start = 1
    end = p
    cnt = 0
    page = k
    while start <= end:
            c = (start + end) // 2
            if c == page:
                return cnt
                break
            elif c < page:
                start = c
                cnt += 1
            else:
                end = c 
                cnt += 1

T = int(input())

for tc in range(1, T + 1):
    p, a, b = map(int, input().split())
    A = bi_search(p,a)
    B = bi_search(p,b)
    
    if A < B:
        print('#%d'%tc, 'A')
    elif A == B:
        print('#%d'%tc,'0')
    
    else:
        print('#%d'%tc,'B')
