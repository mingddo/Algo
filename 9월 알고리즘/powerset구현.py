li = [1,2,3,4,5,6,7,8,9,10]
bits = [0]*len(li)
A = []
result = []
def powerset(k,n,cnt):
    if k == n:
        if cnt == 10:
            print(A)


    else:
        bits[k] = 1
        A.append(li[k])
        powerset(k+1, n , cnt+ li[k])
        A.pop()

        bits[k] = 0
        powerset(k + 1, n, cnt)


powerset(0, len(li), 0)
