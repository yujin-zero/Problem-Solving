import sys

n = int(sys.stdin.readline())
dist = [[float('inf')] * n for _ in range(n)]
score = [0] * n
answer = []
cnt = 0
for i in range(n):
    dist[i][i] = 0

while True :
    a, b = map(int,sys.stdin.readline().split())
    if a == -1 and b == -1 :
        break

    dist[a-1][b-1] = 1
    dist[b-1][a-1] = 1

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if dist[i][j] > dist[i][k] + dist[k][j] :
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(n) :
    score[i] = max(dist[i])

tmp = min(score)
for i in range(n) :
    if score[i] == tmp :
        cnt += 1
        answer.append(i+1)

print(tmp, cnt)
print(*answer)

