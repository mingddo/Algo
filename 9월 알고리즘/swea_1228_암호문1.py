import sys

sys.stdin = open("input.txt", "r")
def f1():
    # 삽입
    global q
    i = int(q.pop(0))
    y = int(q.pop(0))
    for _ in range(y):
        pw[i:i] = [q.pop(0)]

def f2():
    #삭제
    i = int(q.pop(0))
    y = int(q.pop(0))
    for _ in range(y):
        pw.pop(i)

def f3():
    #추가
    y = int(q.pop(0))
    for _ in range(y):
        pw.append(q.pop(0))

for test_case in range(1, 11):
    N = int(input())
    pw = list(map(int,input().split()))
    M = int(input())
    q = list(input().split())
    for _ in range(M):
        pattern = q.pop(0)
        if pattern == 'I':
            #함수 f1
            f1()
        elif pattern == 'D':
            #함수 f2
            f2()
        else:
            #힘스 f3
            f3()

    result = pw[:10]
    print('#{}'.format(test_case), end=' ')
    print(*result)