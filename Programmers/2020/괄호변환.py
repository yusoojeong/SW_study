# 16/100
## 조건 대로
def solution(p):
    answer = ''
    # 1. 빈 문자열은 그대로 돌려준다.
    if not p:
        return answer

    # 2. w를 균형잡힌 괄호 문자열" u, v로 분리한다.
    while p:
        answer, p = check(answer, p)
        if p:
            ans, p = reverse_check(p)
            answer += ans

    return answer


def check(answer, p):
    i = 0
    cnt = 0
    if p[0] == ')':
        return '', p

    while i < len(p):
        if p[i] == ')':
            if cnt <= 0:
                i -= 1
                break
            cnt -= 1
            i += 1
        else:
            cnt += 1
            i += 1
    answer += p[:i]
    p = p[i:]

    return answer, p


def reverse_check(p):
    i = 0
    cnt = 0
    ans = '('
    while i < len(p):
        if p[i] == '(':
            if cnt <= 0:
                break
            cnt -= 1
            i += 1
        else:
            cnt += 1
            i += 1

    if i == 2:
        return '()', []
    for j in range(1, i - 1):
        if p[j] == '(':
            ans += ')'
        else:
            ans += '('
    ans += ')'
    p = p[i:]

    return ans, p

# 여전히 16/100
def solution(p):
    answer = ''
    i = 0
    while i < len(p):
        if p[i] == ')':
            st = i
            cnt = 0
            answer += '('
            while p[i] == ')':
                cnt += 1
                i += 1
            answer += ('()' * (cnt - 1)) + ')'
            i = st + (cnt * 2)
        else:
            st = i
            cnt = 0
            while i < len(p):
                if p[i] == ')':
                    if cnt < 0:
                        i -= 1
                        break
                    cnt -= 1
                    i += 1
                else:
                    cnt += 1
                    i += 1
            answer += p[st:i]

    return answer

print(solution2("()))((()"))