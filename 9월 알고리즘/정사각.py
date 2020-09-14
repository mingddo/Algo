import sys
sys.stdin = open("input (3).txt", "r")


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for t in range(T):
    N = int(input())
    mapp = []
    max_cnt = 0  # 결과값 / 이동한 방의 최대 개수가 저장될 변수
    room = 999999999999  # 결과값 2 / 시작 방번호가 저장될 변수
    for _ in range(N):
        mapp.append(list(map(int, input().split())))
    for x in range(N):  # 모든 x,y 탐색
        for y in range(N):
            cnt = 1
            q = [(x, y)]  # 첫 시작 방 위치 queue에 저장
            while q:  # BFS 탐색 시작 / q가 빌 때까지 q의 요소를 pop 해서 4방향 탐색 조건 만족시 append
                qq = q.pop()
                for i in range(4):
                    if 0 <= qq[0] + dx[i] < N and 0 <= qq[1] + dy[i] < N and (
                            mapp[qq[0] + dx[i]][qq[1] + dy[i]] - mapp[qq[0]][qq[1]] == 1):
                        cnt += 1
                        q.append((qq[0] + dx[i], qq[1] + dy[i]))
            if cnt > max_cnt:  # 탐색 종료 후 건너온 방의 개수가 현재까지 저장된 최대 방 건너온 개수와 비교해서 더 많다면
                max_cnt = cnt  # cnt가 이제 최대 방 건너온 개수가 됨
                room = mapp[x][y]  # room에 위치 저장
            elif cnt == max_cnt:  # 건너온 개수가 같다면
                if mapp[x][y] < room:  # 저장된 방 번호와 비교해 작은지 판단
                    room = mapp[x][y]

    print('#{} {} {}'.format(t + 1, room, max_cnt))