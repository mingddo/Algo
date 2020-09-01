import sys
#sys.stdin = open("input.txt", "r")
for tc in range(1, 11):
    n = input()
    stack = []
    pairs = list(input())
    left = ['[', '{', '<', '(']
    right = [']', '}', '>', ')']
    result = 1
    for p in pairs:
        if p in left:
            stack.append(p)
        elif p in right:
            if len(stack) == 0:
                result = 0
                break
            elif left.index(stack[-1]) != right.index(p):
                result = 0
                break
            else: stack.pop()

    if len(stack) > 0:
        result = 0

    print('#{} {}'.format(tc, result))

