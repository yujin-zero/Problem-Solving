import sys

n = int(sys.stdin.readline())
triangle = []
dp = [[0]*i for i in range(1, n)]
for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    triangle.append(line)
    if i == n-1:
        dp.append(line)

for i in range(n-1, 0, -1):
    for j in range(i):
        dp[i-1][j] = max(dp[i][j], dp[i][j+1]) + triangle[i-1][j]

print(dp[0][0])
