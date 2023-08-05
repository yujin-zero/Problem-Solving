import sys
import heapq

n = int(sys.stdin.readline())
heapPositive = []
heapNegative = []
heapq.heapify(heapPositive)
heapq.heapify(heapNegative)
result = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(heapPositive, x)
    elif x < 0:
        heapq.heappush(heapNegative, -x)
    else:
        if heapPositive and heapNegative:
            p = heapPositive[0]
            n = heapNegative[0]
            if p < n:
                result.append(heapq.heappop(heapPositive))
            else:
                result.append(-heapq.heappop(heapNegative))
        elif heapPositive:
            result.append(heapq.heappop(heapPositive))
        elif heapNegative:
            result.append(-heapq.heappop(heapNegative))
        else:
            result.append(0)

for r in result:
    print(r)
