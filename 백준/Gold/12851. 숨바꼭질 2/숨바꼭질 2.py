import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
queue = deque()
quickTime = 100009
answerCnt = 0
queue.append((n,0))
dp = [float('inf')] * 200001
dp[n] = 0

while queue :
    pos, sec = queue.popleft()

    if pos == k :
        if sec < quickTime :
            quickTime = sec
            answerCnt = 1
        elif sec == quickTime :
            answerCnt += 1
    elif pos > k :
        sec += (pos-k)
        if sec < quickTime :
            quickTime = sec
            answerCnt = 1
        elif sec == quickTime :
            answerCnt += 1
    else :
        if 2*pos <= 200000 :
            if dp[2*pos] >= sec+1 :
                queue.append((2*pos,sec+1))
                dp[2*pos] = sec+1
        if pos+1 <= 200000 :
            if dp[pos+1] >= sec+1 :
                queue.append((pos+1,sec+1))
                dp[pos+1] = sec+1
        if pos-1 >= 0 :
            if dp[pos-1] >= sec+1 :
                queue.append((pos-1,sec+1))
                dp[pos-1] = sec+1

print(quickTime)
print(answerCnt)
