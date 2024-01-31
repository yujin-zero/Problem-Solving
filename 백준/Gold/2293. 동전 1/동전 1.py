import sys

n, k = map(int, sys.stdin.readline().split())
dp = [0]*(k+1)
dp[0] = 1
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))

for c in coin:
    for i in range(c, k+1):
        dp[i] += dp[i-c]

print(dp[k])
