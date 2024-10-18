import sys
sys.setrecursionlimit(10**6)

def DFS(city, visit) :

    if dp[city][visit] != -1 :
        return dp[city][visit]

    if visit == 2**N-1 :
        if W[city][1] > 0 :
            return W[city][1]
        else :
            return float('inf')

    min_cost = float('inf')
    for i in range(2,N+1) :
        # 비트자리가 0인 것들에만 보냄
        tmp = 1 << (i-1)
        if visit & tmp == 0 and W[city][i] > 0:
            min_cost = min(min_cost,DFS(i,visit|tmp)+W[city][i])

    if min_cost != float('inf') :
        dp[city][visit] = min_cost
    else :
        dp[city][visit] = float('inf')
    return dp[city][visit]


N = int(sys.stdin.readline())
W = [[0]]
for _ in range(N) :
    w = [0] + list(map(int,sys.stdin.readline().split()))
    W.append(w)

dp = [[-1 for _ in range(1<<N)] for _ in range(N+1)]

print(DFS(1,1))