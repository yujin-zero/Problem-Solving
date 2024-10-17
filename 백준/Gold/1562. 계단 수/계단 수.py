import sys

n = int(sys.stdin.readline())
dp = [[[0 for _ in range(2**10)] for _ in range(10)] for _ in range(n+1)]
answer = 0
mod = 1000000000

for j in range(1,10) :
    dp[1][j][1 << j] = 1

for i in range(1,n) : # n-1 번째 까지해서 다음 거 저장
    for j in range(10) : # 마지막숫자
        for k in range(2**10) : # 방문현황
            tmp = dp[i][j][k] # 갯수
            if j < 9 :
                nextJ = j + 1
                nextV = k | (1 << nextJ) # 방문처리
                dp[i+1][nextJ][nextV] += tmp
                dp[i+1][nextJ][nextV] %= mod
            if j > 0 :
                beforeJ = j - 1
                nextV = k | (1 << beforeJ)
                dp[i+1][beforeJ][nextV] += tmp
                dp[i+1][beforeJ][nextV] %= mod
S = (1<<10)-1

for j in range(10) :
    answer += dp[n][j][S]
    answer %= mod

print(answer)
