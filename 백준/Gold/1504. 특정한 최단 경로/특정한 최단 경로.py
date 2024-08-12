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

n, e = map(int,sys.stdin.readline().split())
cost = [[] for _ in range(n+1)]
for _ in range(e) :
    a,b,c = map(int,sys.stdin.readline().split())

    cost[a].append((b,c))
    cost[b].append((a,c))
v1, v2 = map(int,sys.stdin.readline().split())

startTo = dijkstra(1)
start_v1 = startTo[v1]
start_v2 = startTo[v2]

v1To = dijkstra(v1)
v1_v2 = v1To[v2]
v1_end = v1To[n]

v2To = dijkstra(v2)
v2_v1 = v2To[v1]
v2_end = v2To[n]

tmp1 = start_v1 + v1_v2 + v2_end
tmp2 = start_v2 + v2_v1 + v1_end
answer = min(tmp1, tmp2)

if answer == float('inf') :
    print(-1)
else :
    print(answer)