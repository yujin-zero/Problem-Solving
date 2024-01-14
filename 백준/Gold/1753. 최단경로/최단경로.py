import sys
import heapq
v, e = map(int, sys.stdin.readline().split())
startNode = int(sys.stdin.readline())
q = []
heapq.heappush(q, (0, startNode))
graph = [[]for _ in range(v+1)]
max_number = float('inf')
cost = dict()
for i in range(1, v+1):
    cost[i] = float('inf')
cost[startNode] = 0

for _ in range(e):
    start, end, w = map(int, sys.stdin.readline().split())
    graph[start].append([end, w])


while q:
    co, now = heapq.heappop(q)
    if cost[now] < co:
        continue
    for node in graph[now]:
        if co + node[1] < cost[node[0]]:
            cost[node[0]] = co+node[1]
            heapq.heappush(q, (co+node[1], node[0]))

    # for tmp in graph[startNode]:
    #     node, ga = tmp[0], tmp[1]
    #     if cost[node] > cost[startNode] + ga:
    #         cost[node] = cost[startNode]+ga
    # if len(visit) == v:
    #     break
    # tmpCost = float('inf')
    # for i in range(1, v+1):
    #     if i not in visit:
    #         if cost[i] < tmpCost:
    #             startNode = i
    # visit.add(startNode)

for i in range(1, v+1):
    if cost[i] == float('inf'):
        print("INF")
    else:
        print(cost[i])
