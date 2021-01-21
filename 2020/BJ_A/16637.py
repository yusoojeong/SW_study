'''
괄호를 추가(이중괄호는 안됨)하거나 하지 않아서 최대값 만들기
연산자는 모두 우선순위가 동일하다.
괄호를 통해 우선순위를 바꿀 수 있다.
9
3+8*7-9*2
'''

def calculate(n1, n2, calc):

    if calc == '+':
        return n1 + n2
    elif calc == '-':
        return n1 - n2
    elif calc == '*':
        return n1 * n2

N = int(input())
data = list(input())
stack = []
stack2 = []

for i in range(N):
    stack.append(data[i])
    stack2.append(data[i])
    print(stack2)
    if not i % 2 and i != 0:
        n2 = stack.pop()
        calc = stack.pop()
        n1 = stack.pop()
        stack.append(calculate(int(n1), int(n2), calc))
    if not i % 4 and i != 0:
        n2 = stack2.pop()
        calc = stack2.pop()
        n1 = stack2.pop()
        stack2.append(calculate(int(n1), int(n2), calc))
        n2 = stack2.pop()
        calc = stack2.pop()
        n1 = stack2.pop()
        stack2.append(calculate(int(n1), int(n2), calc))
        print(stack2)



    

# if N != 1:
#     i = 1
#     while True:
#         if (data[i] == '*' and data[i+2] == '+') or (data[i] == '-' and data[i+2] == '-' and (int(data[i-1]) >= int(data[i+1])-int(data[i+3]))) or (data[i+2] == '*' and data[i+3] == '0'):
#             data = data[:i+1] + [str(calculate(data[i+1:i+4]))] + data[i+4:]
#         if 3 <= i <= len(data)-4:
#             if data[i] == '*' and data[i-2] == '-' and data[i+2] == '-' and data[i+1] < data[i+3]:
#                 data = data[:i+1] + [str(calculate(data[i+1:i+4]))] + data[i+4:]
#         i += 2
#         if i + 2 >= len(data):
#             break

#     n = len(data) // 2
#     ## 앞에서부터 하기
#     for i in range(n):
#         data = [str(calculate(data[0:3]))] + data[3:]

#     print(data[0])
