# 숫자 키패드 누르기
# 20 / 20
def solution(numbers, hand):
    answer = ''
    now_l = 10  # '*'
    now_r = 12  # '#'

    for number in numbers:
        if number % 3 == 1:  # 1, 4, 7
            answer += 'L'
            now_l = number
        elif number % 3 == 0 and number != 0:  # 3, 6, 9
            answer += 'R'
            now_r = number
        else:  # 0, 2, 5, 8
            if number == 0:
                number = 11
            q = [abs(number - now_l), abs(now_r - number)]
            for i in range(2):
                if q[i] == 3: q[i] = 1
                elif q[i] == 4 or q[i] == 6: q[i] = 2
                elif q[i] == 5 or q[i] == 7 or q[i] == 9: q[i] = 3
                elif q[i] == 8 or q[i] == 10: q[i] = 4
            if q[0] > q[1]:
                now_r = number
                answer += 'R'
            elif q[0] < q[1]:
                now_l = number
                answer += 'L'
            else:
                if hand == 'left':
                    now_l = number
                    answer += 'L'
                else:
                    now_r = number
                    answer += 'R'

    return answer

answer = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
print(answer)
# LRLLRRLLLRR
# LRLRLRLRLRR