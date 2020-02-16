'''
https://www.acmicpc.net/problem/3190
시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

★ 칸은 1칸씩만 이동한다. 몸길이도 하나만 줄어들고 사과를 먹었을시 몸통의 길이가 늘기 때문에 꼬리를 움직이지 않는 것이다.
시뮬레이션은 조건에 매우 유의해야한다.

6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

'''
def iswall(y, x):

    if y < 1 or y > N:
        return True
    if x < 1 or x > N:
        return True
    if data[y][x] == 1:
        return True
    return False

def snake(y, x):
    # 방향 초기화
    d = 0
    sec = 0
    data[y][x] = 1
    stack = [y, x]

    while True:
        sec += 1
        y += dy[d]
        x += dx[d]
        stack.append(y)
        stack.append(x)
        if iswall(y, x):
            return sec
        if data[y][x] != 5:
            y_idx = stack.pop(0)
            x_idx = stack.pop(0)
            data[y_idx][x_idx] = 0
        data[y][x] = 1
        if sec in dir_dict.keys():
            if dir_dict[sec] == 'D':
                d += 1
                if d == 4: d = 0
            else:
                d -= 1
                if d == -1: d = 3


# 우 하 좌 상 (시계방향)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

N = int(input()) # 보드 크기
data = [[0] * (N + 1) for _ in range(N + 1)] # 1부터 시작
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
dir_list = [list(input().split()) for _ in range(L)]
dir_dict = {}

for i in range(L):
    dir_dict[int(dir_list[i][0])] = dir_list[i][1]

for i in range(K):
    data[apple[i][0]][apple[i][1]] = 5

ans = snake(1, 1)

print(ans)


