import sys

def bellman_ford() :
    for i in range(n) :
        for j in range(len(edge)) :
            cur, next, cost = edge[j]
            if dist[next] > dist[cur] + cost :
                dist[next] = dist[cur] + cost
                if i == n - 1:
                    return True
    
    return False
    
tc = int(sys.stdin.readline())

for _ in range(tc) :
    n, m, w = map(int,sys.stdin.readline().split())
    edge = []
    dist = [1e9] * (n + 1)

    for _ in range(m) :
        s, e, t = map(int,sys.stdin.readline().split())
        edge.append((s, e, t))
        edge.append((e, s, t))
    
    for _ in range(w) :
        s, e, t = map(int,sys.stdin.readline().split())
        edge.append((s, e, -t))

    if bellman_ford() :
        print("YES")
    else :
        print("NO")