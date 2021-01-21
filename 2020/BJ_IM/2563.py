'''
색종이 붙은 검은 영역의 넓이를 구하기
(겹치는 영역 존재)
'''

data = [[0] * 100 for _ in range(100)]
pieces = int(input())
paper = [list(map(int, input().split())) for _ in range(pieces)]

# 색종이 수 만큼의 넓이 - 겹치는 넓이
basic_area = 10 * 10 * pieces
overlap_data = [0] * (pieces+1)
overlap_area = 0

for i in range(pieces):
    y_idx = paper[i][1]
    x_idx = paper[i][0]
    for y in range(y_idx, y_idx+10):
        for x in range(x_idx, x_idx+10):
            data[y][x] += 1

# 몇 번 겹치는지 카운팅
for y in range(100):
    for x in range(100):
        if data[y][x] == 0:
            continue
        else:
            overlap_data[data[y][x]] += 1

# 겹친 횟수 - 1(1번은 색종이 하나) 만큼 곱해서 overlap_area에 넣는다.
for i in range(2,pieces+1):
    overlap_area += overlap_data[i] * (i-1)

result = basic_area - overlap_area
print(result)