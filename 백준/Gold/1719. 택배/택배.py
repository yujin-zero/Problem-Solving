import sys

n, m = map(int,sys.stdin.readline().split())
path = [['-' for _ in range(n+1)] for _ in range(n+1)]
dp = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m) :
    a, b, c = map(int,sys.stdin.readline().split())
    path[a][b] = b
    path[b][a] = a
    dp[a][b] = c
    dp[b][a] = c

for k in range(1,n+1) :
    for i in range(1,n+1) :
        if i == k :
            continue
        for j in range(1,n+1) :
            if k == j or i == j : 
                continue 
            if dp[i][j] > dp[i][k] + dp[k][j] :
                dp[i][j] = dp[i][k] + dp[k][j]
                path[i][j] = path[i][k] 

for i in range(1,n+1) :
    for j in range(1,n+1) :
        print(path[i][j],end = ' ')
    print()
