import sys

a, b = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))
cnt = len(A) + len(B)
hap = set()

for i in A :
    hap.add(i)
for i in B :
    hap.add(i)

print(len(hap)-cnt+len(hap))