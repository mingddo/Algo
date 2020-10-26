# import sys
# #sys.stdin.readline()
#(가로, 세로) +1+1// 끝까지 가면 (-1,+1)// (-1,-1)//(+1,-1)
w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())
# p가 가로 q가 세로
dx = [1, 1, -1, 1]
dy = [1, -1, -1, -1]
cnt = 0
d = 0
while cnt != t:
    np = p + dy[d]
    nq = q + dx[d]
    if 0<= np <= w and 0<= nq <=h:
        p, q = np, nq
        cnt += 1
    else:
        if (p,q) == (w,h) or (p,q) == (0,0):
            d = (d+2) % 4
            p = p + dy[d]
            q = q + dx[d]
            cnt += 1
        else:
            d = (d + 1) % 4
            p = p + dy[d]
            q = q + dx[d]
            cnt += 1

print('{} {}'.format(p, q))
