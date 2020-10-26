

s = int(input())
switch = [0]+ list(map(int,input().split()))
n = int(input())
for _ in range(n):
    a, b = map(int,input().split())
    #남자인 경우
    if a == 1:
        for i in range(1, (s//b) +1):
            switch[b*i] = (switch[b*i] + 1) % 2
    #여자인 경우
    else:
        switch[b] = (switch[b] + 1) % 2
        if b <= s//2:
            for j in range(1,b):
                if switch[b+j] == switch[b-j]:
                    switch[b+j] = (switch[b+j] + 1) % 2
                    switch[b-j] = (switch[b-j] + 1) % 2
                else:
                    break
        else:
            for j in range(1, s-b+1):
                if switch[b+j] == switch[b-j]:
                    switch[b+j] = (switch[b+j] + 1) % 2
                    switch[b-j] = (switch[b-j] + 1) % 2
                else:
                    break
switch.pop(0)
if len(switch) <= 20:
    print(* switch)
else:
    k = s // 20
    for t in range(k+1):
        print(* switch[20*t:20*(t+1)])
