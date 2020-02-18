'''
연구소
'''

def isnotwall(y, x):

    if y < 0 or y >= N:
        return False
    if x < 0 or x >= N:
        return False
    if data[y][x] == 1:
        return False
    if data[y][x] == 0:
        return True


dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

for y in range(N):
    for x in range(M):
        if data[y][x] == 2:
            for d in range(4):
                y_idx = y + dy[d]
                x_idx = x + dx[d]
                if isnotwall(y_idx, x_idx):
                    

