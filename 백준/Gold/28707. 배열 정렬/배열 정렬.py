import sys
import heapq

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
cost = []
for _ in range(M) :
    l, r ,c = map(int,sys.stdin.readline().split())
    cost.append((l-1,r-1,c))

answer = sorted(A)
for i in range(N) :
    if answer[i] == 10 :
        answer[i] = 0
answer = int(''.join(map(str,answer)))

for i in range(N) :
    if A[i] == 10 :
        A[i] = 0
A = int(''.join(map(str,A)))

queue = []
dp = [float('inf')] * (10**N)
dp[A] = 0
heapq.heappush(queue, (0,A))

while queue :
    now_cost, now_node = heapq.heappop(queue)

    if now_cost > dp[now_node] :
        continue

    for l, r, c in cost :
        next_node = list(str(now_node))
        if len(next_node) != N :
            n_node = ['0'] * N
            for i in range(len(next_node)-1,-1,-1) :
                n_node[i+(N-len(next_node))] = next_node[i]
            next_node = n_node

        tmp = next_node[l]
        next_node[l] = next_node[r]
        next_node[r] = tmp
        next_node = int(''.join(map(str,next_node)))
        dis = now_cost + c
        if dis < dp[next_node] :
            dp[next_node] = dis
            heapq.heappush(queue, (dis,next_node))

if dp[answer] == float('inf') :
    print(-1)
else :
    print(dp[answer])