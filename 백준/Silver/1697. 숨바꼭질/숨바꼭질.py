import sys
from collections import deque


n, k = map(int, sys.stdin.readline().split())

if n >= k:
    print(n-k)
    sys.exit()

queue = deque()
queue.append(n)
visit = {}
visit[n] = 0

while k not in visit:
    temp = queue.popleft()
    for value in {temp-1, temp+1, temp*2}:
        if value >= 0 and value <= 100000 and (value not in visit):
            queue.append(value)
            visit[value] = visit[temp]+1


print(visit[k])