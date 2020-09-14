arr = [1,2,3]
N = 3
sel = [0] * N
visited = [0] * N

def perm(idx):
    if idx == N:
        print(sel)
        return

    for i in range(N):
        if not visited[i]:
            sel[idx] = arr[i]
            visited[i] = 1
            perm((idx+1))
            visited[i] = 0
perm(0)
