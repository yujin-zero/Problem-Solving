import sys

n = int(sys.stdin.readline())
hi = []
power = list(map(int, sys.stdin.readline().split()))
joy = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    if joy[i] != 0:
        hi.append([power[i], joy[i]])

answer = 0
hi.sort(key=lambda x: (x[0]/x[1], -x[0]))
dp = [[0, 0]]  # 체력, 기쁨
for h in hi:
    temp = []
    for d in dp:
        if d[0] + h[0] < 100:
            # if [d[0]+h[0], d[1]+h[1]] not in dp:
            temp.append([d[0]+h[0], d[1]+h[1]])
            if answer < d[1]+h[1]:
                answer = d[1]+h[1]
    for t in temp:
        dp.append(t)

print(answer)
