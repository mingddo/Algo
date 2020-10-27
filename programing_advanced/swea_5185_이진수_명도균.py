
# import time
# start = time.time()

def bin(n):
    if n == 0:
        return '0000'
    sub =''
    while n > 1:
        sub += str(n % 2)
        n = n//2
    sub += '1'
    sub = sub[::-1]
    if len(sub) < 4:
        sub = '0'* (4-len(sub)) + sub
    return sub

for test_case in range(1, int(input()) + 1):
    st = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    temp = list(input().split())
    N = int(temp[0])
    result = ''
    for i in temp[1]:
        if i.isdigit():
            result += bin(int(i))

        else:
            result += bin(st.get(i))

    print('#{} {}'.format(test_case, result))
# print(time.time()-start)