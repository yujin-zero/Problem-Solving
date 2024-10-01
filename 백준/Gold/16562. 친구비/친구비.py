import sys

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

N, M, k = map(int,sys.stdin.readline().split())
cost = [0] + list(map(int,sys.stdin.readline().split()))
parent = [i for i in range(N+1)]
pay = dict()
answer = 0

for _ in range(M) :
    v, w = map(int,sys.stdin.readline().split())

    v = find(v)
    w = find(w)
    union(v,w)

for i in range(1,N+1) :
    group = find(i)
    friend_cost = cost[i]

    if group in pay :
        if pay[group] > friend_cost :
            answer -= pay[group]
            answer += friend_cost
            pay[group] = friend_cost
    else :
        pay[group] = friend_cost
        answer += friend_cost

if answer > k :
    print("Oh no")
else :
    print(answer)
