import sys
sys.setrecursionlimit(10**6)

def dfs(r,c) :
    if r == M-1 and c == N-1 :
        return 1
    
    if dp[r][c] != -1 :
        return dp[r][c]

    dp[r][c] = 0
    current_h = graph[r][c]
    for dr, dc in move :
        next_r = r + dr
        next_c = c + dc
        if 0 <= next_r < M and 0 <= next_c < N :
            next_h = graph[next_r][next_c]
            if next_h < current_h :
                dp[r][c] += dfs(next_r,next_c)

    return dp[r][c]
    

M, N = map(int,sys.stdin.readline().split())
graph = []
move = [(-1,0),(1,0),(0,-1),(0,1)]
for _ in range(M) :
    x = list(map(int,sys.stdin.readline().split()))
    graph.append(x)
dp = [[-1 for _ in range(N)] for _ in range(M)]
print(dfs(0,0))