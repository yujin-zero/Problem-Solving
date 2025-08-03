import sys
from collections import deque

n = int(sys.stdin.readline())
ant_energy = [0] * (n+1)
next_room = [0] * (n+1)
for i in range(1, n+1):
    x = int(sys.stdin.readline())
    ant_energy[i] = x
graph = [dict() for _ in range(n+1)]
neighbor = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c
    graph[b][a] = c
    neighbor[a].append(b)
    neighbor[b].append(a)

queue = deque()
visit = [False] * (n+1)
queue.append(1)
visit[1] = True

while queue:
    current_room = queue.popleft()

    for next_value in neighbor[current_room]:
        if visit[next_value]:
            continue

        next_room[next_value] = current_room
        visit[next_value] = True
        queue.append(next_value)

for i in range(1, n+1):
    current_ant_energy = ant_energy[i]
    current_ant_room = i

    while True:
        if next_room[current_ant_room] == 0:
            print(1)
            break

        tmp_next = next_room[current_ant_room]
        tmp_value = graph[current_ant_room][tmp_next]
        if current_ant_energy - tmp_value < 0:
            print(current_ant_room)
            break

        current_ant_energy -= tmp_value
        current_ant_room = tmp_next
