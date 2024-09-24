import sys
import queue

n, k = map(int,sys.stdin.readline().split())
gem = []
bag = []
answer = 0
priority_queue = queue.PriorityQueue() 
for _ in range(n) :
    m, v = map(int,sys.stdin.readline().split())
    gem.append((m,v)) # 무게, 가격
for _ in range(k) :
    c = int(sys.stdin.readline())
    bag.append(c)

bag.sort()
gem.sort() # 보석 무게가 가벼운 순으로 정렬
i = 0

for b in bag :
    while i < n :
        if gem[i][0] <= b :
            priority_queue.put(-gem[i][1])
        else :
            break
        i += 1
    
    if not priority_queue.empty() :
        answer += priority_queue.get()

print(-answer)