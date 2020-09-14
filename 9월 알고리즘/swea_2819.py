#bfs로 해서 진행하고 뒤에 [x좌표, y좌표, cnt, num=''] 이걸 Q에 저장. 그리고 처음 팝할 때 cnt가 6이면 while 문 탈출하고 q에 남아있는 애들을 pop하면서 num을 result에 저장하기.
import sys

sys.stdin = open("input(1).txt", "r")

def bfs(x,y):
    global numbers
    q = []
    q.append([x,y,0,arr[x][y]])
    while len(q):
        dx, dy, cnt, num = q.pop(0)
        if cnt == 6:
            numbers.add(num)
        else:
            for d in range(4):
                n_x = dx + d_x[d]
                n_y = dy + d_y[d]
                if 0 <= n_x < 4 and 0 <= n_y < 4:
                    q.append([n_x, n_y, cnt+1, num+arr[n_x][n_y]])


for test_case in range(1, int(input()) + 1):
    arr = [list(input().split()) for _ in range(4)]
    numbers = set()
    d_x = [0, 0, -1, 1]
    d_y = [-1, 1, 0, 0]
    for a in range(4):
        for b in range(4):
            bfs(a,b)

    print('#{} {}'.format(test_case,len(numbers)))