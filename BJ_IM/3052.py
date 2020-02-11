
data = {}

for _ in range(10):
    number = int(input())
    a = number % 42
    if a in data.keys():
        data[a] += 1
    else:
        data[a] = 1

print(len(data))
