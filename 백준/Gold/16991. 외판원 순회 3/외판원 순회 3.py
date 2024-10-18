import sys

def DFS(city,visit) :

    if dp[city][visit] != -1 :
        return dp[city][visit]
    
    if visit == (1<<N)-1 :
        if W[1][city] != 0 :
            return W[1][city]
        else :
            return float('inf')
        
    min_cost = float('inf')
    for i in range(2,N+1) :
        tmp = 1 << (i-1)
        if visit & tmp == 0 and W[i][city] > 0 :
            min_cost = min(min_cost,DFS(i,visit|tmp)+W[i][city])

    dp[city][visit] = min_cost 
    return dp[city][visit]



N = int(sys.stdin.readline())
pos = [(-1,-1)]
W = [[0] * (N+1) for _ in range(N+1)]
for i in range(1,N+1) :
    x, y = map(int,sys.stdin.readline().split())
    pos.append((x,y))
for i in range(1,N+1) :
    a, b = pos[i]
    for j in range(i+1,N+1) :
        c, d = pos[j]
        dis = ((a-c)**2 + (b-d)**2)**(1/2)
        W[i][j] = dis
        W[j][i] = dis

dp = [[-1] * (1<<N) for _ in range(N+1)]

print(DFS(1,1))