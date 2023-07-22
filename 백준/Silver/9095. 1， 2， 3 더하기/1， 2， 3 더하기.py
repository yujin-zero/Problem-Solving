import sys

t = int(sys.stdin.readline())
case = []
for _ in range(t):
    case.append(int(sys.stdin.readline()))

m = max(case)
dp = [0]*m
dp[0] = 1
if m >= 2:
    dp[1] = 2
if m >= 3:
    dp[2] = 4
for i in range(3, m):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

for i in range(t):
    print(dp[case[i]-1])
