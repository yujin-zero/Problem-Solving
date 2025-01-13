import sys

def CCW(x1,y1,x2,y2,x3,y3) :
    ccw = (x2-x1) * (y3-y1) - (y2-y1) * (x3-x1)
    return ccw

def cross_line(x1,y1,x2,y2,x3,y3,x4,y4) :
    abc = CCW(x1,y1,x2,y2,x3,y3)
    abd = CCW(x1,y1,x2,y2,x4,y4)
    cdb = CCW(x3,y3,x4,y4,x2,y2)
    cda = CCW(x3,y3,x4,y4,x1,y1)

    if abc * abd < 0 and cda * cdb < 0 :
        return True
    elif abc == 0 and min(x1,x2) <= x3 <= max(x1,x2) and min(y1,y2) <= y3 <= max(y1,y2) :
        return True
    elif abd == 0 and min(x1,x2) <= x4 <= max(x1,x2) and min(y1,y2) <= y4 <= max(y1,y2) :
        return True
    elif cdb == 0 and min(x3,x4) <= x2 <= max(x3,x4) and min(y3,y4) <= y2 <= max(y3,y4) :
        return True
    elif cda == 0 and min(x3,x4) <= x1 <= max(x3,x4) and min(y3,y4) <= y1 <= max(y3,y4) :
        return True
    
    return False

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(a,b) :
    a = find(a)
    b = find(b) 

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

N = int(sys.stdin.readline())
line = []
for _ in range(N) :
    x1, y1, x2, y2 = list(map(int,sys.stdin.readline().split()))
    line.append((x1, y1, x2, y2))
parent = [i for i in range(N)]

for line1 in range(N) :
    for line2 in range(N) :
        if find(line1) == find(line2) :
            continue

        x1, y1, x2, y2 = line[line1]
        x3, y3, x4, y4 = line[line2]
        is_cross = cross_line(x1,y1,x2,y2,x3,y3,x4,y4)

        if is_cross :
            union(line1, line2)

cnt = 0
kind = {}
answer_max = 0
for p in parent :
    if p in kind :
        kind[p] += 1
    else :
        kind[p] = 1
        cnt += 1
    answer_max = max(answer_max, kind[p])

print(cnt)
print(answer_max)