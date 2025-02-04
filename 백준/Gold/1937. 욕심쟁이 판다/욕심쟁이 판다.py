import sys
import heapq

n = int(sys.stdin.readline())
graph = []
heap = []
answer = 0
dp = [[-1 for _ in range(n)] for _ in range(n)]
move = [(-1,0),(1,0),(0,-1),(0,1)]
for i in range(n) :
    x = list(map(int,sys.stdin.readline().split()))
    graph.append(x)
    for j in range(n) :
        heapq.heappush(heap, (-x[j],i,j))

while heap :
    value, x, y = heapq.heappop(heap)

    tmp = 1
    for dx, dy in move :
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < n and 0 <= next_y < n :
            if graph[next_x][next_y] > -value :
                tmp = max(tmp, 1+dp[next_x][next_y])
    dp[x][y] = tmp
    answer = max(answer,tmp)
    
print(answer)