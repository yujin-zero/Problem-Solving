import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
result = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

sum = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + graph[i-1][j-1]

k = int(sys.stdin.readline())
for _ in range(k):
    i, j, x, y = map(int, sys.stdin.readline().split())
    result.append(sum[x][y] - sum[i-1][y] - sum[x][j-1] + sum[i-1][j-1])

for r in result:
    print(r)
