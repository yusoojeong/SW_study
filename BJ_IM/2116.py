
dice = ["A", "B", "C", "D", "E", "F"]
dice_idx = {"A": 5, "B": 3, "C": 4, "D": 1, "E": 2, "F": 0}

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
max = 0

# 아래와 위를 결정
for i in range(6):
    sum = 0
    down = data[0][i]
    up = data[0][dice_idx[dice[i]]]
    # 아래와 위가 아닌 수 중 가장 큰 값
    for num in range(6,0,-1):
        if num != down and num != up:
            sum += num
            break
    # 다음 층
    for floar in range(1, N):
        for j in range(6):
            # 아래 층의 위와 같은 값을 찾아서 아래를 찾고 반대면의 위를 찾음
            if data[floar][j] == up:
                down = data[floar][j]
                up = data[floar][dice_idx[dice[j]]]
                # 아래와 위가 아닌 수 중 가장 큰 값
                for num in range(6,0,-1):
                    if num != down and num != up:
                        sum += num
                        break
                break
    if sum > max:
        max = sum

print(max)

