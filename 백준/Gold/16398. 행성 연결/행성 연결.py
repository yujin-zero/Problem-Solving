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
tree = []
parent = [i for i in range(n+1)]
answer = 0
for i in range(1, n+1):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(i, n):
        tree.append((i, j+1, lst[j]))
tree.sort(key=lambda x: x[2], reverse=True)
while tree:
    planet1, planet2, weight = tree.pop()
    if find(planet1) != find(planet2):
        answer += weight
        union(planet1, planet2)

print(answer)
