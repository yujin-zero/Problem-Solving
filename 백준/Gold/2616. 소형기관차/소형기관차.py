import sys

n = int(sys.stdin.readline())
lst = [0] + list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
answer = 0

for i in range(n) :
    lst[i+1] += lst[i]

dp = [[0 for _ in range(n+1)] for _ in range(3)]

# dp를 3번 업데이트하며 답 찾기
for i in range(m,n+1) :
    tmp = lst[i] - lst[i-m]
    dp[0][i] = max(dp[0][i-1],tmp)

# 2
for i in range(2*m, n+1) :
    tmp = lst[i] - lst[i-m]
    dp[1][i] = max(dp[1][i-1],tmp + dp[0][i-m])

# 3
for i in range(3*m, n+1) :
    tmp = lst[i] - lst[i-m]
    dp[2][i] = max(dp[2][i-1], tmp + dp[1][i-m])

print(dp[2][n])