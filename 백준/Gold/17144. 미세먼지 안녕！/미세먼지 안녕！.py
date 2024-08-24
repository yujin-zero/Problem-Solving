import sys

def spreadDust() :
    tmp = [[0] * (c+1) for _ in range(r+1)]
    for i in range(1,r+1) :
        for j in range(1,c+1) :
            if graph[i][j] > 0 :
                cntSpread = 0
                Arc = graph[i][j] // 5
                for a, b in move :
                    x = i + a
                    y = j + b
                    if 1 <= x <= r and 1<= y <= c :
                        if graph[x][y] >= 0 :
                            cntSpread += 1
                            tmp[x][y] += Arc
                graph[i][j] -= (Arc * cntSpread)
    for i in range(1,r+1) :
        for j in range(1,c+1) :
            graph[i][j] += tmp[i][j]

def airCleaning() :
    for i in range(up-2,0,-1) :
        graph[i+1][1] = graph[i][1]
    for j in range(2,c+1) :
        graph[1][j-1] = graph[1][j]
    for i in range(2,up+1) :
        graph[i-1][c] = graph[i][c]
    for j in range(c-1,1,-1) :
        graph[up][j+1] = graph[up][j]

    for i in range(down+2,r+1) :
        graph[i-1][1] = graph[i][1]
    for j in range(2,c+1) :
        graph[r][j-1] = graph[r][j]
    for i in range(r-1,down-1,-1) :
        graph[i+1][c] = graph[i][c]
    for j in range(c-1,1,-1) :
        graph[down][j+1] = graph[down][j]
    graph[up][2] = 0
    graph[down][2] = 0

r, c, t = map(int,sys.stdin.readline().split())
graph = [[0] * (c+1) for _ in range(r+1)]
move = [(-1,0),(1,0),(0,-1),(0,1)]
up, down = -1 ,-1
for i in range(r) :
    x = list(map(int,sys.stdin.readline().split()))
    for j in range(c) :
        graph[i+1][j+1] = x[j]
        if x[j] == -1 :
            if up == -1 :
                up = i+1
            else :
                down = i+1

sec = 0
while True :
    spreadDust()
    airCleaning()

    sec += 1
    if sec == t :
        break

answer = 0
for g in graph :
    answer += sum(g)

print(answer+2)