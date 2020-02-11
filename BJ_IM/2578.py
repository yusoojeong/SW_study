def bingo():

    for idx, val in enumerate(call):
        a = 0
        for y in range(5):
            for x in range(5):
                if data[y][x] == val:
                    data[y][x] = 0
                    a = 1
                    if check(y, x):
                        return idx+1
                    break
            if a == 1:
                break
            
def check(y, x):
    x_cnt = y_cnt = yx_cnt = 0
    # 가로 확인
    for j in range(5):
        if data[y][j] != 0:
            break
        else: 
            x_cnt += 1
    if x_cnt == 5:
        cnt[0] += 1
    # 세로 확인
    for i in range(5):
        if data[i][x] != 0:
            break
        else:
            y_cnt += 1
    if y_cnt == 5:
        cnt[1] += 1

    # 대각선 확인
    if y == x:
        for i in range(5):
            if data[i][i] != 0:
                break
            else:
                yx_cnt += 1
    elif y + x == 4:
        for i in range(5):
            if data[i][4-i] != 0:
                break
            else:
                yx_cnt += 1  
    if yx_cnt == 5:
        cnt[2] += 1

    if cnt[0] + cnt[1] + cnt[2] >= 3:
        return True
    else:
        return False



data = [list(map(int, input().split())) for _ in range(5)]
data2 = [list(map(int, input().split())) for _ in range(5)]

call = []
cnt = [0, 0, 0]

for i in range(5):
    for j in range(5):
        call.append(data2[i][j])

print(bingo())



