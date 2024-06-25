import sys
sys.setrecursionlimit(10**5)

def partition(aa, pp, rr) :
    global cnt
    global k 
    x = aa[rr]
    i = pp-1
    for j in range(pp,rr) :
        if aa[j] <= x :
            i += 1
            tmp = aa[i]
            aa[i] = aa[j]
            aa[j] = tmp
            cnt += 1
            if cnt == k :
                for value in aa :
                    print(value, end=' ')
    if i+1 != rr :
        tmp = aa[i+1]
        aa[i+1] = aa[rr]
        aa[rr] = tmp
        cnt += 1
        if cnt == k :
            for value in aa :
                print(value, end=' ')
    return i+1

def select(a,p,r,q) :
    if p==r :
        return a[p]
    t = partition(a,p,r)
    k = t-p+1
    if q<k :
        return select(a,p,t-1,q)
    elif q==k :
        return a[t]
    else:
        return select(a,t+1,r,q-k)

n,q,k = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
cnt = 0
select(a,0,n-1,q)
if cnt < k :
    print(-1)