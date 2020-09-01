import sys


#sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    triangle = []
    for i in range(1,n+1):
        triangle.append([1]*i)
    #print(triangle)
    for x in range(2,n):
        for y in range(1,len(triangle[x])-1):
            triangle[x][y] = triangle[x-1][y-1] + triangle[x-1][y]

    print(f'#{test_case}')
    for t in triangle:
        print(*t)