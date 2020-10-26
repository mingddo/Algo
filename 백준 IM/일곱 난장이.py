
seven = []
for _ in range(9):
    seven.append(int(input()))
seven = sorted(seven)
e1 = 0
e2 = 0
for i in range(len(seven)):
    if sum(seven) - e1 - e2 == 100:
        break
    for j in range(len(seven)):
        if j != i:
            if sum(seven) - seven[i] - seven[j] == 100:
                e1 = seven[i]
                e2 = seven[j]
                break

n_seven = []
for s in seven:
    if s == e1:
        continue
    if s == e2:
        continue
    else:
        n_seven.append(s)

for ns in n_seven:
    print(ns)
