

Width, Height = map(int, input().split())
cut = int(input())
data = [list(map(int, input().split())) for _ in range(cut)]
# 자르는 위치 저장을 위한 리스트
x_cut = [0]
y_cut = [0]
max = 0

for i in range(cut):
    if data[i][0] == 0: # 가로로 자르는 건 세로 길이를 줄인다.
        y_cut.append(data[i][1])
    else:
        x_cut.append(data[i][1]) # 세로로 자르는 건 가로 길이를 줄인다.
x_cut.append(Width)
y_cut.append(Height)

x_cut.sort()
y_cut.sort()

for i in range(1, len(x_cut)):
    x_length = x_cut[i] - x_cut[i-1]
    for j in range(1, len(y_cut)):
        y_length = y_cut[j] - y_cut[j-1]
        area = x_length * y_length
        if max < area:
            max = area

print(max)