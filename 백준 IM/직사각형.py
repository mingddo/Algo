result = []
for _ in range(4):
    sq = list(map(int,input().split()))
    A = sq[0:4]
    B = sq[4:]
    #a가출력되는 경우
    if A[0] <= B[0] <= A[2] and A[0] <= B[2] <= A[2]:
        result.append('a')
    elif

