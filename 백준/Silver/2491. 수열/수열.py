import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

countBig = 0
countSmall = 0
tempBig = 0
tempSmall = 0
for i in range(1, n):
    if num[i-1] < num[i]:
        tempBig += 1
        countSmall = max(countSmall, tempSmall)
        tempSmall = 0
    elif num[i-1] == num[i]:
        tempBig += 1
        tempSmall += 1
    else:
        countBig = max(countBig, tempBig)
        tempBig = 0
        tempSmall += 1

countBig = max(countBig, tempBig)
countSmall = max(countSmall, tempSmall)

print(max(countBig+1, countSmall+1))
