import sys

n, m = map(int, sys.stdin.readline().split())
ladder = {}
snake = {}
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    ladder[x] = y
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    snake[x] = y

dp = [0]*107
i = 1
while i <= 100:
    if i in snake:
        if dp[snake[i]] > dp[i]:
            dp[snake[i]] = dp[i]
            i = snake[i]
            continue
    else:
        for j in range(i+1, i+7):
            if dp[j] == 0:
                dp[j] = dp[i]+1
            else:
                dp[j] = min(dp[j], dp[i]+1)
        if i in ladder:
            dp[ladder[i]] = dp[i]

    i += 1

print(dp[100])
