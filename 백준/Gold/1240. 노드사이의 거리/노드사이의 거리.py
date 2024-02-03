import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    visit = set()
    queue = deque()
    queue.append((a, 0))

    while queue:
        x, y = queue.popleft()
        visit.add(x)

        if x == b:
            print(y)
            break

        for node, dis in tree[x]:
            if node not in visit:
                visit.add(node)
                queue.append((node, dis+y))
