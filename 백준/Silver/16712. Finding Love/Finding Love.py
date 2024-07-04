import sys

n, m = map(int,sys.stdin.readline().split())
info = list(map(int,sys.stdin.readline().split()))
vList = list(map(int,sys.stdin.readline().split()))
i = 0

while len(info) >= m :
    delIndex = vList[i]
    x = info[0:m]
    x.sort()
    delInfo = x[delIndex-1]
    info.remove(delInfo)

    i += 1

for i in sorted(info) :
    print(i,end=' ')