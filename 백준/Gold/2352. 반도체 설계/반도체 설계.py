import sys
import bisect

n = int(sys.stdin.readline())
connect = list(map(int,sys.stdin.readline().split()))
lis = [0]

for value in connect :
    if value > lis[-1] :
        lis.append(value)
    else :
        idx = bisect.bisect_left(lis,value)
        lis[idx] = value

print(len(lis) - 1)