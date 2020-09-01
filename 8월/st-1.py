import sys
# set (중복되지 않는 값)
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    numbers = [list(map(int, input().split()))for i in range(9)]
    arr = set(range(1,10))
    result = 1
    # 가로 비교하기

    for number in numbers:
        hor = set()
        for n in number:
            hor.add(n)
        if hor != arr:
            result = 0
    
    # 세로 비교하기
    for x in range(9):
        ver = set()
        for y in range(9):
            ver.add(numbers[y][x])
        if ver != arr:
            result = 0

    
    start = [0, 3, 6]
    for s_a in start:
        for s_b in start:
            box = set()
            for a in range(3):
                for b in range(3):
                    box.add(numbers[a + s_b][b + s_a])
            if box != arr:
                result = 0
        
    
    print(f'#{test_case} {result}')
