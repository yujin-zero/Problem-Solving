import sys
from collections import deque

def BFS() :
    visit = [[False] * (m+2) for _ in range(n+2)]
    queue = deque()
    queue.append((0,0))
    visit[0][0] = True

    while queue :
        i, j = queue.popleft()
        cheese[i][j] = -1

        for r, c in move :
            x = i + r
            y = j + c
            if 0 <= x < n+2 and 0 <= y < m+2 :
                if not visit[x][y] and cheese[x][y] != 1:
                    queue.append((x,y))
                    visit[x][y] = True

def outCheese() :
    global cnt

    out = []
    for i in range(1,n+1) :
        for j in range(1,m+1) :
            if cheese[i][j] == 1 :
                tmp = 0
                for r, c in move :
                    if cheese[i+r][j+c] < 0 :
                        tmp += 1
                if tmp >= 2 :
                    out.append((i,j))
                    cnt -= 1

    for i, j in out :
        cheese[i][j] = -1

n, m = map(int,sys.stdin.readline().split())
cheese = [[0 for _ in range(m+2)] for _ in range(n+2)]
cnt = 0
answer = 0
move = [(-1,0),(1,0),(0,-1),(0,1)]
for i in range(1,n+1) :
    x = list(map(int,sys.stdin.readline().split()))
    for j in range(m) :
        if x[j] == 1 :
            cheese[i][j+1] = 1
            cnt += 1

while cnt > 0 :
    BFS()
    outCheese()
    answer += 1

print(answer)