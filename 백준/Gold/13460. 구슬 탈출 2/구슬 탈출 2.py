import sys
from collections import deque

# 90도 회전함수
def rotate_90(matrix) :
    new_matrix = []
    new_n = len(matrix[0])
    new_m = len(matrix)
    
    for i in range(new_n) :
        line = []
        for j in range(new_m-1,-1,-1) :
            line.append(matrix[j][i])
        new_matrix.append(line)

    return new_matrix

    
# 구슬 하나 아래로 떨어뜨리기
def gravity_one(matrix, x, y) :
    while True :
        next_pos = matrix[x+1][y]
        if next_pos == '#' or next_pos == 'R' or next_pos =='B':
            break

        if next_pos == '.' :
            x += 1
        else : 
            x += 1
            break
    
    return x

N, M = map(int,sys.stdin.readline().split())
graph = []
for i in range(N) :
    x = list(sys.stdin.readline().rstrip())
    graph.append(x)

answer = -1
queue = deque()
queue.append((graph,0))

while queue :
    matrix, cnt = queue.popleft()
    go = True

    if cnt == 11 :
        break

    # print("----")
    # print("cnt : ",cnt)
    # for m in matrix :
    #     print(m)

    if cnt != 0 :
        # 좌표 찾기
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j] == 'R' :
                    R_x, R_y = i, j
                if matrix[i][j] == 'B' :
                    B_x, B_y = i, j

        if R_y == B_y and R_x < B_x :
            # 파란공 먼저
            new_x_B = gravity_one(matrix, B_x, B_y)
            if matrix[new_x_B][B_y] == 'O' :
                go = False
            matrix[new_x_B][B_y] = 'B'
            if B_x != new_x_B :
                matrix[B_x][B_y] = '.'
            # 빨간공 나중
            new_x_R = gravity_one(matrix, R_x, R_y)
            if matrix[new_x_R][R_y] == 'O' :
                answer = cnt
                # print(2)
                print(answer)
                sys.exit()
            matrix[new_x_R][R_y] = 'R'
            if R_x != new_x_R :
                matrix[R_x][R_y] = '.'
        else :
            new_x_R = gravity_one(matrix, R_x, R_y)
            # print("new_x_R : ", new_x_R)
            # print(matrix[new_x_R][R_y])
            if matrix[new_x_R][R_y] == 'O' :
                # print("빨간공 빠짐")
                matrix[R_x][R_y] = '.'
                new_x_B = gravity_one(matrix, B_x, B_y)
                if matrix[new_x_B][B_y] != 'O' :
                    answer = cnt
                    # print(3)
                    print(answer)
                    sys.exit()
                go = False

            matrix[new_x_R][R_y] = 'R'
            if R_x != new_x_R :
                matrix[R_x][R_y] = '.'

            new_x_B = gravity_one(matrix, B_x, B_y)
            matrix[new_x_B][B_y] = 'B'
            if B_x != new_x_B :
                matrix[B_x][B_y] = '.'

        if new_x_R == R_x and new_x_B == B_x :
            go = False

    if go :
        for _ in range(4) :
            matrix = rotate_90(matrix)
            queue.append((matrix,cnt+1))

# print(4)
if answer >= 11 :
    print(-1)
else :
    print(answer)
