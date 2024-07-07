import sys

n, m = map(int,sys.stdin.readline().split())
app = list(map(int,sys.stdin.readline().split()))
cost = list(map(int,sys.stdin.readline().split()))

dp = [[0 for _ in range(sum(cost)+1)] for _ in range(n)]

for i in range(sum(cost)+1) :
    if i < cost[0] :
        dp[0][i] = 0
    else :
        dp[0][i] = app[0]

for i in range(1,n) :
    for j in range(sum(cost)+1) :
        if j < cost[i] :
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-cost[i]]+app[i])

for i in range(sum(cost)+1) :
    for j in range(n) :
        if dp[j][i] >= m :
            print(i)
            sys.exit(0)
