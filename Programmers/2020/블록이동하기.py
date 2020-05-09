from collections import deque
def solution(board):
    answer = 0
    N = len(board) - 1  # 도착 위치의 좌표 [N, N]
    q = deque()
    # [y, x]로 좌표값 받기
    head = [0, 1]
    tail = [0, 0]
    while True:
        if head == [N, N] or tail = [N, N]:
            break
        # 머리와 꼬리가 가로로 있을 때 -> y 좌표가 같을 때
        if head[0] == tail[0]:
            for dy, dx in []

        # 머리와 꼬리가 세로로 있을 때 -> x 좌표가 같을 때
        else:
    return answer