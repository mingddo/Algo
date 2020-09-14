import sys

sys.stdin = open("input.txt", "r")

def inOrder(index):
    if tree[index * 2] != 0:
        inOrder(index * 2)
    print(tree[index], end="")
    if tree[index * 2 + 1] != 0:
        inOrder(index * 2 + 1)


for test_case in range(1, 11):
    N = int(input())
    tree = [0] * 400
    for _ in range(N):
        i = list(input().split())
        n = int(i[0])
        w = i[1]
        tree[int(n)] = w
    print('#{}'.format(test_case), end=' ')
    inOrder(1)
    print()


