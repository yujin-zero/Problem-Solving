import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
queue = deque()
degree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
answer = []
cnt = 0
visit = set()

for _ in range(m) :
    sequence = list(map(int,sys.stdin.readline().split()))
    ll = sequence[0] + 1

    for i in range(1,ll) :
        value = sequence[i] 
        visit.add(value)
        for j in range(i+1, ll) :
            if sequence[j] not in graph[value] :
                graph[value].append(sequence[j])
                degree[sequence[j]] += 1

for i in range(1,n+1) :
    if degree[i] == 0:
        queue.append(i)
        degree[i] -= 1

while queue :
    x = queue.popleft()
    answer.append(x)
    cnt += 1
    for y in graph[x] :
        degree[y] -= 1
        if degree[y] == 0 :
            queue.append(y)

if cnt == n :
    for a in answer :
        print(a)
else :
    print(0)
