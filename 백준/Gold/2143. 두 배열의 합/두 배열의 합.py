import sys

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))
answer = 0

sumA = [0]
sumB = [0]
for i in range(n) :
    sumA.append(sumA[i] + A[i])
for i in range(m) :
    sumB.append(sumB[i] + B[i])

cnt_A = dict()
cnt_B = dict()
for i in range(len(sumA)-1) :
    for j in range(i+1,len(sumA)) :
        tmp = sumA[j] - sumA[i]
        if tmp in cnt_A :
            cnt_A[tmp] += 1
        else :
            cnt_A[tmp] = 1
for i in range(len(sumB)-1) :
    for j in range(i+1,len(sumB)) :
        tmp = sumB[j] - sumB[i]
        if tmp in cnt_B :
            cnt_B[tmp] += 1
        else :
            cnt_B[tmp] = 1

for a in cnt_A :
    if t-a in cnt_B :
        answer += (cnt_A[a] * cnt_B[t-a])

print(answer)
