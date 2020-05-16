'''
야구
1번 선수를 4번 타자로 결정함
다른 선수 타순 결정
이닝 당 결과 알고 있음
가장 많은 득점을 하는 타순 찾고 득점을 구하기
'''
import sys
import time
input = sys.stdin.readline
start_time = time.time() # 시작 시간 저장

from itertools import permutations

def play_order():
    
    max_score = 0

    player = [i for i in range(2, 10)]
    
    # 전체 순열을 돌렸음..
    for order in list(permutations(player,8)):
        player_order = [i for i in order]
        score = game(player_order)
        max_score = max(max_score, score)

    return max_score
    

def game(order, score=0):
    order.insert(3, 1)

    turn = 0 # order[0]번 선수부터 시작

    for n in range(inning):         # inning 수만큼 반복한다
        play = 0                    # 1, 2, 3루 상황을 받아오기 위한 play
        out_cnt = 0                 # 아웃 카운트

        while out_cnt < 3:
            turn %= 9               # 9명이 로테이션
            player = order[turn]    # 해당 turn에 정해진 선수를 받아온다
            result = data[n][player]# 해당 선수의 이번 이닝의 결과를 가져온다

            # 아웃이 아닌 경우
            if result:
                play += 1               # 새로운 주자를 타석에 넣음
                play = play << result   # 새 주자가 친 결과만큼 밀어준다
                for i in range(4, 8):   # 16이상의 값이 있다면 홈에 들어왔으므로 점수로 바꿔준다.
                    if play & (1 << i):
                        score += 1
                        play -= 1 << i

            # 아웃
            else:
                out_cnt += 1

            turn += 1       # 다음 선수

    return score

# game score 계산
# def game2(order, score=0):

#     turn = 0 # order[0]번 선수부터 시작

#     for n in range(inning):         # inning 수만큼 반복한다
#         play = [0, 0, 0]            # 1, 2, 3루 상황을 받아오기 위한 play
#         out_cnt = 0                 # 아웃 카운트

#         while out_cnt < 3:
#             turn %= 9               # 9명이 로테이션
#             player = order[turn]    # 해당 turn에 정해진 선수를 받아온다
#             result = data[n][player]# 해당 선수의 이번 이닝의 결과를 가져온다

#             # 홈런인 경우
#             if result == 4:
#                 score += sum(play) + 1
#                 play = [0, 0, 0]

#             # 3루타인 경우
#             elif result == 3:
#                 score += sum(play)
#                 play = [0, 0, 1]
            
#             # 2루타인 경우
#             elif result == 2:
#                 score += sum(play[1:])
#                 play = [0, 1] + play[0]
            
#             # 1루타인 경우
#             elif result == 1:
#                 score += play[2]
#                 play = [1] + play[:2]

#             # 아웃
#             else:
#                 out_cnt += 1

#             turn += 1       # 다음 선수

#     return score


inning = int(input()) # 이닝 수
data = [[0] + list(map(int, input().split())) for _ in range(inning)] # 이닝 별 결과
# 선수와 맞추기 위해 [0] 삽입

ans = play_order()
print(ans)
print(time.time() - start_time, 'seconds')


