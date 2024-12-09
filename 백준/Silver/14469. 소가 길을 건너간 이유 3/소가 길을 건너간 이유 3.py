import sys
import heapq

N = int(sys.stdin.readline())
cows = []
visit = [False] * N
for _ in range(N) :
    a, b = map(int,sys.stdin.readline().split())
    cows.append([a,b])

time = 0
able_cows = []
cnt = 0

while True :
    for i in range(N) :
        if not visit[i] :
            if cows[i][0] <= time :
                visit[i] = True
                # able_cows.append(cows[i][1])
                heapq.heappush(able_cows,cows[i][1])

    if able_cows :
        value = heapq.heappop(able_cows)
        time += value
        cnt += 1
        if cnt == N :
            break
    else :
        time += 1
    

print(time)
