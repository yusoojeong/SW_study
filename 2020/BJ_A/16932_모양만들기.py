import sys
sys.stdin = open('16932_모양만들기_input.txt')
import time
start = time.time()
from collections import deque

def bfs(y, x, num):
    q = deque()
    q.append((y, x))
    data[y][x] = num
    # popleft 이후에 num을 만들면 [1, 1], [1, 1] 과 같은 구조에서 한 번 더 확인하게 된다.

    cnt = 0 # 현재 모양의 크기를 확인하기 위한 cnt
    while q:
        y, x = q.popleft()
        cnt += 1
        for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            y_idx = y + dy
            x_idx = x + dx
            if 0 <= y_idx < N and 0 <= x_idx < M and data[y_idx][x_idx] == 1:
                q.append((y_idx, x_idx))
                data[y_idx][x_idx] = num

    num_dict[num] = cnt


N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
num = 2     # data에 0과 1이 들어있으므로 2부터 만들어준다.
num_dict = {}

for y in range(N):
    for x in range(M):
        if data[y][x] == 1:
            bfs(y, x, num)
            num += 1

ans = 0
for y in range(N):
    for x in range(M):
        if data[y][x] == 0:
            stack = set()
            for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                y_idx = y + dy
                x_idx = x + dx
                if 0 <= y_idx < N and 0 <= x_idx < M and data[y_idx][x_idx]:
                    stack.add(data[y_idx][x_idx])
            sum_num = 1
            for next_num in stack:
                sum_num += num_dict[next_num]
            if sum_num > ans:
                ans = sum_num

print(ans)

print("{} seconds" .format(time.time() - start))