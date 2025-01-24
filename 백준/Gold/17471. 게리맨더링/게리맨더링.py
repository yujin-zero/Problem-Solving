import sys
from itertools import combinations
from collections import deque

def BFS(x) :
    visit = [False] * (N+1)
    queue = deque()
    queue.append(x[0])
    visit[x[0]] = True
    cnt = 1

    while queue :
        current = queue.popleft()

        for next in graph[current] :
            if not visit[next] and next in x :
                queue.append(next)
                visit[next] = True
                cnt += 1

    if cnt == len(x) :
        return True
    
    return False


N = int(sys.stdin.readline())
population = [0] + list(map(int,sys.stdin.readline().split()))
graph = [[] for _ in range(N+1)]
for i in range(1,N+1) :
    x = list(map(int,sys.stdin.readline().split()))
    for j in range(1,x[0]+1) :
        graph[i].append(x[j])
answer = float('inf')
gu = [i for i in range(1,N+1)]

i = 1
while i <= N//2 :

    for A in combinations(gu,i) :
        a = []
        b = []
        for j in range(1,N+1) :
            if j in A :
                a.append(j)
            else :
                b.append(j)

        connect_a = BFS(a)
        connect_b = BFS(b)

        if connect_a and connect_b :
            t1, t2 = 0, 0
            for k in range(1,N+1) :
                if k in a :
                    t1 += population[k]
                else :
                    t2 += population[k]

            answer = min(answer, abs(t1-t2))
    i += 1

if answer == float('inf') :
    print(-1)
else :
    print(answer)