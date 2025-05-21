import sys

N, M = map(int, sys.stdin.readline().split())
dist = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
long_dist = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    S, E, L = map(int, sys.stdin.readline().split())

    if L < dist[S][E]:
        dist[S][E] = L
        dist[E][S] = L

    if L > long_dist[S][E]:
        long_dist[S][E] = L
        long_dist[E][S] = L

for i in range(1, N+1):
    dist[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

answer = float('inf')
for start in range(1, N+1):
    finish = 0
    for i in range(1, N+1):
        for j in range(i, N+1):
            if long_dist[i][j] == 0:
                continue

            big = max(dist[start][i], dist[start][j])
            small = min(dist[start][i], dist[start][j])

            t = big + (long_dist[i][j] - big + small) / 2
            finish = max(finish, t)

    answer = min(answer, finish)

print(answer)