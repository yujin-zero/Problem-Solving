import sys
import heapq

def dijkstra(start) :
    dp = [float('inf')] * (n*n)
    dp[start] = 0
    queue = []
    heapq.heappush(queue,(0,start))

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


move = [(-1,0),(1,0),(0,-1),(0,1)]

cnt = 1
while True :
    n = int(sys.stdin.readline())
    if n == 0 :
        break

    rupee = []
    for _ in range(n) :
        x = list(map(int,sys.stdin.readline().split()))
        rupee.append(x)

    cost = [[] for _ in range(n*n)]

    for i in range(n) :
        for j in range(n) :
            for x, y in move :
                a = i + x
                b = j + y
                if 0 <= a < n and 0 <= b < n :
                    cost[i*n+j].append((a*n+b,rupee[a][b])) 

    answer = dijkstra(0) + rupee[0][0]

    print("Problem %d: %d"%(cnt,answer))
    cnt += 1