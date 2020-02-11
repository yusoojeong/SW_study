'''
https://www.acmicpc.net/problem/2635
수 이어가기

1. 첫 번째 수는 양의 정수
2. 두 번째 수는 양의 정수 중 하나(첫번째 수와 같거나 작은 수)
3. 세 번째 이후 수는 아래 규칙에 따라 정해짐(첫번째 수 = 1/ 두번째 수 = 2 / ,,,)
   3) 1 - 2 / 4) 2 - 3 / 5) 3 - 4
4. 음의 정수가 만들어지면 음의 정수를 버리고 수를 만들지 않는다.

최대 개수 만드는 프로그램
'''

number = int(input())
result = {}
max = 0

# 뒤에서부터 돌리면서 개수를 key로, 누적 값을 value로 가지는 딕셔너리 만들기
for num in range(number, 0, -1):
    case = [number, num]
    i = 1
    while True:
        num = case[i-1] - case[i]
        if num < 0:
            break
        i += 1    
        case.append(num)
    result[len(case)] = list(case)

for key, val in result.items():
    if key > max:
        max = key
        ans = val

print(max)
for i in range(max):
    print(ans[i], end=" ")



