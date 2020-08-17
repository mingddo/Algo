
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    n_numbers = list(map(int, input().split()))
    m_numbers = list(map(int, input().split()))
    result = []
    if N < M:
        for i in range(M-N+1):
            total = []
            for j in range(N):
                total.append(n_numbers[j] * m_numbers[i+j])
            result.append(sum(total))
    else:
        for i in range(N-M+1):
            total = []
            for j in range(M):
                total.append(m_numbers[j] * n_numbers[i+j])
            result.append(sum(total)) 
    print(f'#{test_case} {max(result)}')
