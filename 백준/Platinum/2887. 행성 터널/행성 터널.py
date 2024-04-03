import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(sys.stdin.readline())
parent = [i for i in range(n+1)]
tree = []
answer = 0
axis_x = []
axis_y = []
axis_z = []

for i in range(1, n+1):
    x, y, z = map(int, sys.stdin.readline().split())
    axis_x.append((x, i))
    axis_y.append((y, i))
    axis_z.append((z, i))

axis_x.sort()
axis_y.sort()
axis_z.sort()

for i in range(n-1):
    nowX, nowP = axis_x[i]
    nextX, nextP = axis_x[i+1]
    tree.append((nowP, nextP, nextX-nowX))
    nowY, nowP = axis_y[i]
    nextY, nextP = axis_y[i+1]
    tree.append((nowP, nextP, nextY-nowY))
    nowZ, nowP = axis_z[i]
    nextZ, nextP = axis_z[i+1]
    tree.append((nowP, nextP, nextZ-nowZ))

tree.sort(key=lambda x: x[2], reverse=True)

while tree:
    p1, p2, w = tree.pop()
    if find(p1) != find(p2):
        answer += w
        union(p1, p2)

print(answer)
