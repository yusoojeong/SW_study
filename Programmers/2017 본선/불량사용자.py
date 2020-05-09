def solution(user_id, banned_id):
    answer = 0
    data = [[] for _ in range(len(banned_id))]
    user_lst = [0] * len(user_id)

    for idx, ban in enumerate(banned_id):
        for us_idx, user in enumerate(user_id):
            if len(ban) == len(user):
                i = 0
                flag = True
                while i < len(ban):
                    if ban[i] != '*' and ban[i] != user[i]:
                        flag == False
                        break
                    i += 1
                if flag:
                    data[idx] += [user]
                    user_lst[us_idx] += 1
    
    for data_l in data:
        for num in data_l:
            if user_lst[num] != 1:
                pass

        
    return answer