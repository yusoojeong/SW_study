import sys
sys.stdin = open("1002_터렛_input.txt")

T = int(input())

for tc in range(1, T+1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    answer = 0

    # Set a value of 1 with a small distance
    if r1 > r2:
        x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    if distance == 0:
        if r1 == r2:
            answer = -1
        else:
            answer = 0
    elif r2 - r1 < distance < r2 + r1:
        answer = 2
    elif distance == r2 + r1 or distance == r2 - r1:
        answer = 1

    print(answer)
    '''
    wrong solve
    result = []

    # Set a value of 1 with a small distance
    if r1 > r2:
        x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1

    for x in range(x1-r1, x1+r1+1):
        y = y1 + ((r1 ** 2) + ((x - x1) ** 2)) ** 0.5
        # Verify that y is an integer value
        if math.isclose(int(y), y):
            y = int(y)
            if ((x - x2) ** 2 + (y - y2) ** 2) == (r2 ** 2):
                result.append((x, y))
    '''
