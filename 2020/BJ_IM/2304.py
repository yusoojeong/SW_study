N = int(input())
column = [list(map(int, input().split())) for _ in range(N)]
column.sort()
max_height = 0

for i in range(N):
    if column[i][1] > max_height:
        max_height = column[i][1]
        x_idx = i

area = max_height
# max_height 왼편
for i in range(x_idx+1):
    if i == 0:
        x = column[0][0]
        y = column[0][1]
    if column[i][1] >= y:
        area += (column[i][0] - x) * y
        x = column[i][0]
        y = column[i][1]
# max_height 오른편
for i in range(N-1, x_idx-1, -1):
    if i == N-1:
        x = column[i][0]
        y = column[i][1]
    if column[i][1] >= y:
        area += (x - column[i][0]) * y
        x = column[i][0]
        y = column[i][1]

print(area)