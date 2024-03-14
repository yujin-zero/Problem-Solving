import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
wall = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
answer = float('inf')
queue = deque([(0, 0, 1, 1)])

while queue:
    row, col, broke, dis = queue.popleft()

    for value in [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]:
        x = value[0]
        y = value[1]
        if 0 <= x < n and 0 <= y < m:
            if x == n-1 and y == m-1:
                if answer > dis+1:
                    answer = dis+1
            if wall[x][y] == 0:
                queue.append((x, y, broke, dis+1))
                if broke == 1:
                    wall[x][y] = 2  # 부술 수 있음
                else:
                    wall[x][y] = 3  # 더 부술 수 없음
            elif wall[x][y] == 1 and broke == 1:
                queue.append((x, y, 0, dis+1))
                wall[x][y] = 4  # 부수고 옴, 벽이었음
            else:
                if wall[x][y] == 3 and broke == 1:
                    queue.append((x, y, 1, dis+1))
                    wall[x][y] = 2

if wall[n-1][m-1] == 0:
    if n == 1 and m == 1:
        print(1)
    else:
        print(-1)
else:
    print(answer)
