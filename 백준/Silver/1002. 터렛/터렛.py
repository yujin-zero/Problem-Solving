import sys

t = int(sys.stdin.readline())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    dis = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    else:
        if r1 > r2:
            bigX, bigY, bigR = x1, y1, r1
            smallX, smallY, smallR = x2, y2, r2
        else:
            bigX, bigY, bigR = x2, y2, r2
            smallX, smallY, smallR = x1, y1, r1

        if bigR == dis:
            print(2)
        elif bigR > dis:
            if dis + smallR < bigR:
                print(0)
            elif dis + smallR == bigR:
                print(1)
            elif dis+smallR > bigR:
                print(2)
        else:
            if r1+r2 < dis:
                print(0)
            elif r1+r2 == dis:
                print(1)
            elif r1+r2 > dis:
                print(2)
