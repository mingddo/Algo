import sys
sys.stdin = open("input5.txt", "r")

def find_1(li, idx):
    for l in range(idx, -1, -1):
        if li[l] == '1':
            return l

# 뒤에서부터 개수 세서 넣는 함수 구현하기
# 필요한것 : 개수 리스트,
def change(arr, q):
    tempo = []
    number = []
    cnt = 0
    cur = '1'
    while len(number) != 8:
        if len(tempo) == 4:
            te = tempo[::-1]
            m = min(te)
            for r in range(len(te)):
                te[r] = te[r]//m
            number.append(cg.index(te[1:]))
            tempo = []
        if len(number) == 7 and len(tempo) == 3 and cur == '0':
            # print(tempo)
            m = min(tempo)
            for r in range(len(tempo)):
                tempo[r] = tempo[r] // m
            number.append(cg.index(tempo[::-1]))
            break
        if arr[q] == cur:
            cnt += 1
            q -= 1
        else:
            tempo.append(cnt)
            cnt = 1
            cur = arr[q]
            q -= 1
    # 32개가 다 저장되어 있는 상태야.
    return (number[::-1], q)


for test_case in range(1, int(input()) + 1):
    alpha = ['A', 'B', 'C', 'D', 'E', 'F']
    cg = [[2, 1, 1], [2, 2, 1], [1, 2, 2], [4, 1, 1], [1, 3, 2],
          [2, 3, 1], [1, 1, 4], [3, 1, 2], [2, 1, 3], [1, 1, 2]]
    N, M = map(int, input().split())

    s_et = set()
    for _ in range(N):
        s_et.add(input())
    t_emp = list(s_et)
    # 0이 아닌게 있는 리스를 찾아서 이진수로 변환해서 저장하기
    bin_num = []
    code = []
    for tem in t_emp:
        # 0의 개수와 같지 않으면,,,, 뭔가 저장이 되어있다는 말이니깐 이걸 이진수로 바꾸고 저장해.
        if tem.count('0') != len(tem):
            binay_num = bin(int(tem, 16))[2:]
            temporary = len(tem) * 4 - len(binay_num)
            binay_num = '0' * temporary + binay_num
            if binay_num not in bin_num:
                bin_num.append(binay_num)
    ###여기까지 하면 bin_num에는 이진수들이 저장되어 있음(해독해야하는 암호 코드의 대상들)
    ## 하나씩 빼서 개수를 세고 4개가 되면 저장해서 숫자로 바꾸면 됨.
    for b_n in bin_num:
        idx = len(b_n) - 1
        while idx != 0:
            # print(b_n)
            idx = find_1(b_n, idx)
            if idx == None:
                break
            # 호출 함수 인자(리스트,idx)
            s_code, idx = change(b_n, idx)
            if s_code not in code:
                code.append(s_code)
    total = 0
    for cod in code:
        s_1 = 0
        s_2 = 0
        for u in range(8):
            if u % 2 == 0:
                s_1 += cod[u]
            else:
                s_2 += cod[u]
        if (s_1*3+s_2) % 10 == 0:
            total += sum(cod)
    print('#{} {}'.format(test_case, total))