import sys

n, m = map(int,sys.stdin.readline().split())
chess = [[0 for _ in range(m+1)] for _  in range(n+1)]
queen = list(map(int,sys.stdin.readline().split()))
knight = list(map(int,sys.stdin.readline().split()))
pawn = list(map(int,sys.stdin.readline().split()))

for i in range(1,pawn[0]*2 + 1,2) :
    chess[pawn[i]][pawn[i+1]] = 'P'

ks = []
for i in range(1,knight[0]*2+1,2) :
    chess[knight[i]][knight[i+1]] = 'K'
    ks.append((knight[i],knight[i+1]))

move = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,-2),(2,-1),(2,1),(1,2)]
for k in ks :
    x,y = k[0], k[1]
    for mm in move :
        xx = x+mm[0]
        yy = y+mm[1]
        if (0<xx<=n) and (0<yy<=m) :
            if chess[xx][yy] != 'K' and chess[xx][yy] != 'P' :
                chess[xx][yy] = 1
    
qs = []
for i in range(1,queen[0]*2+1,2) :
    chess[queen[i]][queen[i+1]] = 'Q'
    qs.append((queen[i],queen[i+1]))

move = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
for q in qs :
    x,y = q[0], q[1]
    for mo in move :
        xx = x
        yy = y
        while True :
            xx += mo[0]
            yy += mo[1]
            if (0<xx<=n) and (0<yy<=m) :
                if chess[xx][yy] != 'K' and chess[xx][yy] != 'P' and chess[xx][yy] != 'Q' :
                    chess[xx][yy] = 2
                else :
                    break
            else:
                break

cnt = 0
for i in range(1,n+1) :
    for j in range(1,m+1) :
        if chess[i][j] == 0:
            cnt += 1

print(cnt)
