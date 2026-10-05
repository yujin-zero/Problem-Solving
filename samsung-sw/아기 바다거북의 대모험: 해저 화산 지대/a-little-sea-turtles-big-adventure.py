## 바다거북 M마리 (1~M번), K = 해저 화산 수, N = 격자 크기
## 바다 N x N / 산호초(1), 다른 바다거북(2), 화석(3) => 통과 못함, 0: 빈공간.
## 안식처 (N-1, N-1)
## 최대 100턴. 각 턴은 4단계
## 1. ID가 작은 순으로 이동. 최단 경로 탐색 -> 한 칸 이동. (우하좌상 순.) 최단 경로가 없으면 제자리
## 2. 모든 해저 화산의 마그마 압력 10씩 증가
## 3. P: 분출 임계치
## 4. 환경 초기화

from collections import deque
import sys

def find_route(a, b) :
    global N
    INF = N*N + 10
    graph = [[INF for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append((N-1, N-1, 0))
    graph[N-1][N-1] = 0

    while queue :
        x, y, dis = queue.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)] :
            new_x = x + dx
            new_y = y + dy
            if not ((0<=new_x<N) and (0<=new_y<N)) :
                continue
            if sea[new_x][new_y] != 0 :
                continue
            if graph[new_x][new_y] == INF :
                queue.append((new_x, new_y, dis+1))
                graph[new_x][new_y] = dis+1

    return graph

def move_turtle(M, turn) :
    INF = N*N + 10
    for i in range(M) :
        if i in dead_turtle :
            continue
        x, y = turtle[i]
        ## 거리 찾기
        distance_graph = find_route(x, y)
        min_value = INF
        for mx, my in move :
            new_x = x + mx
            new_y = y + my
            if not ((0<=new_x<N) and (0<=new_y<N)) :
                continue
            min_value = min(min_value, distance_graph[new_x][new_y])
        if min_value == INF :
            ## 이동할 수 없음
            continue
        for mx, my in move : 
            new_x = x + mx
            new_y = y + my
            if not ((0<=new_x<N) and (0<=new_y<N)) :
                continue
            if distance_graph[new_x][new_y] == min_value :
                ## 이동
                if (new_x == N-1) and (new_y == N-1) :
                    sea[x][y] = 0
                    dead_turtle.append(i)
                    answer[i] = turn
                else:
                    sea[new_x][new_y] = 2
                    sea[x][y] = 0
                    turtle[i][0], turtle[i][1] = new_x, new_y
                break

def up_magma() :
    for r, c, P in fire :
        magma_graph[r][c] += 10

def spread_heat() :
    global N
    result = []
    for r, c, P in fire :
        if magma_graph[r][c] < P :
            continue

        result.append((r,c))
        heat_graph[r][c] += P
        tmp_p = P // 2
        idx = 1
        stop_list = [False, False, False, False]
        while True :
            stop_signal = True
            for sl in stop_list :
                if not sl :
                    stop_signal = False
                    break
            if stop_signal :
                break
            for direct in range(4) :
                if stop_list[direct] :
                    continue
                dx, dy = move[direct]
                new_x = r + (dx * idx)
                new_y = c + (dy * idx)
                if not ((0<=new_x<N) and (0<=new_y<N)) :
                    stop_list[direct] = True
                    continue
                if sea[new_x][new_y] == 1 or tmp_p == 0 :
                    stop_list[direct] = True
                    continue
                heat_graph[new_x][new_y] += tmp_p
            idx += 1
            tmp_p //= 2

    return result

def chain_fire(visit) :
    queue = deque()
    for r, c, P in fire :
        if magma_graph[r][c] + heat_graph[r][c] >= P :
            if (r,c) in visit :
                continue
            queue.append((r,c,P))
            visit.append((r,c))
    
    while queue :
        r, c, P = queue.popleft()

        ## 분출
        heat_graph[r][c] += P
        tmp_p = P // 2
        idx = 1
        stop_list = [False, False, False, False]
        while True :
            stop_signal = True
            for sl in stop_list :
                if not sl :
                    stop_signal = False
                    break
            if stop_signal :
                break
            for direct in range(4) :
                if stop_list[direct] :
                    continue
                dx, dy = move[direct]
                new_x = r + (dx * idx)
                new_y = c + (dy * idx)
                if not ((0<=new_x<N) and (0<=new_y<N)) :
                    stop_list[direct] = True
                    continue
                if sea[new_x][new_y] == 1 or tmp_p == 0 :
                    stop_list[direct] = True
                    continue
                heat_graph[new_x][new_y] += tmp_p
            idx += 1
            tmp_p //= 2

        ## 새로운 화산 넣기
        for r2, c2, P2 in fire :
            if magma_graph[r2][c2] + heat_graph[r2][c2] >= P2 :
                if (r2,c2) not in visit :
                    queue.append((r2,c2,P2))
                    visit.append((r2,c2))
        
    return visit

def fossil() :
    global M
    for i in range(M) :
        if i in dead_turtle :
            continue
        x, y = turtle[i]
        if heat_graph[x][y] >= 20 :
            dead_turtle.append(i)
            sea[x][y] = 3

def clear_heat() :
    global N
    for i in range(N) :
        for j in range(N) :
            heat_graph[i][j] = 0

def clear_magma(pop_list) :
    for r, c in pop_list :
        magma_graph[r][c] = 0

## 입력
N, M, K = map(int, input().split())
sea = []
turtle = []
dead_turtle = []
# turtle_graph = [[0 for _ in range(N)] for _ in range(N)]
fire = []
fire_graph = [[0 for _ in range(N)] for _ in range(N)]
magma_graph = [[0 for _ in range(N)] for _ in range(N)]
heat_graph = [[0 for _ in range(N)] for _ in range(N)]
move = [(0,1),(1,0),(0,-1),(-1,0)]
for _ in range(N) :
    x = list(map(int, input().split()))
    sea.append(x)
for _ in range(M) :
    r, c = map(int, input().split())
    turtle.append([r,c])
    # turtle_graph[r][c] = 1
    sea[r][c] = 2
for _ in range(K) :
    r, c, P = map(int, input().split())
    fire.append((r,c,P))
    fire_graph[r][c] = P
answer = [-1] * M

for turn in range(1,101) :
    ## 1단계
    move_turtle(M, turn)

    ## 2단계
    up_magma()

    ## 3단계
    ## 1. 열기 전파
    pop_list = spread_heat()
    ## 2. 연쇄 반응
    pop_list = chain_fire(pop_list)
    ## 3. 바다거북의 위기
    fossil()

    ## 4단계
    clear_heat()
    clear_magma(pop_list)

for a in answer :
    print(a)
