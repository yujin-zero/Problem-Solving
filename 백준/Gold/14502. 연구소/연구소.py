import sys
from collections import deque
import copy

def virusSpread() :
    queue = deque(virus)
    xx = copy.deepcopy(graph)

    while queue :
        vi,vj = queue.popleft()

        for x, y in move :
            newI = vi + x
            newJ = vj + y
            if 0 <= newI < n and 0 <= newJ < m :
                if xx[newI][newJ] == 0 :
                    xx[newI][newJ] = 2
                    queue.append((newI,newJ))
    
    result = 0
    for i in range(n) :
        for j in range(m) :
            if xx[i][j] == 0 :
                result += 1
        
    return result

n, m = map(int,sys.stdin.readline().split())
graph = []
blank = []
virus = []
move = [(-1,0),(1,0),(0,-1),(0,1)]
for i in range(n) :
    x = list(map(int,sys.stdin.readline().split()))
    graph.append(x)
    for j in range(m) :
        if x[j] == 0 :
            blank.append((i,j))
        elif x[j] == 2 :
            virus.append((i,j))
lenBlank = len(blank)
answer = 0

for i in range(lenBlank-2) :
    x1, y1 = blank[i]
    graph[x1][y1] = 1
    for j in range(i+1,lenBlank-1) :
        x2, y2 = blank[j]
        graph[x2][y2] = 1
        for k in range(j+1, lenBlank) :
            x3, y3 = blank[k]
            graph[x3][y3] = 1

            tmp = virusSpread()
            answer = max(answer,tmp)

            graph[x3][y3] = 0
        graph[x2][y2] = 0
    graph[x1][y1] = 0

print(answer)