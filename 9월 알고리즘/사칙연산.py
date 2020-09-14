import sys
sys.stdin = open("input.txt", "r")
#제일 밑에 있는 부모를 찾아서 자식들 연산 후 그 결과 값을 부모에 저장하는 방식. 최종 결과는 최상단 부모인, 루트에 저장됨.
def calculate(index):
    if tree[index][2] == 0: #오른쪽 자식이 없으면 리턴
        return
    else:
        c = tree[index][0]
        x = int(tree[index][1])
        y = int(tree[index][2])
        calculate(x)
        calculate(y)
        if c == '+':
            result = int(tree[x][0]) + int(tree[y][0])
        elif c == '-':
            result = int(tree[x][0]) - int(tree[y][0])
        if c == '*':
            result = int(tree[x][0]) * int(tree[y][0])
        if c == '/':
            result = int(tree[x][0]) / int(tree[y][0])
        tree[index][0] = result
        tree[index][1] = 0
        tree[index][2] = 0

for test_case in range(1, 11):
    N = int(input())
    # Tree만들기 값, 왼쪽자식, 오른쪽 자식 저장하는 tree 만들기
    tree = [[0] * 3 for _ in range(N+1)]
    for a in range(N):
        temp = input().split()
        l = len(temp)
        for b in range(l-1):
            tree[a+1][b] = temp[b+1]
    calculate(1)
    last_result = int(tree[1][0])
    print('#{} {}'.format(test_case, last_result))