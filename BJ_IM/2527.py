'''
직사각형 2차원 격자공간.
왼쪽 아래 꼭짓점 좌표 x, y
오른쪽 위 꼭짓점 좌표 p, q

3 10 50 60 100 100 200 300
45 50 600 600 400 450 500 543
11 120 120 230 50 40 60 440
35 56 67 90 67 80 500 600
'''

def check():

    ans = 0

    for y in range(rect[1], max_x+1):
        for x in range(rect[0], max_y+1):
            if data[y][x] == 2:
                ans += 1
                if data[y+1][x] == 2:
                    ans += 1
                if data[y][x+1] == 2:
                    ans += 1
                return ans
    return ans

for _ in range(4):
    rect = list(map(int, input().split()))
    # max_x = max_y = 0

    # for i in range(0, len(rect), 2):
    #     if rect[i] > max_x:
    #         max_x = rect[i]
    #     if rect[i+1] > max_y:
    #         max_y = rect[i+1]
            
    data = [[0] * (5000) for _ in range(5000)]

    # 1번 직사각형
    for y in range(rect[1], rect[3]+1):
        for x in range(rect[0], rect[2]+1):
            data[y][x] += 1
    # 2번 직사각형    
    for y in range(rect[5], rect[7]+1):
        for x in range(rect[4], rect[6]+1):
            data[y][x] += 1

    ans = check()
    if ans == 0:
        print("d")
    elif ans == 1:
        print("c")
    elif ans == 2:
        print("b")
    else:
        print("a")
