import sys

n, k = map(int,sys.stdin.readline().split())
dp = [[False for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1) :
    dp[i][i] = True
for _ in range(k) :
    a, b = map(int,sys.stdin.readline().split())
    dp[a][b] = True

for k in range(1,n+1) :
    for i in range(1,n+1) :
        if dp[i][k] == False :
            continue
        for j in range(1,n+1) :
            if dp[k][j] :
                dp[i][j] = True

s = int(sys.stdin.readline())
for _ in range(s) :
    a, b = map(int,sys.stdin.readline().split())
    if dp[a][b] :
        print(-1)
    elif dp[b][a] :
        print(1)
    else :
        print(0)