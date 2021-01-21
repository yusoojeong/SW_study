'''
수열
9
1 2 2 4 4 5 7 7 2
'''

N = int(input())
data = list(map(int, input().split()))

before_num = data[0]

for num in data[1:]:
    if num >