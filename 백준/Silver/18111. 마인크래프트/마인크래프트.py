import sys


def high():
    max = 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] > max:
                max = ground[i][j]
    return max


def low():
    min = 256
    for i in range(n):
        for j in range(m):
            if ground[i][j] < min:
                min = ground[i][j]
    return min


n, m, b = map(int, sys.stdin.readline().split())
ground = []
for _ in range(n):
    g = list(map(int, sys.stdin.readline().split()))
    ground.append(g)

time = []

for x in range(low(), high()+1):
    t = 0
    block = b
    for i in range(n):
        for j in range(m):
            if ground[i][j] > x:
                y = ground[i][j]-x
                t += 2*y
                block += y
            else:
                y = x - ground[i][j]
                t += y
                block -= y
    if block >= 0:
        time.append([t, x])

time.sort(key=lambda x: (x[0], -x[1]))
print(time[0][0], time[0][1])
