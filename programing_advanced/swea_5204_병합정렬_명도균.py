import sys

#sys.stdin = open("input.txt", "r")
def m_Sort(li):
    global cnt
    n = len(li)
    if n == 1:
        return li
    l_arr = m_Sort(li[:n//2])
    r_arr = m_Sort(li[n//2:])
    if l_arr[-1] > r_arr[-1]:
        cnt += 1
    return merge(l_arr, r_arr)

def merge(left, right):
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result



for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    r = m_Sort(arr)
    print('#{} {} {}'.format(test_case, r[len(r)//2], cnt))

