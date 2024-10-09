import sys
import bisect

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
lis = [-float('inf')]

for value in A :
    if value > lis[-1] :
        lis.append(value)
    else :
        idx = bisect.bisect_left(lis,value)
        lis[idx] = value

print(len(lis)-1)
