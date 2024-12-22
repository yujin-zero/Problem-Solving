import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    K = int(sys.stdin.readline())
    file = list(map(int,sys.stdin.readline().split()))
    dp = [[0 for _ in range(K)] for _ in range(K)]
    hap = [0] * (K+1)

    hap[1] = file[0]
    for i in range(2,K+1) :
        hap[i] = hap[i-1] + file[i-1]

    for i in range(K) :
        dp[i][i] = file[i]
    
    for j in range(1,K) :
        for i in range(K-j) :
            # i행 j+i열
            value = float('inf')
            for x in range(i,j+i) :
                one = dp[i][x]
                two = dp[1+x][j+i]
                tmp = 0
                if i != x :
                    tmp += one
                if x+1 != j+i :
                    tmp += two
                tmp += (hap[j+i+1] - hap[i])
                value = min(value,tmp)
            dp[i][j+i] = value

    print(dp[0][K-1])