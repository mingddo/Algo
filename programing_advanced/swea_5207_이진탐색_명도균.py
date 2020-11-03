import sys
sys.stdin = open("sample_input4.txt", "r")
def bin_search(li):
    global cnt
    for k in li:
        start = 0
        end = len(n) -1
        valid = 0
        while start <= end:
            mid = (start + end) // 2
            if n[mid] == k:
                cnt += 1
                break
            #오른쪽 선택
            elif n[mid] < k:
                if valid != 'right':
                    valid = 'right'
                    start = mid+1
                else:
                    break
            else:
                if valid != 'left':
                    valid = 'left'
                    end = mid-1
                else:
                    break
    return


for test_case in range(1, int(input()) + 1):
    N, M = map(int,input().split())
    n = sorted(list(map(int, input().split())))
    m = list(map(int, input().split()))
    cnt = 0
    bin_search(m)
    print('#{} {}'.format(test_case, cnt))
