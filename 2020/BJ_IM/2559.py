N, K = map(int, input().split())
day = list(map(int, input().split()))
max = -987654321
sum_day = 0

for i in range(N-K+1):
    sum_day = sum(day[i:i+K])
    if sum_day > max:
        max = sum_day
    
print(max)