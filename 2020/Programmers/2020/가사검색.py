# 시간 초과
def solution(words, queries):
    n = len(queries)
    answer = [0] * n
    for idx, keyword in enumerate(queries):
        for word in words:
            if len(keyword) == len(word):
                i = 0
                flag = True
                while i < len(keyword):
                    if keyword[i] != '?'and keyword[i] != word[i]:
                        flag = False
                        break
                if flag:
                    answer[idx] += 1
    return answer

# 정확성 25 / 효율성 30 -> 합 55/100
def solution(words, queries):
    # answer을 keyword의 개수만큼 0으로 채우기
    n = len(queries)
    answer = [0] * n
    # keyword를 하나씩 받아온다. answer에 매칭시키기 위해 enumerate 사용
    for idx, keyword in enumerate(queries):
        # sp는 slicing할 point를 줄여서 적은 변수
        sp = [0, len(keyword)]
        # keyword가 처음 ?로 시작한다면 접미사를 찾는 것.
        if keyword[0] == '?':
            for st in range(len(keyword)):
                if keyword[st] != '?':
                    sp[0] = st
                    break
        # keyword가 처음 ?가 아니라면 접두사를 찾는 것.
        else:
            for st in range(len(keyword)):
                if keyword[st] == '?':
                    sp[1] = st
                    break
        # words 안에 담긴 문자들을 꺼내서 keyword의 ?가 아닌 부분과 일치하는지 확인
        for word in words:
            # 길이가 다른 경우 해당하지 않으므로 len을 써서 비교
            if len(keyword) == len(word) and keyword[sp[0]:sp[1]] == word[sp[0]:sp[1]]:
                answer[idx] += 1
    return answer
