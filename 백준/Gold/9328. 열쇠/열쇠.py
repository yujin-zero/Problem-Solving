import sys
from collections import deque

def search() :
    global answer

    # BFS
    while queue :
        posX, posY = queue.popleft()

        tmp = graph[posX][posY]
        # print(tmp, posX, posY)
        go = True
        if tmp == '$' :
            answer += 1
        elif 'a' <= tmp <= 'z' :
            have_key[ord(tmp)-97] = True
        elif 'A' <= tmp <= 'Z' :
            if not have_key[ord(tmp)-ord('A')] :
                go = False
                door.append((tmp, posX, posY))
                visit[posX][posY] = False

        if go :
            for mx, my in move :
                new_x = posX + mx
                new_y = posY + my
                if 0 <= new_x < h and 0 <= new_y < w :
                    if not visit[new_x][new_y] and graph[new_x][new_y] != '*':
                        queue.append((new_x,new_y))
                        visit[new_x][new_y] = True

T = int(sys.stdin.readline())
move = [(-1,0),(1,0),(0,-1),(0,1)]
result = []
for _ in range(T) :
    h, w = map(int,sys.stdin.readline().split())
    graph = []
    have_key = [False] * 26 # 0~25 97~122
    visit = [[False for _ in range(w)] for _ in range(h)]
    answer = 0
    for _ in range(h) :
        x = list(sys.stdin.readline().rstrip())
        graph.append(x)
    key = list(sys.stdin.readline().rstrip())
    if key[0] != '0' :
        for k in key :
            have_key[ord(k)-97] = True
    
    # 초기화
    queue = deque()
    for i in range(h) :
        for j in range(w) :
            if i == 0 or i == (h-1) or j == 0 or j == (w-1) :
                if graph[i][j] != '*' :
                    queue.append((i,j))
                    visit[i][j] = True
    
    door = []

    while True :
        search()

        # 대문자 갈 수 있는 곳 추가
        gg = True
        for ddoor, go_x, go_y in door :
            if have_key[ord(ddoor) - ord('A')] and not visit[go_x][go_y]:
                queue.append((go_x, go_y))
                visit[go_x][go_y] = True
                gg = False

        # 없으면 종료
        if gg :
            break

    result.append(answer)

for r in result :
    print(r)
