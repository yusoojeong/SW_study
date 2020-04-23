
from collections import deque

def bfs(y, x, cnt):
    global room_area

    q.append((y, x))
    visit[y][x] = cnt
    area = 0        # 방 넓이
    
    while q:
        y, x = q.popleft()
        area += 1
        for d in range(4): # 서 북 동 남
            y_idx = y + dy[d]
            x_idx = x + dx[d]
            if 0 <= y_idx < m and 0 <= x_idx < n and not visit[y_idx][x_idx]:
                if not (data[y][x] & (1 << d)): # 비트 연산자가 1이 되면 벽이 있다는 의미이므로 not을 붙여 못 들어오게 함
                    q.append((y_idx, x_idx))
                    visit[y_idx][x_idx] = cnt

    if room_area < area:
        room_area = area

    cnt_lst[cnt] = area


# 서 북 동 남
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

n, m = map(int, input().split())        # 가로, 세로
data = [list(map(int, input().split())) for _ in range(m)]
visit = [[0] * n for _ in range(m)]     # 방문 기록
q = deque()
cnt = 1                         # 방 번호 cnt (1부터 시작)
cnt_lst = [0] * (n * m + 1)     # 해당 방의 넓이 넣을 리스트

room_area = 0
room_ex_area = 0

for y in range(m):
    for x in range(n):
        if visit[y][x] == 0:
            bfs(y, x, cnt)
            cnt += 1
cnt -= 1

if cnt == 1:
    room_ex_area = room_area

for y in range(m):
    for x in range(n):
        for d in range(4):
            y_idx = y + dy[d]
            x_idx = x + dx[d]
            if 0 <= y_idx < m and 0 <= x_idx < n and visit[y][x] != visit[y_idx][x_idx]:
                ex_area = cnt_lst[visit[y][x]] + cnt_lst[visit[y_idx][x_idx]]
                if room_ex_area < ex_area:
                    room_ex_area = ex_area

print(cnt)
print(room_area)
print(room_ex_area)