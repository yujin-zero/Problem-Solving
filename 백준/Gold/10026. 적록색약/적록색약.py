import sys
from collections import deque


def where(b):
    for i in range(n):
        for j in range(n):
            if b[i][j] != 1:
                return [i, j, b[i][j]]
    return -1


def countColor(a):
    count = 0
    while where(a) != -1:
        startX, startY = where(a)[0], where(a)[1]
        c = where(a)[2]
        queue = deque()
        queue.append([startX, startY])
        a[startX][startY] = 1

        while queue:
            temp = queue.popleft()
            x, y = temp[0], temp[1]
            for value in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
                x1, y1 = value[0], value[1]
                if 0 <= x1 < n and 0 <= y1 < n:
                    if a[x1][y1] == c:
                        queue.append(value)
                        a[x1][y1] = 1
        count += 1

    return count


n = int(sys.stdin.readline())
color = []
for i in range(n):
    c = list(sys.stdin.readline().rstrip())
    color.append(c)

color2 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if color[i][j] == 'R':
            color2[i][j] = 'G'
        else:
            color2[i][j] = color[i][j]


print(countColor(color), end=' ')
print(countColor(color2))
