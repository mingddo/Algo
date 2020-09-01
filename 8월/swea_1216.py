import sys
sys.stdin = open("input.txt", "r")
# 회문 찾는 함수 (가로일 때)
# 회문 찾는 함수 (세로일 때)
def pal_test (arr):
    result = 0
    for a in arr:
        for i in range(100, 2, -1):
            if result > i:
                break
            for j in range(100 - i + 1):
                if a[j:i+j] == a[j:i+j][::-1] and result < len(a[j:i+j]):
                    result = (len(a[j:i+j]))
                    break
    return result

def vertical (arr):
    turn_arr = [ [0]*100 for _ in range(100)]
    for x in range(100):
        for y in range(100):
            turn_arr[x][y] = arr[y][x]
    return turn_arr


for _ in range(10):
    tc = input()
    arr = [input() for _ in range(100)]
# 가로 회문 테스트.
    result_row = pal_test(arr)
    result_col = pal_test(vertical(arr))
    if result_row >= result_col:
        print('#{} {}'.format(tc, result_row))
    else:
        print('#{} {}'.format(tc, result_col))