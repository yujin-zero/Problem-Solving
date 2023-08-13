import sys
# 누적합 문제

n, m = map(int, sys.stdin.readline().split())
graph = []
answer = []
prefixSum = [[0]*(n+1) for _ in range(n+1)]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - \
            prefixSum[i-1][j-1] + graph[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    a = prefixSum[x2][y2] - prefixSum[x2][y1-1] - \
        prefixSum[x1-1][y2] + prefixSum[x1-1][y1-1]
    answer.append(a)

for a in answer:
    print(a)
