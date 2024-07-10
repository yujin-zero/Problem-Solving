import sys
from collections import deque


n, m = map(int,sys.stdin.readline().split())
degree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
queue = deque()
answer = [1 for _ in range(n)]

for _ in range(m) :
    a, b = map(int,sys.stdin.readline().split())
    degree[b] += 1
    graph[a].append(b)

for i in range(1,n+1) :
    if degree[i] == 0 :
        queue.append(i)

while queue :
    tmp = queue.popleft()
    for x in graph[tmp] :
        degree[x] -= 1
        if degree[x] == 0:
            queue.append(x)
            answer[x-1] = answer[tmp-1] + 1

print(*answer)