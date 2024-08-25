import sys

n, m, r = map(int,sys.stdin.readline().split())
item = list(map(int,sys.stdin.readline().split()))
dist = [[float('inf')] * n for _ in range(n)]
answer = 0
for i in range(n) :
    dist[i][i] = 0
for _ in range(r) :
    a, b, l = map(int,sys.stdin.readline().split())
    dist[a-1][b-1] = l
    dist[b-1][a-1] = l

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if dist[i][j] > dist[i][k] + dist[k][j] :
                dist[i][j] = dist[i][k] + dist[k][j]

for node in range(n) :
    tmp = 0
    for neighborNode in range(n) :
        if dist[node][neighborNode] <= m :
            tmp += item[neighborNode]
    answer = max(answer,tmp)

print(answer)