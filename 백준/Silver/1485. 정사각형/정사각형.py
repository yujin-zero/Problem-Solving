import sys
from itertools import combinations

t = int(sys.stdin.readline())
for _ in range(t):
    dot = []
    for _ in range(4):
        x, y = map(int, sys.stdin.readline().split())
        dot.append([x, y])
    length = {}
    for value in combinations(dot, 2):
        a, b, c, d = value[0][0], value[0][1], value[1][0], value[1][1]
        l = ((a-c)**2 + (b-d)**2)*(1/2)
        if l in length:
            length[l] += 1
        else:
            length[l] = 1

    if len(length) == 2:
        temp = 0
        for i in length:
            if temp < length[i]:
                temp = length[i]
        if temp == 4:
            print(1)
        else:
            print(0)
    else:
        print(0)
