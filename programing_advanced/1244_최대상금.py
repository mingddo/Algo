import sys
sys.stdin = open("input1.txt", "r")
#idx는 현재 바꿔야하는 자리
def change(idx, mode):
    global count, index, s_number
    s_max = 0
    max_idx = 0
    if count == 0:
        return
    #현재 바꾸려는 자리가 가장 큰 수이면 바꾸지 않고 넘어간다.
    if number[idx] == m:
        return
    else:
        for j in range(idx, n):
            if number[j] > s_max:
                s_max = number[j]
                max_idx = j
        index.append(max_idx)
        number[idx], number[max_idx] = number[max_idx], number[idx]
        s_number.append(number[max_idx])
        # print(number)
        count -= 1
        return




for test_case in range(1, int(input()) + 1):
    q = list(input().split())
    count = int(q[1])
    number = list(map(int,q[0]))
    n = len(number)
    m = max(number)
    index = []
    s_number = []
    # max 값이 두 개 이상이면, 다른 함수를 실행시킬꺼야.
    if number.count(m) > 1:
        for i in range(n):
            change(i, 1)
        if len(index) > 1:
            s_number = sorted(number, reverse=True)
            print(index)
            print(s_number)
            index = sorted(index)
            for q in range(len(index)):
                number[index[q]] = s_number[q]
        print('#{} {}'.format(test_case, number))
    else:
        for i in range(n):
            change(i, 0)
        # 다 바꾼거면 안으로 넣어줘. 왜냐면 위에 max값이 2개 이상인 것들은 그 인덱스 끼리 계속 바꾸면 되기 때문에 필요 없어.
        if count == 0:
            print('#{} {}'.format(test_case, number))
        else:
            while count != 0:
                number[-2], number[-1] = number[-1], number[-2]
                count -= 1
            print('#{} {}'.format(test_case, number))
