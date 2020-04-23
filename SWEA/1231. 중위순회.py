import sys
sys.stdin = open("1231. 중위순회_input.txt")

def dfs(v):

    if v >= len(data):
        return

    dfs(v * 2)
    print(data[v], end='')
    dfs((v * 2) + 1)


for tc in range(1, 10+1):
    N = int(input())
    ans = ''
    data = [0] * (N + 1) # 1번부터 시작

    for _ in range(N):
        alpha = list((input().split()))
        data[int(alpha[0])] = alpha[1]

    print("#{}" .format(tc), end=' ')
    dfs(1)
    print()