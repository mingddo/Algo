import sys
sys.stdin = open("input.txt", "r")

def postOrder(index):
    if index < N+1:
        postOrder(index * 2)
        postOrder(index * 2 + 1)
        print(index)
        calculate.append(tree[index])

for test_case in range(1, 11):
    N = int(input())
    tree = [0] * 4000
    calculate = []
    for _ in range(N):
        i = list(input().split())
        n = int(i[0])
        w = i[1]
        tree[int(n)] = w
    # print('#{}'.format(test_case), end=' ')
    postOrder(1)
    stack = []
    print(calculate) # 잘나오는지 보려고
    # 계산 시작
    for c in calculate:
        if c.isdigit():
           stack.append(int(c))
        else:
            s = c
            b = stack.pop()
            a = stack.pop()
            if s == '-':
                result = a - b
            elif s == '+':
                result = a + b
            elif s == '*':
                result = a * b
            else:
                result = a / b
            stack.append(result)
    print(stack)
    print('#{} {}'.format(test_case, int(stack[0])))
