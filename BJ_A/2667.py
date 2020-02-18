import sys
sys.stdin = open("2667_input.txt")

def dfs(y, x):

    global count
    count += 1
    visit[y][x] = 1

    for d in range(4):
        y_idx = y + dy[d]
        x_idx = x + dx[d]
        if 0 <= y_idx < N and 0 <= x_idx < N and data[y_idx][x_idx] == data[y][x] and not visit[y_idx][x_idx]:
            dfs(y_idx, x_idx)


dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

N = int(input())
data = [list(map(int, input())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
# 단지내 집의 수 받아올 변수 값
result = []

for y in range(N):
    for x in range(N):
        count = 0
        if data[y][x] and not visit[y][x]:
            dfs(y, x)
            result.append(count)

result.sort()

print(len(result))

for i in range(len(result)):
    print(result[i])