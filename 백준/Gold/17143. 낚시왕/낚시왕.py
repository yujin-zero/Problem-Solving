import sys

R, C, M = map(int,sys.stdin.readline().split())
shark = []
shark_pos = []
alive = set(range(M))
graph = [[[] for _ in range(C)] for _ in range(R)]
for i in range(M) :
    r, c, s, d, z = map(int,sys.stdin.readline().split())
    graph[r-1][c-1].append(i)
    shark.append([s,d,z])
    shark_pos.append([r-1,c-1])
answer = 0
go = [(0,0),(-1,0),(1,0),(0,1),(0,-1)]

current_col = -1
while True : 
    ## 낚시왕이 오른쪽으로 한 칸 이동한다.
    current_col += 1
    if current_col == C :
        break

    ## 현재 열에서 땅과 가장 가까운 상어 잡기
    for i in range(R) :
        if len(graph[i][current_col]) > 0 : 
            get_shark = graph[i][current_col][0] 
            answer += shark[get_shark][2]
            graph[i][current_col].remove(get_shark)
            alive.remove(get_shark)
            break

    ## 상어 이동
    for current_shark in alive :
        current_x, current_y = shark_pos[current_shark][0], shark_pos[current_shark][1]
        move_way = shark[current_shark][1]
        dx, dy = go[move_way]
        move_cnt = shark[current_shark][0]
        move_cnt = shark[current_shark][0]
        if move_way in [1, 2] :
            move_cnt %= (2 * (R - 1))
        else :
            move_cnt %= (2 * (C - 1))
        move_tmp = 0
        graph[current_x][current_y].remove(current_shark)
        next_x, next_y = current_x, current_y
        while move_tmp < move_cnt :
            next_x = current_x + dx
            next_y = current_y + dy
            if 0 <= next_x < R and 0 <= next_y < C :
                current_x = next_x
                current_y = next_y
                shark_pos[current_shark][0] = current_x
                shark_pos[current_shark][1] = current_y
                move_tmp += 1
            else :
                dx *= -1
                dy *= -1
                if move_way == 1 :
                    move_way = 2
                elif move_way == 2 :
                    move_way = 1
                elif move_way == 3 :
                    move_way = 4
                else :
                    move_way = 3
                shark[current_shark][1] = move_way
        graph[next_x][next_y].append(current_shark)

    ## 상어 잡아먹기
    for i in range(R) :
        for j in range(C) :
            if len(graph[i][j]) > 1 :
                big_shark = max(graph[i][j], key=lambda x: shark[x][2])  # 가장 큰 상어 찾기
                for other_shark in graph[i][j]:
                    if other_shark != big_shark:
                        alive.discard(other_shark)
                graph[i][j] = [big_shark]
 
print(answer)