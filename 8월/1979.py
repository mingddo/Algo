import sys
sys.stdin = open("input.txt", "r")
def search(arr):
    global number
    for a  in arr:
        cnt = 0
        i = 0
        while i < N-1:
            if a[i]== 1 and a[i+1]==1:
                if i == N-2:
                    cnt += 2
                    number.append(cnt)
                    break
                cnt += 1
            elif a[i] == 1 and a[i+1]==0:
                cnt += 1
                number.append(cnt)
                cnt = 0
                i += 1
            i += 1
    return

def rotate(arr_list):
    new_arr = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            new_arr[x][y] = arr_list[y][x]
    return new_arr


for test_case in range(1, int(input()) + 1):
    N , K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    number = []
    search(arr)
    search(rotate(arr))
    print('#{} {}'.format(test_case, number.count(K)))

