import sys

C, N = map(int, sys.stdin.readline().split())
lst = []
for _ in range(N) :
    cost, num = map(int, sys.stdin.readline().split())
    lst.append((cost, num))
dp = [float('inf')] * (C+1)
dp[0] = 0

for cus_num in range(1, C+1) :
    for cost, num in lst :
        if cus_num - num < 0 :
            tmp = cost
        else :
            tmp = dp[cus_num - num] + cost
        dp[cus_num] = min(dp[cus_num], tmp)

print(dp[C])