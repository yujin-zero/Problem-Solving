from collections import deque

def find_1234(r, c, d) :
    result = []

    tmp = [0,0,0,0]
    ## 1 -> 3 -> 4 -> 2
    ## 2 -> 4 -> 3 -> 1
    ## 3 -> 2 -> 1 -> 4
    ## 4 -> 1 -> 2 -> 3
    if d == 1 :
        tmp = [1, 3, 4, 2]
    elif d == 2 :
        tmp = [2, 4, 3, 1]
    elif d == 3 :
        tmp = [3, 2, 1, 4]
    else :
        tmp = [4, 1, 2, 3]

    for t in tmp :
        dx, dy = way[t]
        result.append((r+dx, c+dy, t))

    return result

def go1() :
    global r,c,d, N

    ## 1,2,3,4 이동 좌표 구하기
    move_list = find_1234(r,c,d)
    for new_x, new_y, t in move_list :
        if not ((0<=new_x<N) and (0<=new_y<N)) :
            continue
        if bada[new_x][new_y] == 0 :
            return (new_x, new_y, t)

    return False

def find_close(r,c,N) :
    queue = deque()
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[r][c] = True
    queue.append((r,c,0))
    tmp = N*N + 10
    result = []

    while queue :
        x, y, distance = queue.popleft()
        if bada[x][y] == 0 :
            if distance > tmp :
                break
            tmp = distance
            result.append((x, y, tmp))
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)] :
            new_x = x + dx
            new_y = y + dy
            if not ((0<=new_x<N) and (0<=new_y<N)) :
                continue
            if bada[new_x][new_y] == 1:
                continue
            if visit[new_x][new_y] :
                continue
            queue.append((new_x, new_y, distance+1))
            visit[new_x][new_y] = True

    result.sort(key=lambda x: (x[0], x[1]))
    return result[0]

def find_distance(a,b,c,d,N,short_dis) :
    result = [[-1 for _ in range(N)] for _ in range(N)]
    visit = [[False for _ in range(N)] for _ in range(N)]
    queue = deque()
    result[c][d] = 0
    visit[c][d] = True
    queue.append((c,d,0))

    while queue :
        x, y, dis = queue.popleft()
        if dis > short_dis :
            break
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)] :
            new_x = x + dx
            new_y = y + dy
            if not ((0<=new_x<N) and (0<=new_y<N)) :
                continue
            if bada[new_x][new_y] == 1:
                continue
            if visit[new_x][new_y] :
                continue
            queue.append((new_x, new_y, dis+1))
            visit[new_x][new_y] = True
            result[new_x][new_y] = dis+1

    return result

def go2() :
    global r,c,N

    ## 가장 가까운 칸 구하기
    find_x, find_y, distance = find_close(r,c,N)

    ## 좌 하 우 상 : 3 -> 2 -> 4 -> 1
    ## 이 순서대로 이동했는데 거리가 1 줄어들었으면 된 것.
    ## 거리를 다 구해두자.

    dis_list = find_distance(r,c,find_x,find_y,N,distance)
    tmp = [3,2,4,1]
    goal_dis = distance-1
    d = -1
    x,y = r,c
    while True :
        for t in tmp :
            dx, dy = way[t]
            new_x = x + dx
            new_y = y + dy
            if not ((0<=new_x<N) and (0<=new_y<N)) :
                continue
            if dis_list[new_x][new_y] == goal_dis :
                x = new_x
                y = new_y
                d = t
                break

        if goal_dis == 0 :
            break
        goal_dis -= 1

    return x, y, d

N, r, c, d = map(int, input().split())
r -= 1
c -= 1
bada = [] # 방문 : 2
cnt = 0
for _ in range(N) :
    x = list(map(int, input().split()))
    bada.append(x)
    for xx in x :
        if xx == 0 :
            cnt += 1
way = [(0,0), (-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
bada[r][c] = 2
answer = []
answer.append((r+1,c+1))
cnt -= 1

while True :
    while True :
        value = go1()
        if not value :
            break
        ## 이동
        r,c,d = value
        bada[r][c] = 2
        answer.append((r+1, c+1))
        cnt -= 1
        if cnt == 0 :
            break

    if cnt == 0 :
        break
    
    value2 = go2()
    r,c,d = value2
    bada[r][c] = 2
    answer.append((r+1, c+1))
    cnt -= 1
    if cnt == 0 :
        break

for a in answer :
    print(*a)