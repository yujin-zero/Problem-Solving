import sys


def add_line(a, b):
    line[a-1][b-1] = 1
    line[b-1][a-1] = 1


def dfs(node):
    computer[node] = 1
    for i in range(n):
        if line[node][i] == 1 and computer[i] == 0:
            dfs(i)


n = int(sys.stdin.readline())
line = [[0]*n for _ in range(n)]

m = int(sys.stdin.readline())
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    add_line(x, y)

computer = [0]*n
dfs(0)

result = 0
for i in range(1, n):
    if computer[i] == 1:
        result += 1
print(result)
