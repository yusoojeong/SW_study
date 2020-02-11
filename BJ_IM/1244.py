'''
스위치 켜고 끄기
남자 - 스위치 번호가 본인 받은 수의 배수인 것을 골라 스위칭
여자 - 본인 스위치 번호부터 대칭인 부분까지 스위칭
'''

switch = int(input())
data = [0] + list(map(int, input().split())) # 1번 인덱스부터 시작
n = int(input())
student = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    gender = student[i][0]
    sw_num = student[i][1]
    if gender == 1:
        for i in range(sw_num, switch+1):
            if i % sw_num == 0:
                if data[i] == 0: data[i] = 1
                else: data[i] = 0
    elif gender == 2:
        if data[sw_num] == 0: data[sw_num] = 1
        else: data[sw_num] = 0
        if sw_num > 1:
            for i in range(sw_num-1, 0, -1):
                if (sw_num) + (sw_num - i) > switch:
                    break
                elif data[i] == data[sw_num + sw_num - i]:
                    if data[i] == 0:
                        data[i] = data[sw_num + sw_num - i] = 1
                    else:
                        data[i] = data[sw_num + sw_num - i] = 0
                else:
                    break

for i in range(1, switch+1):
    if i != 1 and (i-1) % 20 == 0:
        print()
    print(data[i], end=" ")

            


