'''
직사각형 네개의 합집합의 면적 구하기
'''

data = [[0] * 101 for _ in range(101)]
rect = [0] * 4
basic_area = 0
overlap_area = 0


for i in range(4):
    rect[i] = list(map(int, input().split()))

for i in range(4):
    r1 = rect[i][0]
    r2 = rect[i][2]
    c1 = rect[i][1]
    c2 = rect[i][3]
    for y in range(r1, r2):
        for x in range(c1, c2):
            data[y][x] += 1
            basic_area += 1

for y in range(101):
    for x in range(101):
        if data[y][x] > 1:
            overlap_area += data[y][x] - 1

result = basic_area - overlap_area
print(result)