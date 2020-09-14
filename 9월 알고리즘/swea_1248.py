import sys
#sys.stdin = open("input.txt", "r")
def f(id):
    global cnt
    cnt += 1
    if left[id]:
        f(left[id])
    if right[id]:
        f(right[id])


for test_case in range(1, int(input())+1):
    V, E, find_1, find_2 = map(int,input().split())
    left = [0]* (V+1)
    right = [0]* (V+1)
    parents = [0]* (V+1)
    arr = list(map(int,input().split()))
    for i in range(E):
        a, b = arr[2*i], arr[2*i+1]
        if not left[a]:
            left[a] = b
        else:
            right[a] = b
        parents[b] = a
    # 여기까지  노드 정보 받아서 다 처리 find_1의 조상 정보 찾아서 저장하기.
    find_1_parents = []
    idx = find_1
    while parents[idx] !=0:
        find_1_parents.append(parents[idx])
        idx = parents[idx]
    #find 2 정리하기
    index = find_2
    find_parents = -1
    while parents[index] != 0:
        find_parents = parents[index]
        index = find_parents
        if find_parents in find_1_parents:
            break
    #공통 조상 다 찾음
    #공통 조상에 연결된 노드의 개수 찾기.
    cnt = 0
    f(find_parents)
    #print(find_parents)
    print(cnt)
    print('#{} {} {}'.format(test_case, find_parents, cnt))