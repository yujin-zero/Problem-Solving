import sys

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x]) # 최적화
        return parent[x]
    return x

def union(a,b) :
    a = find(a)
    b = find(b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
 
G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
parent = [i for i in range(G+1)]
cnt = 0
for _ in range(P) :
    gate = int(sys.stdin.readline())

    find_gate = find(gate)
    if find_gate == 0 :
        break

    union(find_gate,find_gate-1)
    cnt += 1

print(cnt)