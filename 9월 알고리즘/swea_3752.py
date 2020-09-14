import sys

#sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N = int(input())
    points = list(map(int,input().split()))
    visited = [0] * (sum(points)+1)
    visited[0] = 1
    result = [0]
    for p in points:
        #뒤에 슬라이싱 안하니깐 result 값이 실시간으로 변함.
        result_now = result[:]
        for r in result_now:
            if not visited[p + r]:
                visited[p + r] = 1
                result.append(p + r)
    print(result)
    print('#{} {}'.format(test_case,len(result)))



# 트리로 푸는 방법


for test_case in range(1, int(input()) + 1):
    N = int(input())
    points = list(map(int,input().split()))
    tree = [0]* (2**10)
    tree[1] = 0
    for p in points:
        for t in tree[1:]:
            if t !=0
