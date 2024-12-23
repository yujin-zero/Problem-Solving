import sys
sys.setrecursionlimit(10**6)

def find(node) : 
    for neighbor in friend[node] :
        if not visit[neighbor] :
            visit[neighbor] = True
            find(neighbor)
            dp[node][1] += min(dp[neighbor])
            dp[node][0] += dp[neighbor][1]

N = int(sys.stdin.readline())
friend = [[] for _ in range(N+1)]
for _ in range(N-1) :
    u,v = map(int,sys.stdin.readline().split())
    friend[u].append(v)
    friend[v].append(u)
dp = [[0,1] for _ in range(N+1)]
visit = [False] * (N+1)
visit[1] = True
find(1)
print(min(dp[1]))