import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = []

for i in range(n):
    m = 0
    for j in range(0, i):
        if a[i] > a[j]:
            if dp[j] > m:
                m = dp[j]
    dp.append(m+1)

print(max(dp))
