def solution(key, lock):
    answer = False
    n = len(lock)

    # lock 배열 숫자 뒤집기 -> key와 겹치는 지 확인
    for y in range(n):
        for x in range(n):
            if lock[y][x] == 1:
                lock[y][x] = 0
            else:
                lock[y][x] = 1
    # 2차원 key 배열 회전

    # 2차원 key 배열 상하좌우 이동

    return answer