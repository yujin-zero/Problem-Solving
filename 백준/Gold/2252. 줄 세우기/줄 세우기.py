import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
degree = [0 for _ in range(n+1)]
queue = deque()
answer = []
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    degree[b] += 1
    graph[a].append(b)

for i in range(1,n+1) :
    if degree[i] == 0 :
        queue.append(i)

while queue :
    value = queue.popleft()
    answer.append(value)
    for x in graph[value] :
        degree[x] -= 1
        if degree[x] == 0:
            queue.append(x)

print(*answer)