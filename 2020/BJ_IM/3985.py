L = int(input())
N = int(input())

data = [0] * (N + 1)
roll = [0] * (L + 1)
check = [0] * (N + 1)

max_want = max_val = 0

for i in range(1, N+1):
    data[i] = list(map(int, input().split()))
    want = data[i][1] - data[i][0]
    if want > max_want:
        max_idx = i
        max_want = want

print(max_idx)

for i in range(1, N+1):
    for j in range(data[i][0], data[i][1]+1):
        if roll[j] == 0:
            roll[j] = i
        else:
            continue

for idx in roll[1:]:
    if idx != 0:
        check[idx] += 1

for idx, val in enumerate(check):
    if val > max_val:
        max_val = val
        result = idx

print(result)