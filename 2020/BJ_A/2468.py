def dfs(y, x):
    visit[y][x] = 1
    
    for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        y_idx = y + dy
        x_idx = x + dx
        if 0 <= y_idx < N and 0 <= x_idx < N and data[y_idx][x_idx] and not visit[y_idx][x_idx]:
            dfs(y_idx, x_idx)


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
max = 100
result = 1

for i in range(1, max+1):
    ans = 0
    visit = [[0]*N for _ in range(N)]
    for k in range(N):
        for l in range(N):
            if data[k][l] and data[k][l] <= i:
                data[k][l] = 0

    for y in range(N):
        for x in range(N):
            if data[y][x] and not visit[y][x]:
                dfs(y, x)
                ans += 1
    if not ans:
        break    
    if ans > result:
        result = ans
print(result)
