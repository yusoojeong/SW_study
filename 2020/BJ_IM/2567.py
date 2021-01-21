'''
https://www.acmicpc.net/problem/2567
색종이 둘레
'''

data = [[0] * 100 for _ in range(100)]
pieces = int(input())
paper = [list(map(int, input().split())) for _ in range(pieces)]

# 색종이 수 만큼의 둘레 - 겹치는 둘레
basic_area = 4 * 10 * pieces

for i in range(pieces):
    y_idx = paper[i][1]
    x_idx = paper[i][0]
    for y in range(y_idx, y_idx+10):
        for x in range(x_idx, x_idx+10):
            data[y][x] += 1

