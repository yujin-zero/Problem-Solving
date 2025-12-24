import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
room_cnt = 0
big_room_size = 1
remove_size = 0
room_size = dict()

graph = []
for _ in range(M) :
    g = list(map(int, sys.stdin.readline().split()))
    graph.append(g)
visit = [[False for _ in range(N)] for _ in range(M)]

queue = deque()
queue.append((0,0))
visit[0][0] = True
room_cnt = 1
tmp_size = 1

while queue :
    x, y = queue.popleft()
    # print("x: ", x, "y: ",y)
    value = graph[x][y]
    graph[x][y] = room_cnt

    ## 동 4
    if value & 4 == 0 :
        # print("동")
        xx = x
        yy = y + 1

        if (0 <= xx < M) and (0 <= yy < N) :
            if not visit[xx][yy] :
                queue.append((xx,yy))
                visit[xx][yy] = True
                tmp_size += 1
                big_room_size = max(big_room_size, tmp_size)

    ## 서 1
    if value & 1 == 0 :
        # print("서")
        xx = x
        yy = y - 1

        if (0 <= xx < M) and (0 <= yy < N) :
            if not visit[xx][yy] :
                queue.append((xx,yy))
                visit[xx][yy] = True
                tmp_size += 1
                big_room_size = max(big_room_size, tmp_size)

    ## 남 8
    if value & 8 == 0 :
        # print("남")
        xx = x + 1
        yy = y

        if (0 <= xx < M) and (0 <= yy < N) :
            if not visit[xx][yy] :
                queue.append((xx,yy))
                visit[xx][yy] = True
                tmp_size += 1
                big_room_size = max(big_room_size, tmp_size)

    ## 북 2
    if value & 2 == 0 :
        # print("북")
        xx = x - 1
        yy = y

        if (0 <= xx < M) and (0 <= yy < N) :
            if not visit[xx][yy] :
                queue.append((xx,yy))
                visit[xx][yy] = True
                tmp_size += 1
                big_room_size = max(big_room_size, tmp_size)

    if not queue :
        tmp = False
        for i in range(M) :
            for j in range(N) :
                if not visit[i][j] :
                    queue.append((i,j))
                    visit[i][j] = True
                    room_size[room_cnt] = tmp_size
                    room_cnt += 1
                    # print(i, j)
                    # print(room_cnt)
                    # print("---------")
                    tmp = True
                    tmp_size = 1
                    break
            if tmp :
                break

print(room_cnt)
print(big_room_size)
room_size[room_cnt] = tmp_size

for i in range(M) :
    for j in range(N-1) :
        current = graph[i][j]
        right = graph[i][j+1]
        if current != right :
            t = room_size[current] + room_size[right]
            remove_size = max(remove_size, t)
for i in range(M-1) :
    for j in range(N) :
        current = graph[i][j]
        down = graph[i+1][j]
        if current != down :
            t = room_size[current] + room_size[down]
            remove_size = max(remove_size, t)

print(remove_size)