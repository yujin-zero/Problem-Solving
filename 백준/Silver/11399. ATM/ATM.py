import sys

n = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))
sum = 0
total = 0

t.sort()

for x in t:
    s = sum+x
    sum = s
    total += sum

print(total)