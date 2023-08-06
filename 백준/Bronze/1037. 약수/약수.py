import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
if n == 1:
    result = num[0]**2
else:
    result = num[0]*num[-1]

print(result)
