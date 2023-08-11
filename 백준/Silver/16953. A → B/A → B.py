import sys
import heapq

a, b = map(int, sys.stdin.readline().split())
num = {}
num[a] = 1
nextI = []
i = a
while (i*2 <= b) or (i*10+1 <= b):
    if i in num:
        if i*2 not in num:
            num[i*2] = num[i]+1
        else:
            num[i*2] = min(num[i*2], num[i]+1)
        heapq.heappush(nextI, i*2)

        if (i*10 + 1) not in num:
            num[i*10+1] = num[i]+1
        else:
            num[i*10+1] = min(num[i*10+1], num[i]+1)
        heapq.heappush(nextI, i*10+1)
    i = heapq.heappop(nextI)

if b in num:
    print(num[b])
else:
    print(-1)
