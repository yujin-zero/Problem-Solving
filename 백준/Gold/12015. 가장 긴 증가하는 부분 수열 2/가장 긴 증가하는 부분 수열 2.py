import sys
import bisect

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
lis = []

for value in a:
    if not lis or value > lis[-1]:
        lis.append(value)
    else:
        idx = bisect.bisect_left(lis, value)
        lis[idx] = value

print(len(lis))
