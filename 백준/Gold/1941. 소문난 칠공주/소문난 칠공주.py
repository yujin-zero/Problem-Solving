import sys
from itertools import combinations
from collections import deque

answer = 0
move = [(-1,0),(1,0),(0,-1),(0,1)]
dasom = []
doyeon = []
for i in range(5) :
    t = list(sys.stdin.readline().rstrip())

    for j in range(5) :
        if t[j] == 'S' :
            dasom.append((i,j))
        else :
            doyeon.append((i,j))
dasom_cnt = len(dasom)
graph = [[False for _ in range(5)] for _ in range(5)]

for a in range(4, 8) :
    if a > dasom_cnt :
        break
    b = 7 - a

    for dasom_list in combinations(dasom, a) :
        for x, y in dasom_list :
            graph[x][y] = True

        for doyeon_list in combinations(doyeon, b) :
            for xx, yy in doyeon_list :
                graph[xx][yy] = True

            ## 여기다
            visit = []
            queue = deque()
            queue.append((x, y))
            visit.append((x, y))

            while queue :
                cx, cy = queue.popleft()

                for dx, dy in move :
                    nx = cx + dx
                    ny = cy + dy

                    if (0 <= nx < 5) and (0 <= ny < 5) :
                        if graph[nx][ny] and (nx, ny) not in visit :
                            queue.append((nx, ny))
                            visit.append((nx, ny))
            
            if len(visit) == 7 :
                answer += 1

            for xx, yy in doyeon_list :
                graph[xx][yy] = False
        for x, y in dasom_list :
            graph[x][y] = False

print(answer)