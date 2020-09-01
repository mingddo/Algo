arr = [1, 2, 3]
A = []
bits = [0] * 3  # 원소의 개수만큼


def subset(k, n, cur_sum):
    if k == n:
        print(cur_sum)
        for i in range(n):
            if bits[i]: print(arr[i], end='')
        print('\n-------------------------')
        return
    else:
        bits[k] = 1
        A.append(arr[k])
        subset(k + 1, n, cur_sum + arr[k])
        A.pop

        bits[k] = 0
        subset(k + 1, n, cur_sum)


subset(0, 3, 0)