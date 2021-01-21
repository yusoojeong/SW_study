'''
퇴사
'''

def dfs(v):

    if v > N:
        return

    print(v, data[v][0])

    for i in range(v+data[v][0], N+1):
        dfs(i)


N = int(input())
# 1부터 쓰기 위해 N+1
data = [0] * (N+1)
# T와 P를 [T, P] 형태로 받아옴
for i in range(1, N+1):
    data[i] = list(map(int, input().split()))
result = 0

# 범위를 벗어나는 값은 0으로 바꿔준다.
for i in range(N, 0, -1):
    if i + data[i][0]-1 > N:
        data[i][1] = 0

for i in range(1, N+1):
    dfs(i)

# for i in range(N, 0, -1):
#     if data[i][1]:
#         check = data[i][1] / data[i][0]
#         for j in range(i-1, 0, -1):
#             if data[j][0]-1 + j >= i:
#                 if check > (data[j][1] / data[j][0]):
#                     data[j][1] = 0
#                 elif check == (data[j][1] / data[j][0]):
#                     if data[j][1] > data[i][1]:
#                         data[i][1] = 0
#                         break
#                     else:
#                         data[j][1] = 0

# for i in range(1, N+1):
#     result += data[i][1]

# print(result)