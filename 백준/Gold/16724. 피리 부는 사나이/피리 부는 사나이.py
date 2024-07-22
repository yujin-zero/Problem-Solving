import sys

def go(a,b, c) :
    global cnt
    visit[a][b] = c 
    
    if Map[a][b] == 'U' :
        a -= 1
    elif Map[a][b] == 'D' :
        a += 1
    elif Map[a][b] == 'L' :
        b -= 1
    else :
        b += 1
    
    if visit[a][b] == 0 :
        go(a,b,c)
    elif visit[a][b] == c:
        cnt += 1

n, m = map(int,sys.stdin.readline().split())
Map = []
cnt = 0
tmp = 1
visit = [[0]*m for _ in range(n)] # 방문해야하는지
for _ in range(n) :
    x = list(sys.stdin.readline().rstrip())
    Map.append(x)

for i in range(n) :
    for j in range(m) :
        if visit[i][j] == 0  : 
            go(i,j,tmp)
            tmp += 1

print(cnt)