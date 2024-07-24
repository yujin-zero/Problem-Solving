import sys
import heapq

def dijkstra(start) :
    dp = [float('inf')] * (n*n)
    dp[start] = 0
    queue = []
    heapq.heappush(queue,(0, start))

    while queue :
        nowCost, nowNode = heapq.heappop(queue)

        if nowCost > dp[nowNode] :
            continue

        for neighbor, weight in cost[nowNode] :
            dis = nowCost + weight
            if dis < dp[neighbor] :
                dp[neighbor] = dis
                heapq.heappush(queue,(dis,neighbor))

    return dp[n*n-1]
        

n = int(sys.stdin.readline())
graph = [[0]*n for _ in range(n)]
move = [(-1,0),(1,0),(0,-1),(0,1)]
for i in range(n) :
    x = sys.stdin.readline()
    for j in range(n) :
        value = int(x[j])
        if value == 0 :
            graph[i][j] = 1
        else :
            graph[i][j] = 0

cost = [[] for _ in range(n*n)] 
for i in range(n) :
    for j in range(n) :
        for x, y in move :
            a = i+x
            b = j+y
            if 0 <= a < n and 0 <= b < n :
                cost[i*n+j].append((a*n+b,graph[a][b]))

print(dijkstra(0))
