import sys

n = int(sys.stdin.readline())
cost = []
for _ in range(n):
    cost.append(list(map(int, sys.stdin.readline().split())))
dp = [float('inf'), cost[0][0] + cost[1][1], cost[0][0] + cost[1][2]]

for i in range(2, n-1):
    if dp[1] < dp[2]:
        a = dp[1]+cost[i][0]
    else:
        a = dp[2] + cost[i][0]

    if dp[0] < dp[2]:
        b = dp[0] + cost[i][1]
    else:
        b = dp[2] + cost[i][1]

    if dp[0] < dp[1]:
        c = dp[0] + cost[i][2]
    else:
        c = dp[1] + cost[i][2]

    dp[0] = a
    dp[1] = b
    dp[2] = c

pre1 = min(dp[0], dp[2]) + cost[n-1][1]
pre2 = min(dp[0], dp[1]) + cost[n-1][2]
answer1 = min(pre1, pre2)

#
dp = [cost[0][1]+cost[1][0], float('inf'), cost[0][1]+cost[1][2]]

for i in range(2, n-1):
    if dp[1] < dp[2]:
        a = dp[1]+cost[i][0]
    else:
        a = dp[2] + cost[i][0]

    if dp[0] < dp[2]:
        b = dp[0] + cost[i][1]
    else:
        b = dp[2] + cost[i][1]

    if dp[0] < dp[1]:
        c = dp[0] + cost[i][2]
    else:
        c = dp[1] + cost[i][2]

    dp[0] = a
    dp[1] = b
    dp[2] = c

pre1 = min(dp[1], dp[2]) + cost[n-1][0]
pre2 = min(dp[0], dp[1]) + cost[n-1][2]
answer2 = min(pre1, pre2)

#
dp = [cost[0][2] + cost[1][0], cost[0][2] + cost[1][1], float('inf')]

for i in range(2, n-1):
    if dp[1] < dp[2]:
        a = dp[1]+cost[i][0]
    else:
        a = dp[2] + cost[i][0]

    if dp[0] < dp[2]:
        b = dp[0] + cost[i][1]
    else:
        b = dp[2] + cost[i][1]

    if dp[0] < dp[1]:
        c = dp[0] + cost[i][2]
    else:
        c = dp[1] + cost[i][2]

    dp[0] = a
    dp[1] = b
    dp[2] = c

pre1 = min(dp[1], dp[2]) + cost[n-1][0]
pre2 = min(dp[0], dp[2]) + cost[n-1][1]
answer3 = min(pre1, pre2)

print(min(answer1, answer2, answer3))
