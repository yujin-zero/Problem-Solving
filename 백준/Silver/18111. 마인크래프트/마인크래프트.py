import sys

n, m, b = map(int, sys.stdin.readline().split())
ground = {}  # 높이 : 갯수
for _ in range(n):
    g = list(map(int, sys.stdin.readline().split()))
    for i in range(m):
        if g[i] in ground:
            ground[g[i]] += 1
        else:
            ground[g[i]] = 1


time = []

for x in range(min(ground), max(ground)+1):
    t = 0
    block = b
    for key in ground:
        if key > x:
            y = key-x
            t += 2*y*ground[key]
            block += y*ground[key]
        else:
            y = x - key
            t += y*ground[key]
            block -= y*ground[key]

    if block >= 0:
        time.append([t, x])

time.sort(key=lambda x: (x[0], -x[1]))
print(time[0][0], time[0][1])