import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

visit = [100001] * (100001)
queue = deque([n])
visit[n] = 0

while queue:
    temp = queue.popleft()

    if 0 <= temp-1 < 100001:
        if visit[temp]+1 < visit[temp-1]:
            visit[temp-1] = visit[temp] + 1
            queue.append(temp-1)
    if 0 <= temp+1 < 100001:
        if visit[temp]+1 < visit[temp+1]:
            visit[temp+1] = visit[temp] + 1
            queue.append(temp+1)
    if temp != 0:
        h = temp
        while True:
            h *= 2
            if h > 100000:
                break
            if visit[temp] < visit[h]:
                visit[h] = visit[temp]
                queue.append(h)

print(visit[k])
