'''
https://www.acmicpc.net/problem/17413
단어 뒤집기2

<>는 태그로 뒤집지 않는다.
태그와 단어 사이에는 공백이 없다.
연속된 두 단어는 공백 하나로 구분된다.
'''

data = input()
words = []
ans = ''

for char in data:
    if char == '<':
        if ans:            
            if '<' not in ans:
                words.append(ans[::-1])
            else:
                words.append(ans)
            ans = ''
        ans += char
    elif char == '>':
        ans += char
        words.append(ans)
        ans = ''
    elif char == ' ':
        if '<' not in ans:
            words.append(ans[::-1])
            words.append(' ')
            ans = ''
        else:
            ans += char
    else:
        ans += char
if ans:
    if '<' not in ans:
        words.append(ans[::-1])
    else:
        words.append(ans)

print("".join(words))