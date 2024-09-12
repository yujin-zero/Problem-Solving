import sys
import heapq

def dijstra(start) :
    dp = [float('inf')] * (n+1)
    dp[start] = 0
    city = [[] for _ in range(n+1)]
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
                city[neighbor] = []
                for x in city[nowNode] :
                    city[neighbor].append(x)
                city[neighbor].append(nowNode)
                heapq.heappush(queue, (dis, neighbor))

    city[end].append(end)
    return dp[end], city[end]

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
cost = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b, c = map(int,sys.stdin.readline().split())
    cost[a].append((b,c))
start, end = map(int,sys.stdin.readline().split())

answerCost, answerPath = dijstra(start)
print(answerCost)
print(len(answerPath))
print(*answerPath)