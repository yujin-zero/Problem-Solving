import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = []
for _ in range(n):
    line = list(map(int, sys.stdin.readline().rstrip()))
    maze.append(line)

queue = deque([[0, 0]])
maze[0][0] = 2  # 끝에서 1 빼기
while queue:
    temp = queue.popleft()
    x = temp[0]
    y = temp[1]
    for value in [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]:
        if 0 <= value[0] < n and 0 <= value[1] < m:
            if maze[value[0]][value[1]] == 1:
                queue.append(value)
                maze[value[0]][value[1]] = maze[x][y] + 1

print(maze[n-1][m-1] - 1)
