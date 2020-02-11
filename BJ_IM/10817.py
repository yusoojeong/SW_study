'''
https://www.acmicpc.net/problem/10817
세 수 중 두 번째로 큰 정수 출력
'''

data = list(map(int, input().split()))

data.sort()

print(data[1])