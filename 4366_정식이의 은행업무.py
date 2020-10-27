
import sys

#sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input()) + 1):
    num2 = list(input())
    num3 = list(input())
    li_2 = []
    li_3 = []
    result = 0
    #2진수 변환
    for i in range(len(num2)):
        if num2[i] == '0':
            num2[i] = '1'
            li_2.append(int("".join(num2),2))
            num2[i] = '0'
        else:
            num2[i] = '0'
            li_2.append(int("".join(num2), 2))
            num2[i] = '1'

    # 3진수 변환
    for j in range(len(num3)):
        if num3[j] == '0':
            num3[j] = '1'
            li_3.append(int("".join(num3),3))
            num3[j] = '2'
            li_3.append(int("".join(num3), 3))
            num3[j] = '0'

        elif num3[j] == '1':
            num3[j] = '0'
            li_3.append(int("".join(num3), 3))
            num3[j] = '1'
            li_3.append(int("".join(num3), 3))
            num3[j] = '1'
        else:
            num3[j] = '0'
            li_3.append(int("".join(num3), 3))
            num3[j] = '1'
            li_3.append(int("".join(num3), 3))
            num3[j] = '2'
    for k in li_2:
        if k in li_3:
            result = k
            break

    print('#{} {}'.format(test_case, result))

