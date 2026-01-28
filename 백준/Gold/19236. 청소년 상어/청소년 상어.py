import sys
import copy


def find_next(i, j, d):
    if d == 1:
        return i-1, j
    elif d == 2:
        return i-1, j-1
    elif d == 3:
        return i, j-1
    elif d == 4:
        return i+1, j-1
    elif d == 5:
        return i+1, j
    elif d == 6:
        return i+1, j+1
    elif d == 7:
        return i, j+1
    else:
        return i-1, j+1


def move_turn(shark_x, shark_y, shark_d, sum_eat, c_graph, c_location):
    global answer

    # 물고기 이동
    for i in range(1, 17):
        if not c_location[i]:
            continue
        fish_x, fish_y = c_location[i]
        fish_n, fish_d = c_graph[fish_x][fish_y]
        next_x, next_y = find_next(fish_x, fish_y, fish_d)
        first_d = fish_d

        while True:
            if not ((next_x == shark_x and next_y == shark_y) or not (0 <= next_x < 4 and 0 <= next_y < 4)):
                # 이동
                c_graph[fish_x][fish_y] = [fish_n, fish_d]
                if c_graph[next_x][next_y]:
                    t_x, t_y = c_graph[next_x][next_y]
                    c_graph[next_x][next_y] = c_graph[fish_x][fish_y]
                    c_graph[fish_x][fish_y] = [t_x, t_y]
                    t_l = c_location[t_x]
                    c_location[t_x] = c_location[fish_n]
                    c_location[fish_n] = t_l
                else:
                    c_graph[next_x][next_y] = c_graph[fish_x][fish_y]
                    c_graph[fish_x][fish_y] = []
                    c_location[fish_n] = [next_x, next_y]
                break

            # 이동 못함
            fish_d += 1
            if fish_d == 9:
                fish_d = 1
            if first_d == fish_d:
                break

            next_x, next_y = find_next(fish_x, fish_y, fish_d)

    # 상어 이동
    move_list = []
    next_x, next_y = find_next(shark_x, shark_y, shark_d)
    while True:
        if not (0 <= next_x < 4 and 0 <= next_y < 4):
            break
        if len(c_graph[next_x][next_y]) > 0:
            move_list.append((next_x, next_y))
        next_x, next_y = find_next(next_x, next_y, shark_d)

    if not move_list:
        answer = max(answer, sum_eat)
        return
    for ml in move_list:
        cc_graph = copy.deepcopy(c_graph)
        cc_location = copy.deepcopy(c_location)
        next_x, next_y = ml

        eat_num = cc_graph[next_x][next_y][0]
        tmp_eat = sum_eat + eat_num
        shark_x, shark_y = next_x, next_y
        shark_d = cc_graph[next_x][next_y][1]
        cc_graph[shark_x][shark_y] = []
        cc_location[eat_num] = []
        move_turn(shark_x, shark_y, shark_d, tmp_eat, cc_graph, cc_location)


answer = 0
graph = [[[0, 0] for _ in range(4)] for _ in range(4)]
location_fish = [[-1, -1] for _ in range(17)]
for i in range(4):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(0, 8, 2):
        graph[i][j//2][0] = lst[j]
        graph[i][j//2][1] = lst[j+1]
        location_fish[lst[j]] = [i, j//2]

Sx, Sy = 0, 0
Sd = graph[0][0][1]
sum_eat = graph[0][0][0]
graph[0][0] = []
location_fish[sum_eat] = []
move_turn(Sx, Sy, Sd, sum_eat, copy.deepcopy(
    graph), copy.deepcopy(location_fish))

print(answer)
