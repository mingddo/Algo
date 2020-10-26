
import sys

sys.stdin = open("input.txt", "r")
#회전하는 함수 만들기. 인접하는 곳을 먼저 확인 한 후 돌려야 할 자석을 확인
#돌려야하는 자석을 해당 방향으로 돌리고 return(mgnt)
def turn(a):
    visited = [0]*4
    global idx
    # 돌려야하는 자석을 검사.
    # 0부터 시작하니깐 -1 해줌. x는 톱니바퀴 번호, y는 회전 방향
    p, y = a[0]-1, a[1]

    stack = [(p,-y)]
    plus = [[p,-y]]
    while stack:
        (x , f) = stack.pop()
        y = -f
        visited[x] = 1
        if x == 1 or x == 2:
            if mgnt[x][idx[x][0]] != mgnt[x-1][idx[x-1][-1]] and visited[x-1] == 0:
                stack.append((x-1, y))
                plus.append([x - 1, y])
                visited[x-1] = 1

            if mgnt[x][idx[x][-1]] != mgnt[x+1][idx[x+1][0]] and visited[x+1] == 0:
                stack.append((x + 1, y))
                plus.append([x + 1, y])
                visited [x+1] = 1

        elif x == 0:
            if mgnt[x][idx[x][-1]] != mgnt[x+1][idx[x+1][0]] and visited[x+1] == 0:
                stack.append((x + 1,y))
                plus.append([x+1, y])
                visited[x + 1] = 1

        else:
            if mgnt[x][idx[x][0]] != mgnt[x-1][idx[x-1][-1]] and visited[x-1] == 0:
                stack.append((x - 1,y))
                plus.append([x-1, y])
                visited[x - 1] = 1

    for pl in plus:
        m_x, m_y = pl[0], pl[1]
        for d in range(3):
            idx[m_x][d] = (idx[m_x][d] + m_y) % 8

for test_case in range(1, int(input()) + 1):
    k = int(input())
    # 자석들의 정보를 저장 ( 빨간 화살표부터 시계방향으로 )
    mgnt = [list(map(int, input().split())) for _ in range(4)]
    rotate = [list(map(int, input().split())) for _ in range(k)]
    # 시계방향이면 (-1하고 % 8) 반시계 방향이면 (+1 하고 %8) 최종 idx 가운데 빨간 화살표
    idx = [[6, 0, 2], [6, 0, 2], [6, 0, 2], [6, 0, 2]]
    for r in rotate:
        turn(r)
    total = 0
    for j in range(4):
        total += mgnt[j][idx[j][1]] * (2 ** j)

    print('#{} {}'.format(test_case, total))

