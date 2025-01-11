import sys

def dfs(idx) :
    global answer

    if idx >= len(cctv) :
        cnt = 0
        for g in graph :
            for gg in g :
                if gg == 0 :
                    cnt += 1
        answer = min(cnt,answer)

        # for g in graph :
        #     print(g)
        # print("-------")
        return

    i,j = cctv[idx]
    num = graph[i][j]
    
    for l in light[num] :
        add = []
        for ll in l :
            # print("----")
            x, y = move[ll]
            # print("i=",i," j=",j)
            # print("x=",x," y=",y)
            
            current_x = i
            current_y = j

            tmp = 0
            

            while True :
                tmp += 1
                if tmp > 10 :
                    sys.exit()
                next_x = current_x + x
                next_y = current_y + y
                # print(next_x, next_y)

                if 0 <= next_x < N and 0 <= next_y < M :
                    if graph[next_x][next_y] == 6 :
                        break
                    elif graph[next_x][next_y] == 0 :
                        graph[next_x][next_y] = '#'
                        add.append((next_x,next_y))
                        current_x = next_x
                        current_y = next_y
                    else :
                        current_x = next_x
                        current_y = next_y
                else :
                    break

        dfs(idx+1)
        
        for a,b in add :
            graph[a][b] = 0
        

N, M = map(int,sys.stdin.readline().split())
graph = []
cctv = []
for i in range(N) :
    x = list(map(int,sys.stdin.readline().split()))
    graph.append(x)
    for j in range(M) :
        if 0 < x[j] < 6 :
            cctv.append((i,j))

light = [[],[[1],[2],[3],[4]],[[1,2],[3,4]],[[1,4],[2,4],[2,3],[1,3]],[[1,2,3],[1,2,4],[1,3,4],[2,3,4]],[[1,2,3,4]]]
move = [(),(-1,0),(1,0),(0,-1),(0,1)]
answer = float('inf')

dfs(0)
print(answer)