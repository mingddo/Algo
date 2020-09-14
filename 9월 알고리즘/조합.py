arr = [1, 2, 3, 4]
N = 4
R = 2

sel = [0] * R

def combination(idx, sidx):
    if sidx == R:
        print(sel)
        return

    if idx == N:
        return

    sel[sidx] = arr[idx]
    #뽑고가고
    combination(idx+1, sidx+1)
    #안뽑고가고
    combination(idx+1, sidx)


combination(0, 0)