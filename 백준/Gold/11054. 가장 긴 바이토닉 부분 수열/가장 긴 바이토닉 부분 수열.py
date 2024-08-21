import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
answer = 0

dp1 = []

for i in range(n) :
    m = 0
    for j in range(i) :
        if a[i] > a[j] :
            m = max(m,dp1[j])
    dp1.append(m+1)

dp2 = [0] * n

for i in range(n-1,-1,-1) :
    m = 0
    for j in range(n-1,i,-1) :
        if a[i] > a[j] :
            m = max(m,dp2[j])
    dp2[i] = m+1

for i in range(n) :
    value = a[i]
    tmp1 = 0 
    for j in range(i-1,-1,-1) :
        if a[j] < value :
            tmp1 = max(tmp1,dp1[j])
    tmp2 = 0
    for j in range(i+1,n) :
        if a[j] < value :
            tmp2 = max(tmp2,dp2[j])
    answer = max(answer,tmp1+tmp2)

print(answer+1)