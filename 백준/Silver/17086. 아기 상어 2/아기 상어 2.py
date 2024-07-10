import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
graph = []
queue = deque()
cnt = 0
visit = set()

for i in range(n) :
    x = list(map(int,sys.stdin.readline().split()))
    graph.append(x)
    for j in range(m) :
        if x[j] == 1 :
            cnt += 1
            queue.append((i,j))
            visit.add((i,j))

while queue :
    a, b = queue.popleft()
    distance = graph[a][b] + 1
    for i in range(a-1,a+2) :
        for j in range(b-1, b+2) :
            if 0 <= i < n and 0 <= j < m :
                if (i,j) not in visit :
                    visit.add((i,j))
                    queue.append((i,j))
                    graph[i][j] = distance
                    cnt += 1

                    if cnt == n*m :
                        print(distance-1)
                        sys.exit(0)


