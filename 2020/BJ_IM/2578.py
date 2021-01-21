
def game(call):

    for i in range(5):
        for j in range(5):
            if data[i][j] == call:
                data[i][j] = 'X'
                return i, j

def bingo(y, x):

    count = 0

    if y == x:
        cnt = 0
        for i in range(5):
            if data[i][i] != 'X':
                break
            else:
                cnt += 1
        if cnt == 5:
            count += 1

    if y == 4 - x:
        cnt = 0
        for i in range(5):
            if data[i][4-i] != 'X':
                break
            else:
                cnt += 1
        if cnt == 5:
            count += 1

    cnt = 0
    for i in range(5):
        if data[y][i] != 'X':
            break
        else:
            cnt += 1
    if cnt == 5:
        count += 1

    cnt = 0
    for i in range(5):
        if data[i][x] != 'X':
            break
        else:
            cnt += 1
    if cnt == 5:
        count += 1

    return count

data = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]
calling = [0]
result = 0

for i in range(5):
    for j in range(5):
        calling.append(call[i][j])

for num in range(1, 26):
    call_num = calling[num]
    y, x = game(call_num)
    result += bingo(y, x)
    if result >= 3:
        print(num)
        break
