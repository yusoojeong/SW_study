import sys
sys.stdin = open('1003_피보나치함수_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    fibo = [0, 1] + list(0 for _ in range(N-1))

    if N > 1:
        for i in range(2, N+1):
            fibo[i] = fibo[i-1] + fibo[i-2]

    if N == 0:
        print(1, 0)
    else:
        print(fibo[N-1], fibo[N])

