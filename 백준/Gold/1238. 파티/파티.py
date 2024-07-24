import sys
import heapq


def dijkstra(start) :
    dp = [float('inf')] * (n+1)
    dp[start] = 0
    queue = []
    heapq.heappush(queue, (0,start))

    while queue :
        nowCost, nowNode = heapq.heappop(queue)

        if nowCost > dp[nowNode] :
            continue
            
        for neighbor, weight in cost[nowNode] :
            dis = nowCost + weight
            if dis < dp[neighbor] :
                dp[neighbor] = dis
                heapq.heappush(queue, (dis,neighbor))

    return dp


n, m, x = map(int,sys.stdin.readline().split())
cost = [[] for _ in range(n+1)]
answer = 0

for _ in range(m) :
    a, b, t = map(int,sys.stdin.readline().split())
    cost[a].append((b,t))

toHome = dijkstra(x)

for i in range(1,n+1) :
    if i != x :
        if dijkstra(i)[x] + toHome[i] > answer :
            answer = dijkstra(i)[x] + toHome[i]

print(answer)