import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
visit = [[-1]*m for _ in range(n)]
for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    graph.append(line)
    if 0 in line:
        for j in range(m):
            if line[j] == 0:
                visit[i][j] = 0
    if 2 in line:
        for j in range(m):
            if line[j] == 2:
                startX, startY = i, j
                break

queue = deque()
queue.append([startX, startY])
visit[startX][startY] = 0

while queue:
    temp = queue.popleft()
    x = temp[0]
    y = temp[1]
    for value in [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]:
        if 0 <= value[0] < n and 0 <= value[1] < m:
            if (visit[value[0]][value[1]] == -1) and (graph[value[0]][value[1]] == 1):
                queue.append(value)
                visit[value[0]][value[1]] = visit[x][y] + 1

for v in visit:
    print(*v)
