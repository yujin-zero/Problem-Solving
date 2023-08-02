import sys
from collections import deque


def findStart():
    for i in range(n):
        for j in range(n):
            if danzi[i][j] == 1:
                return [i, j]
    return -1


n = int(sys.stdin.readline())
danzi = []
for _ in range(n):
    line = list(map(int, sys.stdin.readline().rstrip()))
    danzi.append(line)

sum = []
start = findStart()
while start != -1:
    queue = deque()
    queue.append(start)
    startX, startY = start[0], start[1]
    danzi[startX][startY] = 2
    count = 1
    while queue:
        temp = queue.popleft()
        x = temp[0]
        y = temp[1]
        for value in [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]:
            if 0 <= value[0] < n and 0 <= value[1] < n:
                if danzi[value[0]][value[1]] == 1:
                    queue.append(value)
                    danzi[value[0]][value[1]] = 2
                    count += 1
    sum.append(count)
    start = findStart()

print(len(sum))
sum.sort()
for s in sum:
    print(s)
