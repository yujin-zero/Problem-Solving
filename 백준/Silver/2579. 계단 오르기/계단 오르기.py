import sys

n = int(sys.stdin.readline())
stairs = []
for _ in range(n):
    stairs.append(int(sys.stdin.readline()))

# 동적 계획법
# Dynamic Programming
dp = [0]*n  # i번째 계단까지 도달했을 때 얻을 수 있는 최댓값
dp[0] = stairs[0]
if n >= 2:
    dp[1] = stairs[0]+stairs[1]
if n >= 3:
    dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

for i in range(3, n):
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])

print(dp[-1])
