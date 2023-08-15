import sys

n, k = map(int, sys.stdin.readline().split())
thing = [[0, 0]]
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    thing.append([w, v])

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight, value = thing[i][0], thing[i][1]
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)

print(dp[n][k])
