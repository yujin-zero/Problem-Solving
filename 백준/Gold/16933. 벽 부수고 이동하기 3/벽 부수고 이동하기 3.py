import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
answer = float('inf')
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
graph = []
for _ in range(N):
    x = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(x)

visit = [[-1 for _ in range(M)] for _ in range(N)]
queue = deque()
queue.append((0, 0, 1, K, True))  # row, col, distance, cnt, day
visit[0][0] = K

while queue:
    x, y, dis, cnt, is_day = queue.popleft()

    if x == N-1 and y == M-1:
        answer = dis
        break

    if cnt < visit[x][y]:
        continue

    for dx, dy in move:
        new_x = x + dx
        new_y = y + dy

        if not (0 <= new_x < N and 0 <= new_y < M):
            continue

        value = graph[new_x][new_y]
        if value == 0:
            if cnt > visit[new_x][new_y]:
                visit[new_x][new_y] = cnt
                queue.append((new_x, new_y, dis+1, cnt, not is_day))
        elif is_day:
            if cnt == 0:
                continue

            if cnt-1 > visit[new_x][new_y]:
                visit[new_x][new_y] = cnt-1
                queue.append((new_x, new_y, dis+1, cnt-1, False))
        if not is_day:
            queue.append((x, y, dis+1, cnt, True))

if answer == float('inf'):
    print(-1)
else:
    print(answer)
