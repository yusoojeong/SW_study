
N, H = map(int, input().split())
data = [0] * H

for x in range(1, N+1):
    n = int(input())
    while n > 0:
        if x % 2:
            data[n-1] += 1
        else:
            data[H-n] += 1
        n -= 1

ans = min(data)
print(ans, data.count(ans))