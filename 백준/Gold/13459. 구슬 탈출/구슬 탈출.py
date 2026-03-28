import sys
from collections import deque
import copy


def find_R_B(graph, n, m):
    rx, ry, bx, by = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'R':
                rx, ry = i, j
            elif graph[i][j] == 'B':
                bx, by = i, j

    return (rx, ry, bx, by)


def move_ball(graph, type, x, y, dx, dy):
    while True:
        new_x = x + dx
        new_y = y + dy

        if graph[new_x][new_y] == '#':
            break
        elif graph[new_x][new_y] == 'O':
            graph[x][y] = '.'
            break
        elif graph[new_x][new_y] == '.':
            graph[x][y] = '.'
            x, y = new_x, new_y
            graph[x][y] = type
        else:
            break

    return graph


def move_right(graph, n, m):
    rx, ry, bx, by = find_R_B(graph, n, m)

    if ry > by:
        graph = move_ball(graph, 'R', rx, ry, 0, 1)
        graph = move_ball(graph, 'B', bx, by, 0, 1)
    else:
        graph = move_ball(graph, 'B', bx, by, 0, 1)
        graph = move_ball(graph, 'R', rx, ry, 0, 1)

    return graph


def move_left(graph, n, m):
    rx, ry, bx, by = find_R_B(graph, n, m)

    if ry < by:
        graph = move_ball(graph, 'R', rx, ry, 0, -1)
        graph = move_ball(graph, 'B', bx, by, 0, -1)
    else:
        graph = move_ball(graph, 'B', bx, by, 0, -1)
        graph = move_ball(graph, 'R', rx, ry, 0, -1)

    return graph


def move_up(graph, n, m):
    rx, ry, bx, by = find_R_B(graph, n, m)

    if rx < bx:
        graph = move_ball(graph, 'R', rx, ry, -1, 0)
        graph = move_ball(graph, 'B', bx, by, -1, 0)
    else:
        graph = move_ball(graph, 'B', bx, by, -1, 0)
        graph = move_ball(graph, 'R', rx, ry, -1, 0)

    return graph


def move_down(graph, n, m):
    rx, ry, bx, by = find_R_B(graph, n, m)

    if rx > bx:
        graph = move_ball(graph, 'R', rx, ry, 1, 0)
        graph = move_ball(graph, 'B', bx, by, 1, 0)
    else:
        graph = move_ball(graph, 'B', bx, by, 1, 0)
        graph = move_ball(graph, 'R', rx, ry, 1, 0)

    return graph


answer = 0
N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    x = list(sys.stdin.readline().rstrip())
    graph.append(x)

queue = deque()
queue.append((graph, 0))
visit = []

while queue:
    current_graph, cnt = queue.popleft()

    if cnt > 10:
        break

    Rx, Ry, Bx, By = find_R_B(current_graph, N, M)
    if Rx == -1 and Bx != -1:
        answer = 1
        break
    elif Bx == -1:
        continue
    elif (Rx, Ry, Bx, By) in visit:
        continue

    visit.append((Rx, Ry, Bx, By))

    queue.append((move_up(copy.deepcopy(current_graph), N, M), cnt+1))
    queue.append((move_down(copy.deepcopy(current_graph), N, M), cnt+1))
    queue.append((move_left(copy.deepcopy(current_graph), N, M), cnt+1))
    queue.append((move_right(copy.deepcopy(current_graph), N, M), cnt+1))

print(answer)
