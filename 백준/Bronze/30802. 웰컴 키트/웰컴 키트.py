import sys

n = int(sys.stdin.readline())
size = list(map(int,sys.stdin.readline().split()))
t, p = map(int,sys.stdin.readline().split())

cntT = 0
cntP = 0
total = sum(size)

for s in size :
    cntT += (s//t)
    if s%t != 0 :
        cntT += 1

print(cntT)
print(total//p, total%p)
