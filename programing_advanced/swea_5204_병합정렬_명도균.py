import sys
# sys.stdin = open("input.txt", "r")
#append로 풀었을 때 badgateway 나옴.
#index로 접근하기
def m_Sort(li):
    global cnt
    n = len(li)
    if n == 1:
        return li
    l_arr = m_Sort(li[:n // 2])
    r_arr = m_Sort(li[n // 2:])
    if l_arr[-1] > r_arr[-1]:
        cnt += 1
    return merge(l_arr, r_arr)

def merge(left, right):
    result = [0]*(len(left)+len(right))
    i = 0
    l = 0
    r = 0
    while len(left) - l > 0 and len(right) -r > 0:
        if left[l] < right[r]:
            result[i] = left[l]
            i += 1
            l += 1
        else:
            result[i] = right[r]
            i += 1
            r += 1
    if l != len(left):
        while l != len(left):
            result[i] = left[l]
            i += 1
            l += 1
    if r != len(right):
        while r != len(right):
            result[i] = right[r]
            i += 1
            r += 1
    return result

for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = m_Sort(arr)
    print('#{} {} {}'.format(test_case, arr[(len(arr) // 2)], cnt))
