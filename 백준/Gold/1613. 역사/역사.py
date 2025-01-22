import sys

n, k = map(int,sys.stdin.readline().split())
dp = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1) :
    dp[i][i] = 0
for _ in range(k) :
    a, b = map(int,sys.stdin.readline().split())
    dp[a][b] = 1

for k in range(1,n+1) :
    for i in range(1,n+1) :
        if dp[i][k] == float('inf') :
            continue
        for j in range(1,n+1) :
            dp[i][j] = min(dp[i][k] + dp[k][j],dp[i][j])

s = int(sys.stdin.readline())
for _ in range(s) :
    a, b = map(int,sys.stdin.readline().split())
    if dp[a][b] != float('inf') :
        print(-1)
    elif dp[b][a] != float('inf') :
        print(1)
    else :
        print(0)