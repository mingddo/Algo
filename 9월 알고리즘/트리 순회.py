# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

N = int(input())
info = list(map(int, input().split()))
tree = [0] * 100

# 두칸씩 자르고 처음칸 부모, 두번째는 자식
for i in range(0, len(info), 2):
    p = info[i]
    c = info[i + 1]

    if p not in tree:
        idx = -1
    else:
        idx = tree.index(p)

    if idx == -1:
        tree[1] = p
        tree[2] = c
    else:
        # 왼쪽자식이 비었으면 거기
        if tree[idx * 2] == 0:
            tree[idx * 2] = c
        # 아니라면 오른쪽
        else:
            tree[idx * 2 + 1] = c


# print(tree)

def preOrder(index):
    print(tree[index], end=" ")
    if tree[index * 2] != 0:
        preOrder(index * 2)
    if tree[index * 2 + 1] != 0:
        preOrder(index * 2 + 1)


def inOrder(index):
    if tree[index * 2] != 0:
        inOrder(index * 2)
    print(tree[index], end=" ")
    if tree[index * 2 + 1] != 0:
        inOrder(index * 2 + 1)


def postOrder(index):
    if tree[index * 2] != 0:
        postOrder(index * 2)
    if tree[index * 2 + 1] != 0:
        postOrder(index * 2 + 1)
    print(tree[index], end=" ")

preOrder(1)
print()
inOrder(1)
print()
postOrder(1)




# def preorder(v):
#     print(v, end=' ')
#     if L[v]:
#         preorder(L[v])
#     if R[v]:
#         preorder(R[v])
#
# # 중위
# def in_order(v):  # v = 현재 노드
#     if L[v]:
#         in_order(L[v])
#     print(v, end=' ')
#     if R[v]:
#         in_order(R[v])
#
# # 후위
# def postorder(v):
#     if L[v]:
#         postorder(L[v])
#     if R[v]:
#         postorder(R[v])
#     print(v, end=' ')
#
# V = int(input()) # 노드수, 간선수
# L = [0] * (V + 1)
# R = [0] * (V + 1)
# P = [0] * (V + 1)
# arr = list(map(int, input().split()))
# for i in range(0, len(arr), 2):
#     p = arr[i]
#     c = arr[i + 1]
#     if L[p] == 0:
#         L[p] = c
#     else:
#         R[p] = c
#     P[c] = p  # 부모 정보는 필요한 경우에 저장해서 사용
#
# print('중위 순회')
# in_order(1)
# print()
#
# print('전위 순회')
# preorder(1)
# print()
#
# print('후위 순회')
# postorder(1)
# print()