import sys
import heapq

def dijkstra(start) :
    dp = [float('inf')] * (v+1)
    dp[start] = 0
    queue = []
    heapq.heappush(queue,(0,start))

    while queue :
        nowCost, nowNode = heapq.heappop(queue)

        if nowCost > dp[nowNode] :
            continue

        for nextNode, weight in cost[nowNode] :
            dis = nowCost + weight
            if dis < dp[nextNode] :
                dp[nextNode] = dis 
                heapq.heappush(queue,(dis, nextNode))

    return dp


v, e, p = map(int,sys.stdin.readline().split())
cost = [[] for _ in range(v+1)]
for _ in range(e) :
    a, b, c = map(int,sys.stdin.readline().split())

    cost[a].append((b,c))
    cost[b].append((a,c))

tmp = dijkstra(1)
goHome, goGunwoo = tmp[v], tmp[p]
takeGunwoo = goGunwoo + dijkstra(p)[v]

if goHome == takeGunwoo :
    print("SAVE HIM")
else :
    print("GOOD BYE")