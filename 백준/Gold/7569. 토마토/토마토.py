import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

tomato = []
queue = deque()
count = 1

for i in range(h):
    toma = []
    for j in range(n):
        t = list(map(int, sys.stdin.readline().split()))
        for k in range(m):
            if t[k] == 1:
                queue.append([i, j, k])
                # t[k] = 2
        toma.append(t)
    tomato.append(toma)

while queue:
    temp = queue.popleft()
    x = temp[0]
    y = temp[1]
    z = temp[2]
    for value in [[x-1, y, z], [x+1, y, z], [x, y-1, z], [x, y+1, z], [x, y, z-1], [x, y, z+1]]:
        x2 = value[0]
        y2 = value[1]
        z2 = value[2]
        if 0 <= x2 < h and 0 <= y2 < n and 0 <= z2 < m:
            if tomato[x2][y2][z2] == 0:
                queue.append(value)
                count = tomato[x2][y2][z2] = tomato[x][y][z]+1

check = 0
for a in tomato:
    for b in a:
        for c in b:
            if c == 0:
                check = 1
                break
        if check == 1:
            break
    if check == 1:
        break

if check == 0:
    print(count-1)
else:
    print(-1)
