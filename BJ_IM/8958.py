'''
연속된 O 만큼 해당 문제의 점수가 됨
"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점
'''

T = int(input())

for tc in range(1, T+1):

    data = list(input())
    score_data = []
    score = 0
    result = 0

    for ans in data:
        if ans == 'O':
            score += 1            
        else:
            score = 0
        score_data.append(score)            

    for a in score_data:
        result += a

    print("{}" .format(result))