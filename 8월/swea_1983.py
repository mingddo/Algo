import sys


sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, k = map(int, input().split())
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    total = []
    for n in range(N):
        mid, final, hw = map(int, input().split())
        total.append(mid * 0.35 + final * 0.45 + hw * 0.20)
    k_score = total[k-1]
    total_score = sorted(total, reverse=True)
    result = total_score.index(k_score) // (N//10)
    print(f'#{test_case} {grades[result]}')