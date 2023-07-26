import sys


def dfs(v):
    visit = [v]
    stack = [v]
    while stack != []:
        c = 0
        for n in node[stack[-1]]:
            if n not in visit:
                stack.append(n)
                visit.append(n)
                c = 1
                break
        if c == 0:
            stack.pop()
    for vi in visit:
        print(vi, end=' ')
    print()


def bfs(v):
    visit = [v]
    queue = [v]
    while queue != []:
        for n in node[queue[0]]:
            if n not in visit:
                queue.append(n)
                visit.append(n)
        queue.pop(0)
    for vi in visit:
        print(vi, end=' ')
    print()


n, m, v = map(int, sys.stdin.readline().split())
node = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    node[x].append(y)
    node[y].append(x)
for i in range(n+1):
    node[i].sort()

dfs(v)
bfs(v)
