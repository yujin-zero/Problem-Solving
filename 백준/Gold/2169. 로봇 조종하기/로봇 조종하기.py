import sys

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N) :
    x = list(map(int, sys.stdin.readline().split()))
    graph.append(x)
dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = graph[0][0]
for i in range(1, M) :
    dp[0][i] = dp[0][i-1] + graph[0][i]

for i in range(1, N) :
    go_right = [0] * M
    go_left = [0] * M

    go_right[0] = dp[i-1][0] + graph[i][0]
    for k in range(1, M) :
        go_right[k] = max(go_right[k-1], dp[i-1][k]) + graph[i][k]
    go_left[M-1] = dp[i-1][M-1] + graph[i][M-1]
    for k in range(M-2, -1, -1) :
        go_left[k] = max(go_left[k+1], dp[i-1][k]) + graph[i][k]

    for j in range(M) :
        dp[i][j] = max(go_left[j], go_right[j])

print(dp[N-1][M-1])