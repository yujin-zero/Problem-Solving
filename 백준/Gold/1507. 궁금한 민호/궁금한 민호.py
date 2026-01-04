import sys
import heapq

N = int(sys.stdin.readline())
graph = [[0 for _ in range(N)] for _ in range(N)]
answer_graph = [[float('inf') for _ in range(N)] for _ in range(N)]
for i in range(N) :
    answer_graph[i][i] = 0
road = []
for i in range(N) :
    x = list(map(int, sys.stdin.readline().split()))
    for j in range(N) :
        graph[i][j] = x[j]
heap = []

for i in range(N) :
    for j in range(i+1, N) :
        dis = graph[i][j]
        heapq.heappush(heap, (dis, i,j))

possible = True
while heap and possible :
    dis, x, y = heapq.heappop(heap)
    # print("------")
    # print("dis: ", dis)
    # print("x: ", x)
    # print("y: ",y)

    tmp = answer_graph[x][y]
    if dis < tmp :
        # print("111")
        road.append((dis, x, y))
        answer_graph[x][y] = dis
        answer_graph[y][x] = dis

        # 플로이드 워셜
        for k in range(N) :
            for i in range(N) :
                for j in range(N) :
                    if answer_graph[i][j] > answer_graph[i][k] + answer_graph[k][j] :
                        answer_graph[i][j] = answer_graph[i][k] + answer_graph[k][j]
    elif dis > tmp :
        # print("222")
        possible = False

    # for aa in answer_graph :
    #     print(aa)

if possible :
    answer = 0
    for a,b,c in road :
        answer += a
    print(answer)
    # print(road)
else :
    print(-1)