import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[float('inf')] * (n+1) for _ in range(n+1)]
for i in range(1,n+1) :
    graph[i][i] = 0
for _ in range(m) :
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a][b] = min(c,graph[a][b])

# 플로이드-워셜 알고리즘
for k in range(1,n+1) :
    for i in range(1,n+1) :
        for j in range(1,n+1) :
            if graph[i][j] > graph[i][k] + graph[k][j] :
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1,n+1) :
    for j in range(1,n+1) :
        if graph[i][j] == float('inf') :
            print(0, end=' ')
        else :
            print(graph[i][j],end=' ')
    print()