def check(y, x, d1, d2):
    global ans

    A_num = [0] * 5

    # 2, 4번 마지막 부분이 잘 안됨

    for c in range(N):
        for r in range(N):
            # 1번 구역
            if 0<= c < y and 0<= r <= x + d1 and (c + r < y + x):
                print('1', '(', c, r, ')')
                A_num[0] += A[c][r]
            # 2번 구역
            elif 0<= c <= y - d1 + d2 and x + d1 < r < N:
                print('2', '(', c, r, ')')
                A_num[1] += A[c][r]
            # 3번 구역
            elif y <= c < N and 0<= r < x + d2 and (c + d1 > r - d1):
                print('3', '(', c, r, ')')
                A_num[2] += A[c][r]
            # 4번 구역
            elif y - d1 + d2 < c < N and x + d2 <= r < N and (c + r) > (y + x + (2 * d2)):
                print('4', '(', c, r, ')')
                A_num[3] += A[c][r]
            # 5번 구역
            else:
                print('5', '(', c, r, ')')
                A_num[4] += A[c][r]

    if ans > max(A_num) - min(A_num):
        ans = max(A_num) - min(A_num)

    return



N = int(input()) # 재현시의 크기
A = [list(map(int, input().split())) for _ in range(N)] # 재현시 구역 별 인구

ans = 40000 # 매우 큰 값 (최대값 100 * N크기 20*20)

# for y in range(1, N-1): # y는 1부터 N-2까지 가능
#     for x in range(N-2): # x는 0부터 N-3까지 가능
#         for d1 in range(1, y+1): # d1은 1부터 y까지 가능
#             for d2 in range(1, N-y+2): # d2는 1부터 N-y+1까지 가능
#                 if d1 + d2 <= N-x+1:
#                     check(y, x, d1, d2)

# check(3, 1, 1, 1)
check(4, 2, 2, 1)

print(ans)


