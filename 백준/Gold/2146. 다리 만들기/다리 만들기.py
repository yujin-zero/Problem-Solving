import sys
from collections import deque

def find_island() : # 섬 찾기
    for i in range(N) :
        for j in range(N) :
            if graph[i][j] != 1 :
                continue
            
            queue = deque()
            queue.append((i,j))
            graph[i][j] = 2 # 방문처리
            current_islands = []
            current_islands.append((i,j))
            
            while queue :
                x, y = queue.popleft()

                for dx, dy in move :
                    new_x = x + dx
                    new_y = y + dy

                    if 0 <= new_x < N and 0 <= new_y < N :
                        if graph[new_x][new_y] == 1 :
                            queue.append((new_x,new_y))
                            graph[new_x][new_y] = 2
                            current_islands.append((new_x,new_y))

            island.append(current_islands)

def find_length(a,b) : # 섬 간 최소거리 구하기
    min_dis = float('inf')

    for x1, y1 in island[a] :
        for x2, y2 in island[b] :
            tmp = abs(x1-x2) + abs(y1-y2) - 1
            min_dis = min(min_dis,tmp)

    return min_dis


N = int(sys.stdin.readline())
graph = []
island = []
move = [(-1,0),(1,0),(0,-1),(0,1)]
answer = float('inf')
for _ in range(N) :
    x = list(map(int,sys.stdin.readline().split()))
    graph.append(x)

find_island()
island_cnt = len(island)

for land1 in range(island_cnt) :
    for land2 in range(land1+1,island_cnt) :
        dis = find_length(land1, land2)
        answer = min(answer,dis)

print(answer)