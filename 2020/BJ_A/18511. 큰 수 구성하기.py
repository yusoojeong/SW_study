import sys
sys.stdin = open("18511. 큰 수 구성하기_input.txt")

T = int(input())

for tc in range(1, T+1):

    N, K = input().split()
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    ans = ''

    i = j = 0
    flag = False
    while i < len(N):
        num = int(N[i])
        if flag == True:
            ans += str(data[0]) * (len(N) - i)
            break

        if int(N[i]) in data:
            ans += N[i]
        else:

            ans += str(data[j])
            if data[j] < num:
                flag = True
            i += 1
            j = 0

    print(ans)



