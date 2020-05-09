def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        y = 0
        while y < len(board): # 범위 체크를 잘하자..
            if board[y][move-1]:
                val = board[y][move-1]
                board[y][move-1] = 0
                if stack:
                    if stack[-1] == val:
                        answer += 2
                        stack.pop()
                    else:
                        stack.append(val)
                else:
                    stack.append(val)
                break
            else:
                y += 1
    
    return answer

board = [0] + [list(map(int, input().split())) for _ in range(5)]
moves = list(map(int, input().split()))

answer = solution(board, moves)

print(answer)