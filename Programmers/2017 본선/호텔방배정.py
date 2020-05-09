## 1번 풀이 - 테케 1 틀림 / 효율 0
def solution(k, room_number):
    answer = []
    room = [True] * k
    for num in room_number:
        if room[num]:
            room[num] = False
        else:
            while True:
                num += 1
                if room[num]:
                    room[num] = False
                    break
        answer.append(num)
                    
    return answer

## 2번 풀이 - 테케 정답 / 효율 0
def solution2(k, room_number):
    answer = [0] * len(room_number)
    for i, num in enumerate(room_number):
        if num not in answer:
            answer[i] = num
        else:
            while True:
                num += 1
                if num not in answer:
                    answer[i] = num
                    break               
    return answer