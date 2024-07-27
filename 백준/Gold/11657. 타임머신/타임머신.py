import sys
INF = int(1e9)

def bf(start) :
    dp[start] = 0

    for i in range(n) :
        for cur, next, cost in edge :
            if dp[cur] != INF and dp[cur] + cost < dp[next] :
                dp[next] = dp[cur] + cost
                if i == (n-1) :
                    return True

    return False


n, m = map(int,sys.stdin.readline().split())
edge = []
dp = [INF] * (n+1)
for _ in range(m) :
    a, b, c = map(int,sys.stdin.readline().split())
    edge.append((a,b,c))

answer = bf(1)
if answer :
    print(-1)
else:
    for i in range(2,n+1) :
        if dp[i] == INF:
            print(-1)
        else:
            print(dp[i])