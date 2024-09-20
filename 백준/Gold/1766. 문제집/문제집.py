import sys
import queue

n, m = map(int,sys.stdin.readline().split())
degree = [0] * (n+1)
afterSolve = [[] for _ in range(n+1)]
priority_queue = queue.PriorityQueue()
answer = []
for _ in range(m) :
    a, b = map(int,sys.stdin.readline().split())
    degree[b] += 1
    afterSolve[a].append(b)

for i in range(1,n+1) :
    if degree[i] == 0 :
        priority_queue.put(i)

while not priority_queue.empty() :
    current = priority_queue.get()
    answer.append(current)
    
    for nextP in afterSolve[current] :
        degree[nextP] -= 1
        if degree[nextP] == 0 :
            priority_queue.put(nextP)

for a in answer :
    print(a, end=' ')

