import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n)]

for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if line[j] == 1:
            graph[i].append(j)

for i in range(n):
    for j in range(n):
        queue = deque([i])
        visit = []
        check = 0
        while queue:
            temp = queue.popleft()
            if graph[temp]:
                for g in graph[temp]:
                    if g not in visit:
                        queue.append(g)
                        visit.append(g)
                        if g == j:
                            print(1, end=' ')
                            check = 1
                            break
            if check == 1:
                break
        if j not in visit:
            print(0, end=' ')
    print()
