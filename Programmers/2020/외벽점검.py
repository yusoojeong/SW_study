# 시간 초과 40점/100점
# 원순열 : 하나의 자리를 고정시키고 나머지를 돌린 것과 같다.
# 파이썬은 몫을 음수로 하고 나머지가 양수로 나옴

def solution(n, weak, dist):
    answer = 0
    # 갈 수 있는 거리가 긴 친구부터 정렬
    dist.sort(reverse=True)

    # 취약 지점 사이의 거리 구하기
    m = len(weak)
    weak_len = [0] * m
    # 거리는 현재 지점과 바로 다음 지점까지 거리. 마지막 취약 지점은 첫 취약 지점 사이의 거리 받아오기
    max_len, idx = 0, 0
    for i in range(m):
        if i == m - 1:
            weak_len[i] = (n - weak[i]) + weak[0]
        else:
            weak_len[i] = weak[i + 1] - weak[i]
        # 제일 먼 거리는 갈 필요가 없으므로 빼기 위해 받아와서 false으로 돌려줌
        if weak_len[i] >= max_len:
            max_len = weak_len[i]
            idx = i
    weak_len[idx] = False
    # weak_len의 false가 제일 마지막으로 가도록 weak_len을 슬라이싱해서 붙여줌
    weak_len = weak_len[idx+1:] + weak_len[:idx+1]

    while True:
        answer += 1 # answer 개수 == False 개수
        if answer > len(dist):
            return -1
        len_lst = []
        len_sum = 0
        max_len, idx = 0, 0
        for i in range(m):
            if weak_len[i] == False:
                len_lst.append(len_sum)
                len_sum = 0
            else:
                len_sum += weak_len[i]
            if weak_len[i] >= max_len:
                max_len = weak_len[i]
                idx = i
        flag = True
        for j in range(answer):
            if dist[j] < len_lst[j]:
                flag = False
                break
        if flag:
            break
        weak_len[idx] = False

    return answer


# 40점/100점
def solution(n, weak, dist):
    answer = 0
    # 갈 수 있는 거리가 긴 친구부터 정렬
    dist.sort(reverse=True)

    # 취약 지점 사이의 거리 구하기
    m = len(weak)
    weak_len = [0] * m
    # 거리는 현재 지점과 바로 다음 지점까지 거리. 마지막 취약 지점은 첫 취약 지점 사이의 거리 받아오기
    max_len, idx = 0, 0
    for i in range(m):
        if i == m - 1:
            weak_len[i] = (n - weak[i]) + weak[0]
        else:
            weak_len[i] = weak[i + 1] - weak[i]
        # 제일 먼 거리는 갈 필요가 없으므로 빼기 위해 받아와서 false로 돌려줌
        if weak_len[i] >= max_len:
            max_len = weak_len[i]
            idx = i
    weak_len[idx] = False
    # weak_len의 false가 제일 마지막으로 가도록 weak_len을 슬라이싱해서 붙여줌
    weak_len = weak_len[idx+1:] + weak_len[:idx+1]

    while True:
        answer += 1 # answer 개수 == False 개수
        if answer > len(dist):
            return -1
        len_lst = []
        len_sum = 0
        max_len, idx = 0, 0
        for i in range(m):
            if weak_len[i] == False:
                len_lst.append(len_sum)
                len_sum = 0
            else:
                len_sum += weak_len[i]
            if weak_len[i] >= max_len:
                max_len = weak_len[i]
                idx = i
        flag = True
        for j in range(answer):
            if dist[j] < len_lst[j]:
                flag = False
                break
        if flag:
            break
        weak_len[idx] = False

    return answer