import sys

## 유니온 파인드로 그룹 묶기

def find(x) :
    if parent[x] == x :
        return x
    
    parent[x] = find(parent[x])
    return parent[x]


def union(x,y) :
    x = find(x)
    y = find(y)

    if x == y :
        return
    
    if x < y :
        parent[y] = x
    else :
        parent[x] = y

n, m, k = map(int,sys.stdin.readline().split())
candy = [0] + list(map(int,sys.stdin.readline().split()))
parent = [i for i in range(n+1)]
group = []
for _ in range(m) :
    a, b = map(int,sys.stdin.readline().split())
    union(a,b)

for i in range(1,n+1) :
    if parent[i] != i :
        parent[i] = find(i)

weight = [0] * (n+1)
value = [0] * (n+1)

for i in range(1,n+1) :
    p = parent[i]

    weight[p] += 1
    value[p] += candy[i]

## 냅색 알고리즘
dp = [0] * (k+1)

for i in range(1,n+1) :
    if weight[i] != 0:
        w = weight[i]
        v = value[i]

        if w > k :
            continue
        
        for j in range(k,-1,-1) :
            if j >= w :
                dp[j] = max(dp[j], dp[j-w]+v)

print(dp[k-1])