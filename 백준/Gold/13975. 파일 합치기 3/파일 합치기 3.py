import sys
import heapq

t = int(sys.stdin.readline())
for _ in range(t) :
    k = int(sys.stdin.readline())
    file = list(map(int,sys.stdin.readline().split()))
    answer = 0

    heap = []
    heapq.heapify(heap)
    for f in file :
        heapq.heappush(heap, f)

    while len(heap) > 1:
        tmp = heapq.heappop(heap)
        tmp += heapq.heappop(heap)
        answer += tmp
        heapq.heappush(heap, tmp)

    print(answer)
