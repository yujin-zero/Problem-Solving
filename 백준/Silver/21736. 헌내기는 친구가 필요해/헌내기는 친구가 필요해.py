import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
campus = []
for i in range(n):
    line = list(sys.stdin.readline().strip())
    campus.append(line)
    for j in range(m):
        if line[j] == 'I':
            startI = i
            startJ = j

queue = deque()
queue.append([startI, startJ])
count = 0
while queue:
    temp = queue.popleft()
    x = temp[0]
    y = temp[1]
    for value in [[x+1, y], [x, y+1], [x-1, y], [x, y-1]]:
        if 0 <= value[0] < n and 0 <= value[1] < m:
            sign = campus[value[0]][value[1]]
            if sign == 'O':
                queue.append(value)
                campus[value[0]][value[1]] = 'S'
            elif sign == 'P':
                count += 1
                queue.append(value)
                campus[value[0]][value[1]] = 'S'

if count == 0:
    print("TT")
else:
    print(count)
