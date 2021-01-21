N = int(input())
data = list(map(int, input().split()))

sum = 0

for i in range(N):
    for j in range(i+1, N):
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]

for i in range(N):
    sum += data[i] * (N - i)

print(sum)