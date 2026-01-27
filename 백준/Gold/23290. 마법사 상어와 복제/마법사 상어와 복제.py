import sys
from collections import deque

def copy_graph() :
    for i in range(1, 5) :
        for j in range(1, 5) :
            graph_tmp[i][j] = graph[i][j]

def find_next(i, j, d) :
    if d == 1 :
        return i, j-1
    elif d == 2 :
        return i-1, j-1
    elif d == 3 :
        return i-1, j
    elif d == 4 :
        return i-1, j+1
    elif d == 5 :
        return i, j+1
    elif d == 6 :
        return i+1, j+1
    elif d == 7 :
        return i+1, j
    else :
        return i+1, j-1

def move_fish() :
    for i in range(1,5) :
        for j in range(1,5) :
            for d in graph[i][j] : ## 각각의 물고기의 방향
                first_d = d
                while True :
                    next_i, next_j  = find_next(i, j, d)

                    can_move = True
                    if next_i == sx and next_j == sy :
                        can_move = False
                    elif not (1 <= next_i < 5 and 1 <= next_j < 5) :
                        can_move = False
                    elif fish_smell[next_i][next_j] > 0 :
                        can_move = False

                    if can_move :
                        fish_queue.append((next_i, next_j, d))
                        break
                    else :
                        d -= 1
                        if d == 0:
                            d = 8

                    if d == first_d :
                        fish_queue.append((i, j, d))
                        break

def find_next_shark(x, y, d) :
    if d == 1 :
        x -= 1
    elif d == 2 :
        y -= 1
    elif d == 3 :
        x += 1
    else :
        y += 1
    
    return x, y

def move_shark(x, y) :
    find_road = [(0,0), (0,0), (0,0)]
    max_fish = -1
    for i in range(1, 5) :
        x1, y1 = find_next_shark(x, y, i)
        if not (1 <= x1 < 5 and 1 <= y1 < 5) :
            continue
        for j in range(1, 5) :
            x2, y2 = find_next_shark(x1, y1, j)
            if not (1 <= x2 < 5 and 1 <= y2 < 5) :
                continue
            for k in range(1, 5) :
                x3, y3 = find_next_shark(x2, y2, k)
                if not (1 <= x3 < 5 and 1 <= y3 < 5) :
                    continue

                tmp_fish = len(graph[x1][y1]) + len(graph[x2][y2]) + len(graph[x3][y3])
                if x1 == x3 and y1 == y3 :
                    tmp_fish -= len(graph[x1][y1])
                if tmp_fish > max_fish :
                    max_fish = tmp_fish
                    find_road = [(x1, y1), (x2, y2), (x3, y3)]

    return find_road

M, S = map(int, sys.stdin.readline().split())
graph = [[[] for _ in range(5)] for _ in range(5)]
graph_tmp = [[[] for _ in range(5)] for _ in range(5)] ## 현재 물고기들 복사해두기
fish_smell = [[0 for _ in range(5)] for _ in range(5)]
fish_queue = deque()
for _ in range(M) :
    fx, fy, d = map(int, sys.stdin.readline().split())
    graph[fx][fy].append(d)
sx, sy = map(int, sys.stdin.readline().split())

for _ in range(S) :
    ## 1
    copy_graph()

    ## 2
    move_fish()
    graph = [[[] for _ in range(5)] for _ in range(5)]
    while fish_queue :
        fish_x ,fish_y, fish_d = fish_queue.popleft()
        graph[fish_x][fish_y].append(fish_d)

    ## 3
    shark_move_list = move_shark(sx, sy)
    for mx, my in shark_move_list :
        if len(graph[mx][my]) > 0 :
            fish_smell[mx][my] = 3
            graph[mx][my] = []
    sx, sy = shark_move_list[2]

    ## 4
    for i in range(1, 5) :
        for j in range(1, 5) :
            if fish_smell[i][j] > 0 :
                fish_smell[i][j] -= 1

    ## 5
    for i in range(1, 5) :
        for j in range(1, 5) :
            for d in graph_tmp[i][j] :
                graph[i][j].append(d)

answer = 0
for i in range(1, 5) :
    for j in range(1, 5) :
        answer += len(graph[i][j])

print(answer)