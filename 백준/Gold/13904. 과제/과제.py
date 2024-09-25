import sys
import heapq

n = int(sys.stdin.readline())
task = []
heap = []
score = 0
heapq.heapify(heap)
for _ in range(n) :
    d, w = map(int,sys.stdin.readline().split())
    task.append((d,w)) # 남은일수, 과제점수

task.sort(key= lambda x: -x[0])
i = task[0][0]
j = 0

while i > 0 :
    while j < n :
        if task[j][0] >= i :
            heapq.heappush(heap, -task[j][1])
            j += 1
        else :
            break

    if heap :
        s = heapq.heappop(heap)
        score += s

    i -= 1

print(-score)