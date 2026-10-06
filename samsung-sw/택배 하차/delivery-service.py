## N x N / M: 택배 갯수
## 1. 택배 투입  / 택배  k: 택배 번호, h: 세로 크기, w: 가로 크기, c: 왼쪽 열
## 2. 택배 하차(좌측)  (택배 번호순)
## 3. 택배 하자(우측)
def down_k_cnt(k, cnt) :
    ## 우선 없애
    x, y = coordinate[k]
    w, h = package_info[k]
    for i in range(x, x-h, -1) :
        for j in range(y, y+w) :
            graph[i][j] = 0

    ## 새로운 자리
    coordinate[k][0] += cnt
    x, y = coordinate[k]
    for i in range(x, x-h, -1) :
        for j in range(y, y+w) :
            graph[i][j] = k

def gravitation() :
    global N 

    for k in input_list :
        x, y = coordinate[k]
        w, h = package_info[k]
        ## 봐야할 열
        tmp = [[-1,-1] for _ in range(w)]
        for i in range(w) :
            tmp[i] = [x, y+i]
        down_cnt = 0

        while True :
            for i in range(w) :
                tmp[i][0] += 1
            ## 아래가 비어있는지 확인
            is_empty = True
            for next_x, next_y in tmp :
                if next_x >= N :
                    is_empty = False
                    break
                if graph[next_x][next_y] != 0:
                    is_empty = False
                    break
            if is_empty :
                down_cnt += 1
            else :
                break
        
        ## k번 down_cnt칸 내리기
        down_k_cnt(k, down_cnt)


def stack_package(k, h, w, c) :
    for i in range(h) :
        for j in range(c-1, c-1+w) :
            graph[i][j] = k
    
    package_info[k] = (w, h)
    coordinate[k] = [h-1, c-1]
    input_list.append(k)
    gravitation()

def can_off_left(k) :
    x, y = coordinate[k]
    w, h = package_info[k]

    tmp = [[-1,-1] for _ in range(h)]
    for i in range(h) :
        tmp[i] = [x-i, y]
    while True :
        for i in range(h) :
            tmp[i][1] -= 1
        is_empty = True
        for next_x, next_y in tmp :
            if next_y < 0 :
                is_empty = False
                break
            if graph[next_x][next_y] != 0 :
                is_empty = False
                break
        if not is_empty :
            break

    if tmp[0][1] < 0 :
        return True
    return False

def get_off_left() :
    small_list = sorted(input_list)

    for k in small_list :
        if can_off_left(k) :
            return k

def can_off_right(k) :
    global N
    x, y = coordinate[k]
    w, h = package_info[k]

    tmp = [[-1,-1] for _ in range(h)]
    for i in range(h) :
        tmp[i] = [x-i, y+w-1]
    while True :
        for i in range(h) :
            tmp[i][1] += 1
        is_empty = True
        for next_x, next_y in tmp :
            if next_y >= N :
                is_empty = False
                break
            if graph[next_x][next_y] != 0 :
                is_empty = False
                break
        if not is_empty :
            break

    if tmp[0][1] >= N :
        return True
    return False

def get_off_right() :
    small_list = sorted(input_list)

    for k in small_list :
        if can_off_right(k) :
            return k

def out_list_k(k) :
    x, y = coordinate[k]
    w, h = package_info[k]

    for i in range(x, x-h, -1) :
        for j in range(y, y+w) :
            graph[i][j] = 0
    
    input_list.remove(k)

## 입력
N, M = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(N)]
coordinate = dict()
package_info = dict() # w, h
input_list = []
answer = []
for _ in range(M) :
    k, h, w, c = map(int, input().split()) # 1,2,1,3
    ## 1. 택배 투입
    stack_package(k, h, w, c)

while input_list :
    ## 2. 택배 하차(좌측)
    out_package = get_off_left()
    answer.append(out_package)
    out_list_k(out_package)
    if not input_list :
        break
    gravitation()

    ## 3. 택배 하자(우측)
    out_package = get_off_right()
    answer.append(out_package)
    out_list_k(out_package)
    gravitation()

for a in answer :
    print(a)