import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if num[i] == num[i+1]:
        dp[i][i+1] = 1
for i in range(n-2):
    if num[i] == num[i+2]:
        dp[i][i+2] = 1

cnt = n-3
i = 0
j = 3
tmp = 3
while True:
    if cnt == 0:
        break

    for k in range(cnt):
        if num[i] == num[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1
        i += 1
        j += 1
    i = 0
    tmp += 1
    j = tmp

    cnt -= 1

m = int(sys.stdin.readline())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s-1][e-1])
