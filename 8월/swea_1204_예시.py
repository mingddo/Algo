T = int(input())
 
for t in range(1, T+1):
    case = int(input())
    score_list = list(map(int, input().split()))
    counting_list = [0] * 101
 
    for score in score_list:
        counting_list[score] += 1
 
    max_idx = 0
    for idx in range(len(counting_list)):
        if counting_list[max_idx] <= counting_list[idx]:
            max_idx = idx
 
    print('#{} {}'.format(case, max_idx))