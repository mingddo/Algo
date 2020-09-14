def makeTree(n):
    global count
    # 배열이니까 배열크기 넘어가지 않도록
    if n <= N:
        # 왼쪽노드는 현재 인덱스의 2배
        makeTree(n * 2)
        # 더이상 못가면 값넣기
        tree[n] = count
        # 값 넣었으면 증가시키기
        count += 1
        # 우측 노드는 인덱스 2배 + 1
        makeTree(n * 2 + 1)


for t in range(int(input())):
    N = int(input())
    tree = [0 for i in range(N + 1)]
    count = 1
    makeTree(1)
    print(tree)