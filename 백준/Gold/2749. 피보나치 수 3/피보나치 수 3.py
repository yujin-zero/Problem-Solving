import sys

def f(x) : 
    if x in dp :
        return dp[x]
    
    if x%2 == 0 :
        k = x//2
        dp[x] =  (f(k)*(2*f(k-1)+f(k))) % 1000000
    else :
        k = (x-1)//2
        dp[x] = (f(k+1)*f(k+1) + f(k)*f(k)) % 1000000
    
    return dp[x]


n = int(sys.stdin.readline())
dp = {0:0, 1:1}
print(f(n))
