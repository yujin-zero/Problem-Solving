## N x N / K: 로봇 청소기 개수, L: 테스트 횟수
## (1) 먼지 공간: 1~100 (p) / (2) 먼지 없음 / (3) 물건 위치 / -1: 물건 위치
## 1. 청소기 이동 / 가장 가까운 오염된 격자 / 행열오름차순 / 물건, 청소기 자리엔 이동 불가
## 2. 청소 / ㅗ모양으로 청소  / 최대 20 청소  / 우하좌상 순 / 청소기 순서대로
## 3. 먼지 축적 / 먼지 += 5
## 4. 먼지 확산
## 5. 출력

from collections import deque

def find_pollution_coordinate(x, y) :
    global N
    result = []
    queue = deque()
    visit = [[False for _ in range(N+1)] for _ in range(N+1)]
    queue.append((x,y,0))
    visit[x][y] = True
    flag = False
    min_dis = -1

    while queue :
        x, y, dis = queue.popleft()
        if graph[x][y] > 0 :
            if not flag :
                flag = True
                min_dis = dis
                result.append((x, y))
            else :
                if dis == min_dis :
                    result.append((x,y))
                else :
                    break
        for dx, dy in move :
            new_x = x + dx
            new_y = y + dy
            if not ((1 <= new_x <= N) and (1 <= new_y <= N)) :
                continue
            if graph[new_x][new_y] == -1 :
                continue
            if robot_graph[new_x][new_y] > 0 :
                continue
            if visit[new_x][new_y] :
                continue
            queue.append((new_x, new_y, dis+1))
            visit[new_x][new_y] = True

    return result


def move_robot() :
    global K
    for i in range(K) :
        x, y = robot[i]
        ## 가장 가까운 오염된 격자들 찾기
        tmp = find_pollution_coordinate(x, y)
        tmp.sort(key = lambda x : (x[0], x[1]))
        if tmp :
            new_x, new_y = tmp[0]
        else :
            new_x, new_y = x, y
        ## 이동
        robot[i][0] = new_x
        robot[i][1] = new_y
        robot_graph[x][y] = 0
        robot_graph[new_x][new_y] = i+1

def find_clean_direction(x, y) :
    global N
    ## 먼지양 구하기
    dust_list = [0] * 4
    tmp_sum = 0
    tmp_sum += graph[x][y]
    for dx, dy in move:
        new_x = x + dx
        new_y = y + dy
        if not ((1 <= new_x <= N) and (1 <= new_y <= N)) :
            continue
        if graph[new_x][new_y] == -1 :
            continue
        tmp = graph[new_x][new_y]
        if tmp > 20 :
            tmp = 20
        tmp_sum += tmp
    for i in range(4) :
        dx, dy = exception_direction[i]
        new_x = x + dx
        new_y = y + dy
        if not ((1 <= new_x <= N) and (1 <= new_y <= N)) :
            dust_list[i] = tmp_sum
            continue
        if graph[new_x][new_y] == -1 :
            dust_list[i] = tmp_sum
            continue
        tmp = graph[new_x][new_y]
        if tmp > 20 :
            tmp = 20
        dust_list[i] = tmp_sum - tmp
    max_value = max(dust_list)
    for i in range(4) :
        if dust_list[i] == max_value :
            return i

def cleaning() :
    global K
    global N
    for i in range(K) :
        # print(i+1, "번 청소")
        x, y = robot[i]
        ## 청소 방향 구하기 / 오른, 아래, 왼, 위
        clean_direction = find_clean_direction(x, y)
        ## 청소
        graph[x][y] = max(0, graph[x][y] - 20)
        for j in range(4) :
            if j == clean_direction :
                continue
            dx, dy = exception_direction[j]
            new_x = x + dx
            new_y = y + dy
            if not ((1 <= new_x <= N) and (1 <= new_y <= N)) :
                continue
            if graph[new_x][new_y] == -1 :
                continue
            graph[new_x][new_y] = max(0, graph[new_x][new_y] - 20)

def accumulation_dust() :
    global N
    for i in range(1, N+1) :
        for j in range(1, N+1) :
            if graph[i][j] > 0 :
                graph[i][j] += 5


def diffusion_dust() :
    global N
    add_dust = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N+1) :
        for j in range(1, N+1) :
            if graph[i][j] != 0 :
                continue
            # if robot_graph[i][j] != 0 :
            #     # print(i, j)
            #     continue
            tmp = 0
            for dx, dy in move :
                new_x = i + dx
                new_y = j + dy
                if not ((1 <= new_x <= N) and (1 <= new_y <= N)) :
                    continue
                if graph[new_x][new_y] == -1 :
                    continue
                tmp += graph[new_x][new_y]
            add_dust[i][j] = tmp//10
 
    for i in range(1, N+1) :
        for j in range(1, N+1) :
            graph[i][j] += add_dust[i][j]             

def calculate_dust_sum() :
    global N
    result = 0
    for i in range(1, N+1) :
        for j in range(1, N+1) :
            if graph[i][j] <= 0 :
                continue
            result += graph[i][j]
    return result

## 입력
N, K, L = map(int, input().split())
move = [(0,1),(1,0),(0,-1),(-1,0)] # 오른, 아래, 왼, 위
exception_direction = [(0,-1),(-1,0),(0,1),(1,0)] # 왼, 위, 오른, 아래
graph = [[-1 for _ in range(N+1)]]
robot = []
robot_graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(N) :
    x = list(map(int, input().split()))
    graph.append([-1] + x)
for i in range(1, K+1) :
    r, c = map(int, input().split())
    robot.append([r,c])
    robot_graph[r][c] = i

for _ in range(L) :
    
    ## 1. 청소기 이동
    move_robot()

    ## 2. 청소
    cleaning()

    ## 3. 먼지 축적
    accumulation_dust()

    ## 4. 먼지 확산
    diffusion_dust()

    ## 5. 출력
    ds = calculate_dust_sum()
    print(ds)

    if ds == 0 :
        break




# for i in range(1, N+1) :
#     for j in range(1, N+1) :
#         print("%2d" % graph[i][j], end = ' ')
#     print()
# print("------")
# for i in range(1, N+1) :
#     for j in range(1, N+1) :
#         print("%2d" % robot_graph[i][j], end = ' ')
#     print()