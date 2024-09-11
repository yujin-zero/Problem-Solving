import sys
sys.setrecursionlimit(10**6)

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


v, e = map(int, sys.stdin.readline().split())
tree = []
answer = 0
parent = [i for i in range(v+1)]
visit = set()

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    tree.append((a, b, c))
tree.sort(key=lambda x: x[2], reverse=True)

while tree:
    node1, node2, weight = tree.pop()
    if find(node1) != find(node2):  # 써클 생성되지 않음
        answer += weight
        union(node1, node2)

print(answer)
