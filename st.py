import sys

def count_number(a):
    for b in a:
        if a.count(b) > 1:
            return 0
        else:
            return 1



T = int(input())

for test_case in range(1, T + 1):
    numbers = [list(map(int, input().split()))for i in range(9)]
total = []
# 가로 검색하는  While문
results_h = []
for num_list in numbers:
    results_h.append(count_number(num_list))
for result in results_h:
    if result == 0:
        total.append(0)
    else:
        total.append(1)

#세로 검색하기
result_v = []
for i in range(9):
    results_list = []
    for number in numbers:
        results_list.append(number[i])
        if number[i] in results_list:
            result_v.append(0)
        else:
            result_v.append(1)
for re in result_v:
    if re ==0:
        total.append(0)
    else:
        total.append(1)

# 박스검색하기
# 세로의 범위 0, 3, 6 이 시작.
for x in range(3):
    for y in range(3):
        for j in range(3):
            
    
    
        

    


    

