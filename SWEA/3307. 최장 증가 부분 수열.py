import sys
sys.stdin = open("3307_input.txt")

def check(length, i):

    global ans

    if length + (N-i-1) < ans:
        return
    if i == N-1:
        if length > ans:
            ans = length
        return
    if data[i] <= data[i+1]:
        check(length+1, i+1)
    check(length, i+1)


T = int(input())

for tc in range(1, T+1):

    N = int(input())
    data = list(map(int, input().split()))
    ans = 0
    case = []
    case_dict = {}
    max_idx = 0

    for i in range(N):
        a = []
        for j in range(i+1, N):
            if data[i] <= data[j]:
                a.append(j)
        case.append(a)
        case_dict[i] = len(a)
        if case_dict[i] > case_dict[max_idx]:
            max_idx = i

    print(case)
    print(case_dict)
    print(max_idx)

    while True:
        if case_dict[max_idx] == 0:
            ans += 1
            break

        max_len = 0
        for idx in case[max_idx]:
            print(idx)
            if case_dict[idx] > case_dict[case[max_idx][max_len]]:
                max_len = idx
                ans += 1
        max_idx = max_len

    print("#{} {}" .format(tc, ans))