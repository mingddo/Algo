

for tc in range(1, int(input())+1):
    temp, w = input().rstrip().split()
    N = int(temp)
    word = set()
    n = len(w)
    for i in range(n):
        for j in range(i+1,n+1):
            word.add(w[i:j])


    w_list = sorted(list(word))
    print(w_list)
    print('#{} {} {}'.format(tc,w_list[N-1][0], len(w_list[N-1])))


