import sys
from collections import deque

n = int(sys.stdin.readline())
buildTime = [0]
beforeBuild = [[] for _ in range(n+1)]
afterBuild = [[] for _ in range(n+1)]
degree = [0] * (n+1)
queue = deque()
dp = [0] * (n+1)

for j in range(n) :
    x = list(map(int,sys.stdin.readline().split()))
    for i in range(len(x)-1) :
        if i == 0 :
            buildTime.append(x[i])
        else :
            beforeBuild[j+1].append(x[i])
            afterBuild[x[i]].append(j+1)
            degree[j+1] += 1

for i in range(1,n+1) :
    if degree[i] == 0 :
        queue.append(i)

while queue :
    currentNode = queue.popleft()
    tmp = 0
    for beforeNode in beforeBuild[currentNode] :
        tmp = max(tmp, dp[beforeNode])
    dp[currentNode] = tmp + buildTime[currentNode]
    
    for nextnode in afterBuild[currentNode] :
        degree[nextnode] -= 1
        if degree[nextnode] == 0 :
            queue.append(nextnode)
     

for i in range(1,n+1) :
    print(dp[i])

