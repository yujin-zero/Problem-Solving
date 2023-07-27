import sys


def bfs(startNode):
    queue = [startNode]
    visit.add(startNode)

    while queue != []:
        for value in node[queue[0]]:
            if value not in visit:
                queue.append(value)
                visit.add(value)
        queue.pop(0)


n, m = map(int, sys.stdin.readline().split())
node = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    node[u].append(v)
    node[v].append(u)

visit = set()
result = 0
for i in range(1, n+1):
    if i not in visit:
        bfs(i)
        result += 1

print(result)
