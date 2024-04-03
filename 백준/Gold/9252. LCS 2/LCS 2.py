import sys

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()
dp = [["" for _ in range(len(str1))] for _ in range(len(str2))]

n1 = len(str1)
n2 = len(str2)
cnt = n1 + n2 - 1

if str1[0] == str2[0]:
    dp[0][0] = str1[0]
for i in range(1, n1):
    if dp[0][i-1] != "":
        dp[0][i] = dp[0][i-1]
    else:
        if str1[i] == str2[0]:
            dp[0][i] = str2[0]
for i in range(1, n2):
    if dp[i-1][0] != "":
        dp[i][0] = dp[i-1][0]
    else:
        if str1[0] == str2[i]:
            dp[i][0] = str1[0]

start = 1

while True:
    for i in range(start, n1):
        if str2[start] == str1[i]:
            dp[start][i] = dp[start-1][i-1] + str1[i]
        else:
            if len(dp[start-1][i]) > len(dp[start][i-1]):
                dp[start][i] = dp[start-1][i]
            else:
                dp[start][i] = dp[start][i-1]
    cnt += (n1-start)
    if cnt == n1*n2:
        break

    for i in range(start+1, n2):
        if str1[start] == str2[i]:
            dp[i][start] = dp[i-1][start-1] + str2[i]
        else:
            if len(dp[i-1][start]) > len(dp[i][start-1]):
                dp[i][start] = dp[i-1][start]
            else:
                dp[i][start] = dp[i][start-1]
    cnt += (n2-start-1)
    if cnt == n1*n2:
        break
    start += 1

if len(dp[n2-1][n1-1]) == 0:
    print(0)
else:
    print(len(dp[n2-1][n1-1]))
    print(dp[n2-1][n1-1])
