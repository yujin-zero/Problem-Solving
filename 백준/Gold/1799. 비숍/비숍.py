import sys

def go(k,cnt) :
    global answer
    if k == (2*n-1) :
        answer = max(answer,cnt)
        return
    
    # 가지치기
    if (cnt + 2*n-1-k) <= answer :
        return

    for i,j in right[k] :
        t = i-j+n-1
        if left[t] :
            left[t] = False
            go(k+1,cnt+1)
            left[t] = True

    go(k+1,cnt)

n = int(sys.stdin.readline())
chess = []
for _ in range(n) :
    x = list(map(int,sys.stdin.readline().split()))
    chess.append(x)
answer = 0

right = [[] for _ in range(n*2 - 1)]
left = [True] * (n*2-1) # 둘 수 있는지

# 우 상향 대각에서 갈 수 있는 곳 저장
for i in range(n) :
    for j in range(n) :
        if chess[i][j] == 1 :
            right[i+j].append((i,j))

go(0,0) # k, cnt
print(answer)