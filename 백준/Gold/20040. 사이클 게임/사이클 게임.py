import sys


def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    if find(a) == find(b):
        print(i+1)
        exit()
    union(a, b)

print(0)
