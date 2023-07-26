import sys
import heapq

n = int(sys.stdin.readline())
lst = []
result = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if lst:
            result.append(heapq.heappop(lst))
        else:
            result.append(0)
    else:
        heapq.heappush(lst, x)

for r in result:
    print(r)
