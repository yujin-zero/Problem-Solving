import sys

def palin() :
    for i in range(n) :
        isPal[i][i] = True

    for i in range(2,n) :
        ii = i
        for j in range(1,n+1-i) :
            if x[ii] == x[j] :
                if ii - j <= 2 :
                    isPal[j][ii] = True 
                else :
                    if isPal[j+1][ii-1] :
                        isPal[j][ii] = True

            ii += 1

x = [0] + list(sys.stdin.readline().rstrip())
n = len(x)
isPal = [[False] * n for _ in range(n)]
palin()

dp = [float('inf')] * n
dp[0] = 0

for i in range(1,n) :
    for j in range(i+1) :
        if x[i] == x[j] :
            if isPal[j][i] :
                dp[i] = min(dp[j-1]+1,dp[i])

print(dp[n-1])