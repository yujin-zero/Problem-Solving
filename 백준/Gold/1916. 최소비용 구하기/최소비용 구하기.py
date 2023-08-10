import sys
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    cost[start] = 0
    while q:
        co, now = heapq.heappop(q)  # 가장 비용이 적은 노드에 대한 정보
        if cost[now] < co:
            continue  # 이미 처리된 적이 있는 노드라면 무시

        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for node in graph[now]:
            if co + node[1] < cost[node[0]]:
                cost[node[0]] = co + node[1]
                heapq.heappush(q, (co+node[1], node[0]))


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담은 리스트
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

start, stop = map(int, sys.stdin.readline().split())
cost = [float('inf')] * (n+1)

dijkstra(start)
print(cost[stop])
