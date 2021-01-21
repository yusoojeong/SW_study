'''
https://www.acmicpc.net/problem/9655
돌 게임
'''

N = int(input())
i = 0

while N > 0:

    if N > 2:
        N -= 3
    else:
        N -= 1
    i += 1

if i % 2:
    print("SK")
else:
    print("CY")