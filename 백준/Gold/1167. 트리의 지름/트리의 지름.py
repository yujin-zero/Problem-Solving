import sys
sys.setrecursionlimit(10**6)

def DFS(node, dist) :
    global maxDist, findNode 
    visit[node] = True

    if dist > maxDist :
        maxDist = dist
        findNode = node

    for nextNode, weight in tree[node] :
        if not visit[nextNode] :
            DFS(nextNode, dist + weight)

v = int(sys.stdin.readline())
tree = [[] for _ in range(v+1)]
for _ in range(v) :
    x = list(map(int,sys.stdin.readline().split()))

    node = x[0]
    for i in range(1,len(x)-1,2) :
        n, w = x[i], x[i+1]
        tree[node].append((n,w))

maxDist = 0
findNode = -1
visit = [False] * (v+1)
DFS(1,0)

maxDist = 0
visit = [False] * (v+1)
DFS(findNode, 0)

print(maxDist)