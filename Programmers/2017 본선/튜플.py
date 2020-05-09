def solution(s):
    answer = []
    data = [0] * (500 + 1)
    s = s[1:len(s)-1]
    i = 0
    max = 0
    while i < len(s):
        if s[i] == '{': 
            stack = []
            cnt = 0
            val = ''
            while True:
                i += 1
                if s[i] == '}':
                    if val:
                        stack.append(int(val))
                        cnt += 1
                    break
                if s[i] == ',':
                    stack.append(int(val))
                    cnt += 1
                    val = ''
                else:
                    val += s[i]
                
            data[cnt] = stack
            if max < cnt:
                max = cnt
        i += 1
        
    for char in data[1:max+1]:
        for val in char:
            if val not in answer:
                answer.append(val)

    return answer

# 이건 나중에 고쳐볼 것
def solution2(s):
    s = s[1:len(s)-1] # 앞뒤 {} 제거
    answer = []
    data = {}
    i = 0
    while i < len(s):
        if s[i] == '{':
            val = ''
            while True:
                i += 1
                if s[i] == '}' or s[i] == ',':
                    if val not in data.keys():
                        data[val] = 0
                    data[val] += 1
                    if s[i] == '}':
                        break
                    val = ''
                else:
                    val += s[i]
 
    print(data)
    return answer

# s = input()
# print(s)

# answer = solution2(s)
# print(answer)
