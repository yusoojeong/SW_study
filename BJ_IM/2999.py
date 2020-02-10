data = list(map(str, input()))
RC = len(data)
result = ""
for num in range(RC//2 - 1,1,-1):
    if not RC % num:
        r = num
        c = RC // num
        break

data_list = [[0 for _ in range(c)] for _ in range(r)]

for j in range(c):
    for i in range(r):
        data_list[i][j] = data.pop(0)

for i in range(r):
    for j in range(c):
        result += data_list[i][j]

print(result)
