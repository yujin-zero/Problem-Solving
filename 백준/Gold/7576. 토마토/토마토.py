import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
tomato = []
queue = deque()
grow = 0
for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    tomato.append(line)
    for j in range(m):
        if line[j] == 1:
            queue.append([i, j])
        else:
            grow = 1

if grow == 0:
    print(0)
    sys.exit()

while queue:
    temp = queue.popleft()
    x = temp[0]
    y = temp[1]
    for node in [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]:
        if 0 <= node[0] < n and 0 <= node[1] < m:
            if tomato[node[0]][node[1]] == 0:
                queue.append(node)
                tomato[node[0]][node[1]] = tomato[x][y]+1

max = 0
for to in tomato:
    for t in to:
        if t == 0:
            print(-1)
            sys.exit()
        if t > max:
            max = t

print(max-1)
