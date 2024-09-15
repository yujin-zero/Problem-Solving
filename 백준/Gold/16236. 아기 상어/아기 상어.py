import sys
from collections import deque

def calDis(fx,fy) :
    queue = deque()
    visit = [[False] * n for _ in range(n)]
    queue.append((babyX,babyY,0))
    visit[babyX][babyY] = True 

    while queue :
        a, b, t = queue.popleft()
        if a == fx and b == fy :
            return t
        
        for mx, my in move :
            nx = mx + a
            ny = my + b
            if 0 <= nx < n and 0 <= ny < n :
                if visit[nx][ny] == False :
                    if graph[nx][ny] <= babySize :
                        queue.append((nx,ny,t+1))
                        visit[nx][ny] = True
    
    return -1

def eat() :
    tmp = []
    for i in range(n) :
        for j in range(n) :
            if graph[i][j] < babySize and graph[i][j] != 0 :
                dis = calDis(i,j)
                if dis > 0 :
                    tmp.append((i,j,dis))
    return tmp


n = int(sys.stdin.readline())
graph = []
babyX, babyY = -1, -1
babySize = 2
currentEat = 0
sec = 0
move = [(-1,0),(1,0),(0,-1),(0,1)]
for i in range(n) :
    x = list(map(int,sys.stdin.readline().split()))
    for j in range(n) :
        if x[j] == 9 :
            babyX = i
            babyY = j
            x[j] = 0
    graph.append(x)

while True :
    eatFish = eat()
    if len(eatFish) == 0 :
        break
    elif len(eatFish) == 1 :
        nextX, nextY, dis = eatFish[0]
        currentEat += 1
        if currentEat == babySize :
            babySize += 1
            currentEat = 0
        babyX = nextX
        babyY = nextY
        graph[babyX][babyY] = 0
        sec += dis
    else :
        eatFish.sort(key = lambda x : (x[2], x[0], x[1]))
        nextX, nextY, dis = eatFish[0]
        currentEat += 1
        if currentEat == babySize :
            babySize += 1
            currentEat = 0
        babyX = nextX
        babyY = nextY
        graph[babyX][babyY] = 0
        sec += dis

print(sec)