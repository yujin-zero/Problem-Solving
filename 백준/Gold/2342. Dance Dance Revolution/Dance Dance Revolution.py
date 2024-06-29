import sys

step = list(map(int,sys.stdin.readline().split()))
n = len(step)
move = [[0,2,2,2,2],[0,1,3,4,3],[0,3,1,3,4],[0,4,3,1,3],[0,3,4,3,1]]
dp = [[[float('inf') for _ in range(5)] for _ in range(5)] for _ in range(n)]

dp[0][0][0] = 0

for i in range(1,n) :
    value = step[i-1]

    for left in range(5) :
        for right in range(5) :
            power = dp[i-1][left][right]
            # 왼쪽 발을 움직이는 경우
            tmp = move[left][value] + power
            if tmp < dp[i][value][right] :
                dp[i][value][right] = tmp
            # 오른쪽 발을 움직이는 경우
            tmp = move[right][value] + power
            if tmp < dp[i][left][value] :
                dp[i][left][value] = tmp

# for i in range(n):
#     for j in range(5) :
#         print(i,dp[i][j])

answer = float('inf')
for x in dp[n-1] :
    for y in x :
        if y < answer :
            answer = y
print(answer)
