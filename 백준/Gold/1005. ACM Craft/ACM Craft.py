import sys
from collections import deque

t = int(sys.stdin.readline())
answer = []
for _ in range(t) :
    n, k = map(int,sys.stdin.readline().split())
    Dlist = list(map(int,sys.stdin.readline().split()))
    degree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    before = [[] for _ in range(n+1)]
    queue = deque()
    dp = [-1] * (n+1)

    for _ in range(k) :
        x, y = map(int,sys.stdin.readline().split())
        degree[y] += 1
        graph[x].append(y)
        before[y].append(x)

    xNode = int(sys.stdin.readline())

    for i in range(1,n+1) :
        if degree[i] == 0 :
            queue.append(i)

    while queue :
        currentNode = queue.popleft()
        tmp = 0 
        for beforeNode in before[currentNode] :
            tmp = max(tmp, dp[beforeNode])
        dp[currentNode] = tmp + Dlist[currentNode-1]

        for nextNode in graph[currentNode] :
            degree[nextNode] -= 1
            if degree[nextNode] == 0 :
                queue.append(nextNode)

    answer.append(dp[xNode])
    
for a in answer :
    print(a)