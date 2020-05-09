
def solution(s):
    answer = 1000
    char = ''
    i = 1
    while i <= len(s):
        stack = [s[:i]]
        cnt = 1
        for j in range(i, len(s), i):
            if stack[-1] == s[j:j+i]:
                cnt += 1
            else:
                char += str(cnt) + stack.pop()
                stack.append(s[j:j+i])
                cnt = 1
        if stack:
            char += str(cnt) + stack.pop()
        if len(char) < answer:
            answer = len(char)





    return answer