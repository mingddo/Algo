import sys

#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = int(input())
    scores = list(map(int, input().split()))
    max_score = 0
    frq_score = 0
    for score in scores: 
        if frq_score != score:
            if scores.count(score) > max_score:
                max_score = scores.count(score)
                frq_score = score
            elif scores.count(score) == max_score:
                if frq_score < score:
                    frq_score = score
    print(f'#{tc} {frq_score}')
