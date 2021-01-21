# 재성이 코드

N, M, V = map(int, input().split())
st = [0] * M
ed = [0] * M
ij = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    st[i], ed[i] = map(int, input().split())
    ij[st[i]][ed[i]] = 1
    ij[ed[i]][st[i]] = 1
for j in range(N+1):
    print(ij[j])
print()

stack = []
stack.append(V)
i = 0
visited = [0] * (N+1)
visited[V] = 1

# print(stack)
while True:
    for c in range(1,N+1):
        if ij[stack[i]][c] == 1 and visited[c] == 0:
            visited[c] = 1
            stack.append(c)
            i += 1
            # print(stack)
            break
    else:
        i -= 1

    if i == -1:
        break

for j in range(len(stack)):
    print(stack[j], end = " ")
print()

que = []
que.append(V)
visited_bfs = [0] * (N+1)
visited_bfs[V] = 1
result = []
while True:
    for c in range(1, N+1):
        if ij[que[0]][c] == 1 and visited_bfs[c] == 0:
            visited_bfs[c] = 1
            que.append(c)
    # print(que)
    result.append(que.pop(0))

    if len(que) == 0:
        break

for k in range(len(result)):
    print(result[k], end=" ")
print()