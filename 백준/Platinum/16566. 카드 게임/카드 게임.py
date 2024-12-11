import sys

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(a,b) :
    a = find(a)
    b = find(b)
    parent[a] = b

N, M, K = map(int,sys.stdin.readline().split())
holding_card = list(map(int,sys.stdin.readline().split()))
cheolsoo = list(map(int,sys.stdin.readline().split()))
holding_card.sort()
parent = [i for i in range(M+1)]

for card in cheolsoo :
    left = 0
    right = M-1
    
    while left <= right :
        mid = (left+right)//2

        if holding_card[mid] > card :
            right = mid-1
        else :
            left = mid+1
    
    idx = find(left)
    print(holding_card[idx])
    
    union(idx,idx+1)