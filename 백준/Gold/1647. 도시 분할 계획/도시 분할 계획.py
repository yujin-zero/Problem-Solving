import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    else:
        return x


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
        path.discard(b)
    else:
        parent[a] = b
        path.discard(a)


n, m = map(int, sys.stdin.readline().split())
if n == 2:
    print(0)
    exit(0)
tree = []
parent = [i for i in range(n+1)]
path = set(i for i in range(1, n+1))
answer = 0

for _ in range(m):
    house1, house2, weight = map(int, sys.stdin.readline().split())
    tree.append((house1, house2, weight))
tree.sort(key=lambda x: x[2], reverse=True)

while tree:
    house1, house2, weight = tree.pop()
    if find(house1) != find(house2):
        answer += weight
        union(house1, house2)
        if len(path) == 2:
            break

print(answer)
