import sys
sys.stdin = open("말이 되고픈 원숭이_input.txt")
#1 4
#2 6
#3 -1
#4 1
#5 1
#6 8
#7 -1
#8 10
#9 4
#10 8

from collections import deque

def check():
    global ans
    visit = [[0] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            visit[y][x] = [K, W*H]

    visit[0][0] = [K, 0]
    while q:
        y, x = q.popleft()
        k, cnt = visit[y][x]
        if y == H-1 and x == W-1:
            ans = cnt
            return
        # for dy, dx in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        for dy, dx in [[0, 1], [1, 0]]:
            y_idx = y + dy
            x_idx = x + dx
            if 0 <= y_idx < H and 0 <= x_idx < W and data[y_idx][x_idx] == 0 and (visit[y_idx][x_idx][0] < k or visit[y_idx][x_idx][1] > cnt+1) :
                visit[y_idx][x_idx] = [k, cnt+1]
                q.append((y_idx, x_idx))
        if k:
            # for sy, sx in [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]:
            for sy, sx in [[1, 2], [2, 1]]:
                y_idx = y + sy
                x_idx = x + sx
                if 0 <= y_idx < H and 0 <= x_idx < W and data[y_idx][x_idx] == 0 and (visit[y_idx][x_idx][0] < k or visit[y_idx][x_idx][1] > cnt+1) :
                    visit[y_idx][x_idx] = [k-1, cnt + 1]
                    q.append((y_idx, x_idx))

T = int(input())
for tc in range(1, T+1):

    K = int(input())
    W, H = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(H)]
    ans = -1

    q = deque()
    if data[0][0] == 0 and data[H - 1][W - 1] == 0:
        q.append((0, 0))
        check()

    print("#{} {}" .format(tc, ans))

# K = int(input())
# W, H = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(H)]
# ans = -1
#
# q = deque()
# if data[0][0] == 0 and data[H-1][W-1] == 0:
#     q.append((0, 0))
#     check()
#
# print(ans)