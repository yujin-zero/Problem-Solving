import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
graph = []
group_width = [0,0] # 그룹번호의 너비를 담는 리스트
group_num = 2
move = [(-1,0),(1,0),(0,1),(0,-1)]
for _ in range(n) :
    x = list(map(int,sys.stdin.readline().rstrip()))
    graph.append(x)

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0 :
            # BFS해서 그룹번호 저장
            cnt = 1
            graph[i][j] = group_num
            queue = deque()
            queue.append((i,j))

            while queue :
                x, y = queue.popleft()
                for xx, yy in move :
                    X = x + xx
                    Y = y + yy
                    if 0 <= X < n and 0 <= Y < m :
                        if graph[X][Y] == 0 :
                            queue.append((X,Y))
                            graph[X][Y] = group_num
                            cnt += 1

            group_width.append(cnt)
            group_num += 1

new_graph = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            add_list = set()
            for a, b in move :
                I = i + a
                J = j + b
                if 0 <= I < n and 0 <= J < m :
                    add_list.add(graph[I][J])
            for al in add_list :
                new_graph[i][j] += group_width[al]
            new_graph[i][j] += 1
            new_graph[i][j] %= 10

for x in new_graph :
    print("".join(map(str,x)))
