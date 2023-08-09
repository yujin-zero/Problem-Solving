import sys

n = int(sys.stdin.readline())
edge = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    edge[x].append(y)
    edge[y].append(x)

visit = set()
visit.add(1)
stack = [1]
parrent = {}

while stack:
    temp = 0
    explor = stack[-1]
    for node in edge[explor]:
        if node not in visit:
            parrent[node] = explor
            stack.append(node)
            visit.add(node)
            temp = 1
    if temp == 0:
        stack.pop()


for i in range(2, n+1):
    print(parrent[i])
