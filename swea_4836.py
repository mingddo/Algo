import sys


T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    arr = [[0]* 10 for _ in range(10)]
    colors = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    # 이중포문으로 색칠하기
    # 만약 arr에 있는 값이 0이 아니고, 주어진 color의 값과 같지 않다면(2를 칠해야하는데 1이 있다면)
    # cnt += 1
    for color in colors: # N만큼 반복해서 색칠해야함.
        for x in range (color[0], color[2]+1):
            for y in range (color[1], color[3]+1):
                if arr[x][y] == 0:
                    arr[x][y] = color[4]
                
                elif arr[x][y] < 3 and arr[x][y] != color[4]:
                    arr[x][y] += color[4]
    for array in arr:
        for a in array:
            if a == 3:
                cnt += 1
    
    print(f'#{test_case} {cnt}')