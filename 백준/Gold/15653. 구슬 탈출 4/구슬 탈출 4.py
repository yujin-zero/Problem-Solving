import sys
import copy


def move_ball(graph, direction, rx, ry, bx, by, move_cnt):
    global answer

    dx, dy = move[direction]

    red_goal = False
    blue_goal = False

    while True:
        red_move = False
        blue_move = False

        nrx = rx + dx
        nry = ry + dy

        if not red_goal:
            if graph[nrx][nry] == '.':
                red_move = True
                graph[rx][ry] = '.'
                rx, ry = nrx, nry
                graph[rx][ry] = 'R'
            elif graph[nrx][nry] == 'O':
                red_move = True
                red_goal = True
                graph[rx][ry] = '.'

        nbx = bx + dx
        nby = by + dy

        if not blue_goal:
            if graph[nbx][nby] == '.':
                blue_move = True
                graph[bx][by] = '.'
                bx, by = nbx, nby
                graph[bx][by] = 'B'
            elif graph[nbx][nby] == 'O':
                blue_move = True
                blue_goal = True
                graph[bx][by] = '.'

        if not red_move and not blue_move:
            break

    if blue_goal:
        return
    elif red_goal:
        answer = min(answer, move_cnt+1)
    else:
        # 이동
        if (rx, ry, bx, by) not in visit:
            visit.append((rx, ry, bx, by))
            move_cnt_dict[(rx, ry, bx, by)] = move_cnt + 1
            for i in range(4):
                move_ball(copy.deepcopy(graph), i, rx,
                          ry, bx, by, move_cnt + 1)
        else:
            if move_cnt+1 < move_cnt_dict[(rx, ry, bx, by)]:
                move_cnt_dict[(rx, ry, bx, by)] = move_cnt + 1
                for i in range(4):
                    move_ball(copy.deepcopy(graph), i, rx,
                              ry, bx, by, move_cnt + 1)


N, M = map(int, sys.stdin.readline().split())
answer = float('inf')
graph1 = []
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
rx, ry, bx, by = -1, -1, -1, -1
move_cnt_dict = dict()
visit = []
for i in range(N):
    g = list(sys.stdin.readline().strip())
    graph1.append(g)
    for j in range(M):
        if g[j] == 'R':
            rx, ry = i, j
        elif g[j] == 'B':
            bx, by = i, j

for i in range(4):
    visit.append((rx, ry, bx, by))
    move_cnt_dict[(rx, ry, bx, by)] = 0
    move_ball(copy.deepcopy(graph1), i, rx, ry, bx, by, 0)

if answer == float('inf'):
    print(-1)
else:
    print(answer)
