
N, M, L = map(int, input().split())
data = [0] * (N+1)

player = 1
count = 0

while True:

    data[player] += 1
    if data[player] == M:
        break

    if data[player] % 2:
        player += L
        if player > N:
            player -= N
    else:
        player -= L
        if player < 1:
            player = N + player    
    count += 1

print(count)