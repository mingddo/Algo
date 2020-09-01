import sys

sys.stdin = open("input (2).txt", "r")

for tc in range(1, 11):
    N = int(input())
    cal = list(input())
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    push = ['', '+', '*', '(']
    in_operate = ['(', '+', '*']
    operater = []
    stack = []
    for c in cal:
        if c in numbers:
            stack.append(c)
        else:
            if len(operater) == 0:
                operater.append(c)
            elif len(operater) != 0:
                if c == ')':
                    while operater[-1] != '(':
                        stack.append(operater.pop())
                    operater.pop()
                elif push.index(c) > in_operate.index(operater[-1]):
                    operater.append(c)
                else:
                    while push.index(c) <= in_operate.index(operater[-1]):
                        stack.append(operater.pop())
                    operater.append(c)

    # print(stack)
    # 계산하기
    result = []
    for s in stack:
        if s in numbers:
            result.append(int(s))
        else:
            b = result.pop()
            a = result.pop()
            if s == '*':
                result.append(a * b)
            elif s == '+':
                result.append(a + b)

    print('#{} {}'.format(tc, result[0]))




