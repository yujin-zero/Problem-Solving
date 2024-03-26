import sys


def find(x):
    if x != parent[x]:
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
m = int(sys.stdin.readline())
tree = []
answer = 0
parent = [i for i in range(n+1)]
for _ in range(m):
    com1, com2, weight = map(int, sys.stdin.readline().split())
    tree.append((com1, com2, weight))
tree.sort(key=lambda x: x[2], reverse=True)
while tree:
    com1, com2, weight = tree.pop()
    if find(com1) != find(com2):
        answer += weight
        union(com1, com2)
print(answer)
