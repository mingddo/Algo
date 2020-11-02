def preorder(v):
    print(v, end=' ')
    if L[v]:
        preorder(L[v])
    if R[v]:
        preorder(R[v])

# 중위
def in_order(v):  # v = 현재 노드
    if L[v]:
        in_order(L[v])
    print(v, end=' ')
    if R[v]:
        in_order(R[v])

# 후위
def postorder(v):
    if L[v]:
        postorder(L[v])
    if R[v]:
        postorder(R[v])
    print(v, end=' ')

V = int(input()) # 노드수, 간선수
L = [0] * (V + 1)
R = [0] * (V + 1)
# P = [0] * (V + 1)
arr = list(map(int, input().split()))
for i in range(0, len(arr), 2):
    p = arr[i]
    c = arr[i + 1]
    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c
    # P[c] = p  # 부모 정보는 필요한 경우에 저장해서 사용

print('중위 순회')
in_order(1)
print()

print('전위 순회')
preorder(1)
print()

print('후위 순회')
postorder(1)
print()