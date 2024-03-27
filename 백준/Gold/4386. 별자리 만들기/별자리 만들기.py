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
star = []
tree = []
answer = 0
for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    star.append((x, y))

for i in range(n-1):
    for j in range(i+1, n):
        x1, y1 = star[i]
        x2, y2 = star[j]
        weight = ((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))**(1/2)
        tree.append((i+1, j+1, weight))
tree.sort(key=lambda x: x[2], reverse=True)

while tree:
    star1, star2, weight = tree.pop()
    if find(star1) != find(star2):
        answer += weight
        union(star1, star2)

print(answer)
