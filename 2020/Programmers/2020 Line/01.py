def solution(boxes):
    answer = 0
    check_list = [0] * 1000000
    
    for goods in boxes:
        if goods[0] != goods[1]:
            answer += 1
            check_list[goods[0]] += 1
            check_list[goods[1]] += 1
            if check_list[goods[0]] == 2:
                check_list[goods[0]] = 0
                answer -= 1
            if check_list[goods[1]] == 2:
                check_list[goods[1]] = 0
                answer -= 1
    
    return answer